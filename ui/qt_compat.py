"""Compatibility wrappers for optional PyQt5 import."""

from __future__ import annotations

try:
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import (
        QApplication,
        QComboBox,
        QDateTimeEdit,
        QFormLayout,
        QHBoxLayout,
        QLabel,
        QLineEdit,
        QListWidget,
        QMainWindow,
        QMessageBox,
        QPushButton,
        QTableWidget,
        QTableWidgetItem,
        QTextEdit,
        QVBoxLayout,
        QWidget,
    )
    PYQT_AVAILABLE = True
except ImportError:  # pragma: no cover
    Qt = object
    QApplication = QComboBox = QDateTimeEdit = QFormLayout = QHBoxLayout = QLabel = QLineEdit = QListWidget = object
    QMainWindow = QMessageBox = QPushButton = QTableWidget = QTableWidgetItem = QTextEdit = QVBoxLayout = QWidget = object
    PYQT_AVAILABLE = False


__all__ = [
    "PYQT_AVAILABLE",
    "Qt",
    "QApplication",
    "QComboBox",
    "QDateTimeEdit",
    "QFormLayout",
    "QHBoxLayout",
    "QLabel",
    "QLineEdit",
    "QListWidget",
    "QMainWindow",
    "QMessageBox",
    "QPushButton",
    "QTableWidget",
    "QTableWidgetItem",
    "QTextEdit",
    "QVBoxLayout",
    "QWidget",
]
