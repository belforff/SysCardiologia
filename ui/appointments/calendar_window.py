"""Appointments calendar window."""

from __future__ import annotations

from ui.qt_compat import QTableWidget, QVBoxLayout, QWidget, PYQT_AVAILABLE


class AppointmentCalendarWindow(QWidget):
    def __init__(self):
        if not PYQT_AVAILABLE:
            raise RuntimeError("PyQt5 no está instalado")
        super().__init__()
        self.setWindowTitle("Calendario de citas")
        layout = QVBoxLayout()
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["Fecha", "Paciente", "Motivo", "Estado"])
        layout.addWidget(self.table)
        self.setLayout(layout)
