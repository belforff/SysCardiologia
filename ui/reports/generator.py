"""Simple reports utility panel placeholder."""

from __future__ import annotations

from ui.qt_compat import QPushButton, QVBoxLayout, QWidget, PYQT_AVAILABLE


class ReportsWindow(QWidget):
    def __init__(self):
        if not PYQT_AVAILABLE:
            raise RuntimeError("PyQt5 no está instalado")
        super().__init__()
        self.setWindowTitle("Reportes")
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Generar ficha PDF"))
        layout.addWidget(QPushButton("Exportar pacientes Excel"))
        self.setLayout(layout)
