"""Audit logs view window (Admin only)."""

from __future__ import annotations

from ui.qt_compat import QTableWidget, QVBoxLayout, QWidget, PYQT_AVAILABLE


class AuditViewWindow(QWidget):
    def __init__(self):
        if not PYQT_AVAILABLE:
            raise RuntimeError("PyQt5 no está instalado")
        super().__init__()
        self.setWindowTitle("Auditoría")
        layout = QVBoxLayout()
        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(["Fecha", "Usuario", "Acción", "Tabla", "Detalles"])
        layout.addWidget(self.table)
        self.setLayout(layout)
