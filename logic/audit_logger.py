"""Audit logging for traceability."""

from __future__ import annotations

from database.models import AuditLog


class AuditLogger:
    def __init__(self, session):
        self.session = session

    def log(self, *, user_id: int, action: str, table_name: str, record_id: int | None, details: str) -> None:
        self.session.add(
            AuditLog(
                user_id=user_id,
                action=action,
                table_name=table_name,
                record_id=record_id,
                details=details,
            )
        )

    def list_logs(self, requester_role: str):
        if requester_role != "Admin":
            raise PermissionError("Solo Admin puede acceder a auditoría")
        return self.session.query(AuditLog).order_by(AuditLog.created_at.desc()).all()
