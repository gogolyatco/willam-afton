from PyQt5.QtWidgets import (
    QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import*
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
app = QApplication([])
win = QWidget()

win.setStyleSheet("background-color:#ABDCFF; font-size:24px; padding: 5px")
win.resize(1200,700)
win.setWindowTitle("Easy Editor")

btn_dir = QPushButton("Папка")
btn_dir.setCursor(Qt.PointingHandCursor)
btn_dir.setStyleSheet("Border: 2pc solid #708899; border-pradius: 20px; background-color:white")
lw_files = QListWidget()

btn_left = QPushButton("Вліво")
btn_left.setCursor(Qt.PointingHandCursor)
btn_left.setStyleSheet("Border: 2pc solid #708899; border-pradius: 20px; background-color:white")

btn_right = QPushButton("Вправо")
btn_right.setCursor(Qt.PointingHandCursor)
btn_right.setStyleSheet("Border: 2pc solid #708899; border-pradius: 20px; background-color:white")

btn_flip = QPushButton("Відзеркалити")
btn_flip.setCursor(Qt.PointingHandCursor)
btn_flip.setStyleSheet("Border: 2pc solid #708899; border-pradius: 20px; background-color:white")

btn_sharp = QPushButton("Різкість")
btn_sharp.setCursor(Qt.PointingHandCursor)
btn_sharp.setStyleSheet("Border: 2pc solid #708899; border-pradius: 20px; background-color:white")

btn_bw = QPushButton("Ч\Б")
btn_bw.setCursor(Qt.PointingHandCursor)
btn_bw.setStyleSheet("Border: 2pc solid #708899; border-pradius: 20px; background-color:white")

lb_image = QLabel("Картинка")
row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col3 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image)
col3.addWidget(btn_left)
col3.addWidget(btn_right)
col3.addWidget(btn_flip)
col3.addWidget(btn_sharp)
col3.addWidget(btn_bw)
row.addLayout(col1, 20)
row.addLayout(col2, 60)
row.addLayout(col3, 20)
win.setLayout(row)
win.show()
app.exec()