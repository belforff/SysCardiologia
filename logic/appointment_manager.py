"""Appointment management logic."""

from __future__ import annotations

from datetime import datetime

from database.models import Appointment, Patient


class AppointmentManager:
    def __init__(self, session, audit_logger=None):
        self.session = session
        self.audit_logger = audit_logger

    def schedule_appointment(self, actor_id: int, patient_id: int, when: datetime, reason: str = "") -> Appointment:
        patient = self.session.query(Patient).filter(Patient.id == patient_id, Patient.is_deleted.is_(False)).one_or_none()
        if not patient:
            raise ValueError("Paciente no encontrado")

        appointment = Appointment(patient_id=patient_id, scheduled_for=when, reason=reason)
        self.session.add(appointment)
        self.session.flush()

        patient.next_appointment_date = when.date()
        self.session.add(patient)

        if self.audit_logger:
            self.audit_logger.log(
                user_id=actor_id,
                action="CREATE",
                table_name="appointments",
                record_id=appointment.id,
                details="Cita programada",
            )
        return appointment

    def list_calendar(self, start: datetime, end: datetime):
        return (
            self.session.query(Appointment)
            .filter(Appointment.scheduled_for >= start, Appointment.scheduled_for <= end)
            .order_by(Appointment.scheduled_for.asc())
            .all()
        )
