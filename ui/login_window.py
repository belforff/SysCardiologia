"""Secure login window."""

from __future__ import annotations

from ui.dialogs import error
from ui.qt_compat import (
    QFormLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    PYQT_AVAILABLE,
)


class LoginWindow(QWidget):
    def __init__(self, on_login):
        if not PYQT_AVAILABLE:
            raise RuntimeError("PyQt5 no está instalado")
        super().__init__()
        self.on_login = on_login

        self.setWindowTitle("SysCardiologia - Login")
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        login_btn = QPushButton("Ingresar")
        login_btn.clicked.connect(self._submit)

        form = QFormLayout()
        form.addRow("Usuario", self.username_input)
        form.addRow("Contraseña", self.password_input)

        root = QVBoxLayout()
        root.addLayout(form)
        root.addWidget(login_btn)
        self.setLayout(root)

    def _submit(self):
        username = self.username_input.text().strip()
        password = self.password_input.text()
        if not username or not password:
            error(self, "Login", "Ingrese usuario y contraseña")
            return
        self.on_login(username, password)
