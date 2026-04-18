"""Users management window (Admin only)."""

from __future__ import annotations

from ui.qt_compat import QTableWidget, QVBoxLayout, QWidget, PYQT_AVAILABLE


class UsersWindow(QWidget):
    def __init__(self):
        if not PYQT_AVAILABLE:
            raise RuntimeError("PyQt5 no está instalado")
        super().__init__()
        self.setWindowTitle("Gestión de usuarios")
        layout = QVBoxLayout()
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["Usuario", "Nombre", "Rol", "Activo"])
        layout.addWidget(self.table)
        self.setLayout(layout)
