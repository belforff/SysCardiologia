"""Main dashboard window."""

from __future__ import annotations

from ui.qt_compat import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, PYQT_AVAILABLE


class MainWindow(QMainWindow):
    def __init__(self, user):
        if not PYQT_AVAILABLE:
            raise RuntimeError("PyQt5 no está instalado")
        super().__init__()
        self.user = user
        self.setWindowTitle("SysCardiologia - Dashboard")

        central = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Bienvenido/a, {user.full_name} ({user.role.name})"))

        layout.addWidget(QPushButton("Pacientes"))
        layout.addWidget(QPushButton("Citas"))
        layout.addWidget(QPushButton("Reportes"))
        if user.role.name == "Admin":
            layout.addWidget(QPushButton("Auditoría"))
            layout.addWidget(QPushButton("Usuarios"))

        central.setLayout(layout)
        self.setCentralWidget(central)
