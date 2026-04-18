"""Application themes and styles."""

LIGHT_THEME = """
QWidget { font-family: Segoe UI, Arial; font-size: 12px; }
QMainWindow { background: #f4f7fb; }
QPushButton { background: #1f6feb; color: white; border-radius: 4px; padding: 6px 10px; }
QPushButton:hover { background: #1558b0; }
"""

DARK_THEME = """
QWidget { font-family: Segoe UI, Arial; font-size: 12px; color: #f0f4ff; }
QMainWindow { background: #101621; }
QLineEdit, QTextEdit, QTableWidget { background: #172033; border: 1px solid #2a3650; }
QPushButton { background: #2f81f7; color: white; border-radius: 4px; padding: 6px 10px; }
QPushButton:hover { background: #1f6feb; }
"""
