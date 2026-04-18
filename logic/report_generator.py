"""Professional report generation (PDF / Excel)."""

from __future__ import annotations

from pathlib import Path


class ReportGenerator:
    def __init__(self, output_dir: str = "reports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _patient_summary_lines(self, patient) -> list[str]:
        return [
            "FICHA MÉDICA - SYSCARDIOLOGIA",
            f"Paciente: {patient.first_name} {patient.last_name}",
            f"Edad: {patient.age} | Género: {patient.gender}",
            f"Diagnóstico: {patient.diagnosis or 'N/A'}",
            f"PA: {patient.blood_pressure or 'N/A'} | FC: {patient.heart_rate or 'N/A'}",
            f"Plan de tratamiento: {patient.treatment_plan or 'N/A'}",
        ]

    def generate_patient_pdf(self, patient, filename: str | None = None) -> Path:
        filename = filename or f"ficha_paciente_{patient.id}.pdf"
        path = self.output_dir / filename

        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.pdfgen import canvas
        except ImportError as exc:
            raise RuntimeError("Instale reportlab para generar PDF") from exc

        pdf = canvas.Canvas(str(path), pagesize=A4)
        y = 800
        for line in self._patient_summary_lines(patient):
            pdf.drawString(40, y, line)
            y -= 20
        pdf.save()
        return path

    def export_patients_excel(self, patients: list, filename: str = "pacientes.xlsx") -> Path:
        path = self.output_dir / filename
        try:
            from openpyxl import Workbook
        except ImportError as exc:
            raise RuntimeError("Instale openpyxl para exportar Excel") from exc

        wb = Workbook()
        ws = wb.active
        ws.title = "Pacientes"
        ws.append(["ID", "Nombre", "Edad", "Género", "Diagnóstico", "Estado"])
        for p in patients:
            ws.append([p.id, f"{p.first_name} {p.last_name}", p.age, p.gender, p.diagnosis, str(p.status)])
        wb.save(path)
        return path
