from PyQt6.QtWidgets import QMainWindow, QApplication,QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout

import sys
import sqlite3 as sql

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):

        super(MainWindow, self).__init__(*args, **kwargs)

        container = QWidget()
        containerLayout = QVBoxLayout()
        container.setLayout(containerLayout)

        self.setCentralWidget(container)




        self.DB = sql.connect(
            "Navtime.db"
        )
        self.cur = self.DB.cursor()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())