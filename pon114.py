from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QHBoxLayout

app = QApplication([])

window = QWidget()
window.resize(500,500)

lbl = QLabel("Вікторина")
main_line = QHBoxLayout()
main_line.addWidget(lbl)

window.setLayout(main_line)

window.show()
app.exec()

