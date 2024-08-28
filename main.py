from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from widgets import mainWidgets


app = QApplication([])

window = QWidget()
window.setFixedSize(429, 680)
window.setWindowTitle("Calculator")
window.setWindowIcon(QIcon("calc.png"))
window.setStyleSheet("""
    background-color: black;
    border: None;
""")


mainWidgets(window)

window.move(500, 100)

window.show()

app.exec_()
