"""Entry point for SysCardiologia desktop app."""

from __future__ import annotations

import sys

from ui.qt_compat import QApplication, PYQT_AVAILABLE
from ui.styles import LIGHT_THEME


class AppController:
    def __init__(self, session_factory, login_window_cls, main_window_cls, error_dialog):
        self.session = session_factory()
        self.login_window = login_window_cls(self.handle_login)
        self.main_window = None
        self.main_window_cls = main_window_cls
        self.error_dialog = error_dialog

    def handle_login(self, username: str, password: str) -> None:
        from logic.auth import authenticate_user

        user = authenticate_user(self.session, username, password)
        if not user:
            self.error_dialog(self.login_window, "Acceso denegado", "Credenciales inválidas")
            return

        self.main_window = self.main_window_cls(user)
        self.main_window.show()
        self.login_window.hide()


def main() -> int:
    if not PYQT_AVAILABLE:
        print("PyQt5 no está instalado. Ejecute: pip install -r requirements.txt")
        return 1

    from database.connection import SessionLocal, create_db_and_seed_defaults
    from ui.dialogs import error
    from ui.login_window import LoginWindow
    from ui.main_window import MainWindow

    create_db_and_seed_defaults()

    app = QApplication(sys.argv)
    app.setStyleSheet(LIGHT_THEME)
    controller = AppController(SessionLocal, LoginWindow, MainWindow, error)
    controller.login_window.show()
    return app.exec_()


if __name__ == "__main__":
    raise SystemExit(main())
