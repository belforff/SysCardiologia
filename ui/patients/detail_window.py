"""Patient detail window."""

from __future__ import annotations

from ui.qt_compat import QTextEdit, QVBoxLayout, QWidget, PYQT_AVAILABLE


class PatientDetailWindow(QWidget):
    def __init__(self):
        if not PYQT_AVAILABLE:
            raise RuntimeError("PyQt5 no está instalado")
        super().__init__()
        self.setWindowTitle("Detalle de paciente")
        layout = QVBoxLayout()
        self.content = QTextEdit()
        self.content.setReadOnly(True)
        layout.addWidget(self.content)
        self.setLayout(layout)
