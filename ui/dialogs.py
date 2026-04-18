"""Common dialogs."""

from __future__ import annotations

from ui.qt_compat import QMessageBox, PYQT_AVAILABLE


def info(parent, title: str, message: str) -> None:
    if not PYQT_AVAILABLE:
        return
    QMessageBox.information(parent, title, message)


def error(parent, title: str, message: str) -> None:
    if not PYQT_AVAILABLE:
        return
    QMessageBox.critical(parent, title, message)
