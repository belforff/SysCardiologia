"""Database connection and bootstrap utilities."""

from __future__ import annotations

from contextlib import contextmanager

from config import settings

try:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session, sessionmaker
except ImportError as exc:  # pragma: no cover - handled at runtime for missing deps
    raise RuntimeError(
        "SQLAlchemy is required. Install dependencies from requirements.txt"
    ) from exc

from database.models import Base, Role, RoleType, User
from logic.auth import hash_password

_ENGINE = create_engine(settings.database_url, future=True)
SessionLocal = sessionmaker(bind=_ENGINE, autoflush=False, autocommit=False, future=True)


def get_engine():
    return _ENGINE


@contextmanager
def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def create_db_and_seed_defaults() -> None:
    Base.metadata.create_all(bind=_ENGINE)

    with get_session() as session:
        existing_roles = {role.name for role in session.query(Role).all()}
        for role_type in RoleType:
            if role_type.value not in existing_roles:
                session.add(Role(name=role_type.value))

    with get_session() as session:
        admin = session.query(User).filter(User.username == settings.default_admin_username).one_or_none()
        if admin:
            return
        admin_role = session.query(Role).filter(Role.name == RoleType.ADMIN.value).one()
        session.add(
            User(
                username=settings.default_admin_username,
                full_name="Administrador",
                email="admin@syscardiologia.local",
                password_hash=hash_password(settings.default_admin_password),
                role_id=admin_role.id,
                is_active=True,
            )
        )
