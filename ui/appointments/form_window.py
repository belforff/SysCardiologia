"""Appointment form window."""

from __future__ import annotations

from ui.qt_compat import QDateTimeEdit, QFormLayout, QLineEdit, QVBoxLayout, QWidget, PYQT_AVAILABLE


class AppointmentFormWindow(QWidget):
    def __init__(self):
        if not PYQT_AVAILABLE:
            raise RuntimeError("PyQt5 no está instalado")
        super().__init__()
        self.setWindowTitle("Programar cita")
        form = QFormLayout()
        self.patient_id = QLineEdit()
        self.reason = QLineEdit()
        self.datetime = QDateTimeEdit()
        form.addRow("ID Paciente", self.patient_id)
        form.addRow("Motivo", self.reason)
        form.addRow("Fecha/Hora", self.datetime)

        layout = QVBoxLayout()
        layout.addLayout(form)
        self.setLayout(layout)
