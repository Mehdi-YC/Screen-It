from PyQt5 import QtWidgets, QtGui
from screenui import Ui_Screen_it
from sys import exit
from pyautogui import position


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Screen_it()
        self.ui.setupUi(self)
        self.ui.label.setScaledContents(True)
        self.setWindowIcon(QtGui.QIcon('icon.png'))

    def keyPressEvent(self, event):
        if self.ui.ready == 1:
            if event.text() == 's':
                self.ui.x1, self.ui.y1 = position()
                self.ui.end = 1

            if (event.text() == 'e') and (self.ui.end == 1):
                self.ui.x2, self.ui.y2 = position()
                self.ui.end = 0
                self.ui.ready = 0
                self.ui.startScrean(self.ui.x1, self.ui.x2,
                                    self.ui.y1, self.ui.y2)
                newindex = int(self.ui.IndexValue.text())+1
                self.ui.IndexValue.setText(str(newindex))
        if self.ui.ready == 2:
            if event.text() == 'a':
                self.hide()
                self.ui.fullshot()
                self.show()
                self.ui.ready = 0
        if self.ui.ready == 3:
            if event.text() == 'b':
                try:
                    self.ui.startScrean(self.ui.x1f, self.ui.x2f,
                                        self.ui.y1f, self.ui.y2f)
                    newindex = int(self.ui.IndexValue.text())+1
                    self.ui.IndexValue.setText(str(newindex))
                    self.ui.ready = 0
                except:
                    pass
        if self.ui.ready == 4:
            if event.text() == 's':
                self.ui.x1f, self.ui.y1f = position()
                self.ui.end = 1

            if (event.text() == 'e') and (self.ui.end == 1):
                self.ui.x2f, self.ui.y2f = position()
                self.ui.RegionScreenfixed.setEnabled(True)
                self.ui.end = 0
                self.ui.ready = 0


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    exit(app.exec_())
