import sys
import webbrowser
from PyQt6.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt6.uic import loadUi

from Gui.main_window_ui import Ui_MainWindow
from Gui.make_config_dia import Ui_Dialog
url="https://realpython.com/qt-designer-python/"

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # self.
        self.setupUi(self)
        self.connectSignalsSlots()
        self.setWindowTitle('Dash board')
    def connectSignalsSlots(self):
        self.action_New_cofig.triggered.connect(self.New_config)
        self.actionDoc.triggered.connect(self.doc)
        # self.action_Exit.triggered.connect(self.close)
        # self.action_Find_Replace.triggered.connect(self.findAndReplace)
        # self.action_About.triggered.connect(self.about)
    def doc(self):
        webbrowser.open_new(url)
    def New_config(self):
        new = New_config(self)
        new.exec()


class New_config(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        #self.setupUi("Gui/config.ui")
        loadUi("Gui/config.ui",self)


class New_config_be(QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("Gui/config.ui", self)
        self.setWindowTitle("hallo")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
2