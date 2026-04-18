"""Patient business logic layer."""

from __future__ import annotations

from sqlalchemy import or_

from database.models import Patient, PatientStatus
from logic.validators import validate_patient_payload


class PatientManager:
    def __init__(self, session, audit_logger=None):
        self.session = session
        self.audit_logger = audit_logger

    def create_patient(self, actor_id: int, payload: dict) -> Patient:
        validated = validate_patient_payload(payload)
        patient = Patient(**validated)
        self.session.add(patient)
        self.session.flush()
        if self.audit_logger:
            self.audit_logger.log(
                user_id=actor_id,
                action="CREATE",
                table_name="patients",
                record_id=patient.id,
                details=f"Paciente creado: {patient.first_name} {patient.last_name}",
            )
        return patient

    def update_patient(self, actor_id: int, patient_id: int, payload: dict) -> Patient:
        patient = self.get_patient(patient_id)
        validated = validate_patient_payload({**patient.__dict__, **payload})
        for key, value in validated.items():
            if hasattr(patient, key):
                setattr(patient, key, value)
        self.session.add(patient)
        if self.audit_logger:
            self.audit_logger.log(
                user_id=actor_id,
                action="UPDATE",
                table_name="patients",
                record_id=patient.id,
                details="Paciente actualizado",
            )
        return patient

    def soft_delete_patient(self, actor_id: int, patient_id: int) -> None:
        patient = self.get_patient(patient_id)
        patient.is_deleted = True
        patient.status = PatientStatus.INACTIVO
        self.session.add(patient)
        if self.audit_logger:
            self.audit_logger.log(
                user_id=actor_id,
                action="DELETE",
                table_name="patients",
                record_id=patient.id,
                details="Eliminación lógica de paciente",
            )

    def get_patient(self, patient_id: int) -> Patient:
        patient = (
            self.session.query(Patient)
            .filter(Patient.id == patient_id, Patient.is_deleted.is_(False))
            .one_or_none()
        )
        if not patient:
            raise ValueError("Paciente no encontrado")
        return patient

    def search_patients(self, query: str = "", status: PatientStatus | None = None):
        q = self.session.query(Patient).filter(Patient.is_deleted.is_(False))
        if query:
            like = f"%{query}%"
            q = q.filter(
                or_(
                    Patient.first_name.ilike(like),
                    Patient.last_name.ilike(like),
                    Patient.diagnosis.ilike(like),
                )
            )
        if status:
            q = q.filter(Patient.status == status)
        return q.order_by(Patient.last_name.asc(), Patient.first_name.asc()).all()
