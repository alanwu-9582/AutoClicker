import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from .app import MyApp

def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())