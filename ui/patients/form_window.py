"""Patient form window."""

from __future__ import annotations

from config import GENDER_OPTIONS
from ui.qt_compat import (
    QComboBox,
    QFormLayout,
    QLineEdit,
    QTextEdit,
    QVBoxLayout,
    QWidget,
    PYQT_AVAILABLE,
)


class PatientFormWindow(QWidget):
    def __init__(self):
        if not PYQT_AVAILABLE:
            raise RuntimeError("PyQt5 no está instalado")
        super().__init__()
        self.setWindowTitle("Formulario de paciente")
        form = QFormLayout()
        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.age = QLineEdit()
        self.gender = QComboBox()
        self.gender.addItems(list(GENDER_OPTIONS))
        self.phone = QLineEdit()
        self.email = QLineEdit()
        self.address = QLineEdit()
        self.symptoms = QTextEdit()
        self.diagnosis = QTextEdit()
        self.treatment_plan = QTextEdit()

        form.addRow("Nombre", self.first_name)
        form.addRow("Apellido", self.last_name)
        form.addRow("Edad", self.age)
        form.addRow("Género", self.gender)
        form.addRow("Teléfono", self.phone)
        form.addRow("Email", self.email)
        form.addRow("Dirección", self.address)
        form.addRow("Síntomas", self.symptoms)
        form.addRow("Diagnóstico", self.diagnosis)
        form.addRow("Plan tratamiento", self.treatment_plan)

        layout = QVBoxLayout()
        layout.addLayout(form)
        self.setLayout(layout)
