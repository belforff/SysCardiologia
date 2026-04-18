"""Authentication and authorization helpers."""

from __future__ import annotations

import secrets
from datetime import UTC, datetime, timedelta
from typing import Iterable

import bcrypt

from config import settings


class SessionState:
    def __init__(self, user_id: int, role_name: str):
        self.user_id = user_id
        self.role_name = role_name
        self.last_activity = datetime.now(UTC)

    def touch(self) -> None:
        self.last_activity = datetime.now(UTC)

    def is_expired(self) -> bool:
        timeout = timedelta(minutes=settings.session_timeout_minutes)
        return datetime.now(UTC) - self.last_activity > timeout


def hash_password(raw_password: str) -> str:
    if len(raw_password) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres")
    return bcrypt.hashpw(raw_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(raw_password: str, password_hash: str) -> bool:
    try:
        return bcrypt.checkpw(raw_password.encode("utf-8"), password_hash.encode("utf-8"))
    except ValueError:
        return False


def has_role(user_role: str, allowed_roles: Iterable[str]) -> bool:
    return user_role in set(allowed_roles)


def build_reset_token() -> tuple[str, datetime]:
    expiration = datetime.now(UTC) + timedelta(hours=1)
    return secrets.token_urlsafe(32), expiration


def authenticate_user(session, username: str, password: str):
    """Return user instance if credentials are valid and user is active."""
    from database.models import User

    user = session.query(User).filter(User.username == username).one_or_none()
    if not user or not user.is_active:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user


def set_new_password(session, user, new_password: str) -> None:
    user.password_hash = hash_password(new_password)
    user.reset_token = None
    user.reset_token_expiration = None
    session.add(user)
