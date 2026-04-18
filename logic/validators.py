"""Input validators for forms and APIs."""

from __future__ import annotations

import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
PHONE_RE = re.compile(r"^[+\d][\d\s()-]{6,}$")
BP_RE = re.compile(r"^\d{2,3}/\d{2,3}$")


def _require(value: str, field_name: str) -> str:
    cleaned = (value or "").strip()
    if not cleaned:
        raise ValueError(f"{field_name} es obligatorio")
    return cleaned


def validate_email(email: str | None) -> str | None:
    if email is None or not str(email).strip():
        return None
    email = email.strip()
    if not EMAIL_RE.match(email):
        raise ValueError("Correo electrónico inválido")
    return email


def validate_phone(phone: str | None) -> str | None:
    if phone is None or not str(phone).strip():
        return None
    phone = phone.strip()
    if not PHONE_RE.match(phone):
        raise ValueError("Teléfono inválido")
    return phone


def validate_blood_pressure(value: str | None) -> str | None:
    if value is None or not str(value).strip():
        return None
    value = value.strip()
    if not BP_RE.match(value):
        raise ValueError("Presión arterial inválida. Use formato SYS/DIA")
    return value


def validate_patient_payload(payload: dict) -> dict:
    first_name = _require(payload.get("first_name", ""), "Nombre")
    last_name = _require(payload.get("last_name", ""), "Apellido")

    age = int(payload.get("age", 0))
    if age <= 0 or age > 120:
        raise ValueError("Edad inválida")

    gender = _require(payload.get("gender", ""), "Género")

    weight = payload.get("weight_kg")
    height = payload.get("height_m")
    bmi = None
    if weight and height:
        weight_v = float(weight)
        height_v = float(height)
        if height_v <= 0:
            raise ValueError("Talla inválida")
        bmi = round(weight_v / (height_v * height_v), 2)

    return {
        **payload,
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "gender": gender,
        "email": validate_email(payload.get("email")),
        "phone": validate_phone(payload.get("phone")),
        "blood_pressure": validate_blood_pressure(payload.get("blood_pressure")),
        "bmi": bmi if bmi is not None else payload.get("bmi"),
    }
