"""Application configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass

GENDER_OPTIONS: tuple[str, ...] = ("Masculino", "Femenino", "Otro", "M", "F")


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "SysCardiologia")
    app_env: str = os.getenv("APP_ENV", "development")
    secret_key: str = os.getenv("SECRET_KEY", "change-this-secret-in-production")
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:postgres@localhost:5432/syscardiologia",
    )
    session_timeout_minutes: int = int(os.getenv("SESSION_TIMEOUT_MINUTES", "30"))
    default_admin_username: str = os.getenv("DEFAULT_ADMIN_USERNAME", "admin")
    default_admin_password: str = os.getenv("DEFAULT_ADMIN_PASSWORD", "admin1234")


settings = Settings()
