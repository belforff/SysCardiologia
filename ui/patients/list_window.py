"""Patient list window with search and filtering."""

from __future__ import annotations

from ui.qt_compat import QLineEdit, QTableWidget, QVBoxLayout, QWidget, PYQT_AVAILABLE


class PatientListWindow(QWidget):
    def __init__(self):
        if not PYQT_AVAILABLE:
            raise RuntimeError("PyQt5 no está instalado")
        super().__init__()
        self.setWindowTitle("Pacientes")
        layout = QVBoxLayout()
        self.search = QLineEdit()
        self.search.setPlaceholderText("Buscar por nombre o diagnóstico")
        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Edad", "Género", "Diagnóstico", "Estado"])
        layout.addWidget(self.search)
        layout.addWidget(self.table)
        self.setLayout(layout)
