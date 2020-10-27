from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from pyautogui import press, screenshot
from PIL import Image
from PIL.ImageQt import ImageQt
from math import fabs
from os import getcwd, remove, startfile
from subprocess import Popen


class Ui_Screen_it(object):
    def setupUi(self, Screen_it):
        self.fullpath = "none"
        self.ready = 0
        self.end = 0
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0
        self.x1f = 0
        self.y1f = 0
        self.x2f = 0
        self.y2f = 0
        Screen_it.setObjectName("Screen_it")
        Screen_it.setFixedSize(340, 411)
        self.centralwidget = QtWidgets.QWidget(Screen_it)
        self.centralwidget.setObjectName("centralwidget")
        self.RegionScreen = QtWidgets.QPushButton(self.centralwidget)
        self.RegionScreen.setGeometry(QtCore.QRect(20, 330, 49, 30))
        self.RegionScreen.setObjectName("RegionScreen")
        self.RegionScreenfixed = QtWidgets.QPushButton(self.centralwidget)
        self.RegionScreenfixed.setGeometry(QtCore.QRect(69, 330, 70, 30))
        self.RegionScreenfixed.setObjectName("RegionScreenFix")
        self.RegionScreenfixing = QtWidgets.QPushButton(self.centralwidget)
        self.RegionScreenfixing.setGeometry(QtCore.QRect(69, 361, 70, 20))
        self.RegionScreenfixing.setObjectName("RegionScreenFixing")
        self.Fullscreen = QtWidgets.QPushButton(self.centralwidget)
        self.Fullscreen.setGeometry(QtCore.QRect(143, 330, 90, 30))
        self.Fullscreen.setObjectName("Fullscreen")
        self.restartCounter = QtWidgets.QPushButton(self.centralwidget)
        self.restartCounter.setGeometry(QtCore.QRect(240, 110, 90, 30))
        self.restartCounter.setObjectName("restartCounter")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 80, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 80, 15))
        self.label_2.setObjectName("label_2")
        self.Namevalue = QtWidgets.QLineEdit(self.centralwidget)
        self.Namevalue.setGeometry(QtCore.QRect(102, 70, 210, 30))
        self.Namevalue.setObjectName("Namevalue")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(30, 160, 280, 150))
        self.image.setObjectName("image")
        self.RemoveLast = QtWidgets.QPushButton(self.centralwidget)
        self.RemoveLast.setGeometry(QtCore.QRect(240, 330, 90, 30))
        self.RemoveLast.setObjectName("RemoveLast")
        self.PathValue = QtWidgets.QLineEdit(self.centralwidget)
        self.PathValue.setGeometry(QtCore.QRect(100, 20, 130, 20))
        self.PathValue.setObjectName("PathValue")
        self.DirPath = QtWidgets.QPushButton(self.centralwidget)
        self.DirPath.setGeometry(QtCore.QRect(240, 20, 80, 30))
        self.DirPath.setObjectName("DirPath")
        self.IndexValue = QtWidgets.QLineEdit(self.centralwidget)
        self.IndexValue.setGeometry(QtCore.QRect(100, 120, 130, 20))
        self.IndexValue.setObjectName("IndexValue")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 45, 15))
        self.label_3.setObjectName("label_3")
        Screen_it.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Screen_it)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 20))
        self.menubar.setObjectName("menubar")
        Screen_it.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Screen_it)
        self.statusbar.setObjectName("statusbar")
        Screen_it.setStatusBar(self.statusbar)
        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setGeometry(QtCore.QRect(324, 172, 20, 130))
        self.Open.setText("")
        self.Open.setObjectName("Open")

        self.retranslateUi(Screen_it)
        QtCore.QMetaObject.connectSlotsByName(Screen_it)

    def retranslateUi(self, Screen_it):
        _translate = QtCore.QCoreApplication.translate
        Screen_it.setWindowTitle(_translate("Screen_it", "Screen it"))
        self.RegionScreen.setText(_translate("Screen_it", "Region "))
        self.RegionScreenfixed .setText(
            _translate("Screen_it", "Region fixed"))
        self.RegionScreenfixing .setText(
            _translate("Screen_it", "selcet region"))
        self.RegionScreenfixed.setEnabled(False)
        self.Fullscreen.setText(_translate("Screen_it", "Fullscreen"))
        self.restartCounter.setText(_translate("Screen_it", "Refresh Index"))
        self.label.setText(_translate("Screen_it", "Screen Name :"))
        self.label_2.setText(_translate("Screen_it", "Save to :"))
        self.image.setText(_translate("Screen_it", ""))
        self.RemoveLast.setText(_translate("Screen_it", "Remove last"))
        self.DirPath.setText(_translate("Screen_it", "Path"))
        self.label_3.setText(_translate("Screen_it", "Index :"))
        self.DirPath.clicked.connect(self.GetDir)
        self.PathValue.setEnabled(False)
        self.Namevalue.setText("Default")
        self.IndexValue.setText("1")
        self.PathValue.setText(getcwd())
        self.IndexValue.setEnabled(False)
        self.RegionScreen.clicked.connect(self.setstartScrean)
        self.RegionScreenfixed.clicked.connect(self.setRegionScreenfixed)
        self.RegionScreenfixing.clicked.connect(self.setRegionScreenfixing)
        self.restartCounter.clicked.connect(self.back2_0)
        self.Fullscreen.clicked.connect(self.setstartScreanFull)
        labImage = QPixmap("none.png")
        labImage2 = labImage.scaled(281, 140)
        self.image.setPixmap(labImage2)
        self.RemoveLast.clicked.connect(self.delete)
        self.Open.clicked.connect(self.open)

    def setstartScrean(self):
        try:
            imageName = str(self.Namevalue.text())[1]
            ind = int(self.IndexValue.text())-1+1
            path = str(self.PathValue.text())[1]
            self.ready = 1
        except:
            self.NoParamError()

    def setRegionScreenfixing(self):
        self.ready = 4

    def setRegionScreenfixed(self):
        try:
            imageName = str(self.Namevalue.text())[1]
            ind = int(self.IndexValue.text())-1+1
            path = str(self.PathValue.text())[1]
            self.ready = 3
            press('b')
        except:
            self.NoParamError()

    def setstartScreanFull(self):
        try:
            imageName = str(self.Namevalue.text())[1]
            ind = int(self.IndexValue.text())-1+1
            path = str(self.PathValue.text())[1]
            self.ready = 2
            press('a')
        except:
            self.NoParamError()

    def setregion(self):
        try:
            imageName = str(self.Namevalue.text())[1]
            ind = int(self.IndexValue.text())-1+1
            path = str(self.PathValue.text())[1]
            self.ready = 3
            press('b')
        except:
            self.NoParamError()

    def GetDir(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName = str(QFileDialog.getExistingDirectory())
        self.PathValue.setText(fileName)

    def max(self, x, y):
        if x > y:
            return x
        return y

    def min(self, x, y):
        if x > y:
            return y
        return x
    # Geting a character input value:

    def startScrean(self, x1, x2, y1, y2):
        h = fabs(y2-y1)
        w = fabs(x2-x1)
        x = min(x1, x2)
        y = min(y1, y2)
        # Printing the infos
        # print("(x,y) = ({},{})\t(w,h) = ({},{}) ".format(x, y, w, h))

        # Taking and saving the image
        imageName = str(self.Namevalue.text())
        ind = str(self.IndexValue.text())
        path = str(self.PathValue.text())

        # Staret the screenshot
        img = screenshot(region=(x, y, w, h))

        # Save the image
        self.fullpath = path+"/{}{}.png".format(imageName, ind)
        img.save(self.fullpath)

        # print it on the gui

        # im = Image.open(self.fullpath)
        # im = img.resize((281, 151), Image.ANTIALIAS)
        # qim = ImageQt(im)
        # pix = QtGui.QPixmap.fromImage(qim)

        labImage = QPixmap(self.fullpath)
        labImage2 = labImage.scaled(281, 151)
        self.image.setPixmap(labImage2)

    def back2_0(self):
        self.IndexValue.setText("1")

    def NoParamError(self):
        buttonReply = QMessageBox.question(
            self.centralwidget, 'Wrong parameters', "Check your values ", QMessageBox.Yes)

    def fullshot(self):

        imageName = str(self.Namevalue.text())
        ind = str(self.IndexValue.text())
        path = str(self.PathValue.text())

        # start the screenshot
        img = screenshot()

        # save the image
        self.fullpath = path+"/{}{}.png".format(imageName, ind)
        img.save(self.fullpath)

        # print it on the gui
        # im = Image.open(self.fullpath)
        # im = img.resize((281, 151), Image.ANTIALIAS)
        # qim = ImageQt(im)
        # pix = QtGui.QPixmap.fromImage(qim)
        labImage = QPixmap(self.fullpath)
        labImage2 = labImage.scaled(281, 151)
        self.image.setPixmap(labImage2)

        # Increment the index
        newindex = int(self.IndexValue.text())+1
        self.IndexValue.setText(str(newindex))

    def open(self):
        try:
            startfile(str(self.PathValue.text()))
        except:
            pass

    def delete(self):
        print("start deleting")
        try:
            imageName = str(self.Namevalue.text())
            ind = int(self.IndexValue.text())
            if ind-2 != 0:
                path = str(self.PathValue.text())
                lastpath = path+"/{}{}.png".format(imageName, ind-2)
                print(lastpath)
                remove(self.fullpath)
                self.fullpath = lastpath

                # decrement the index
                newindex = int(self.IndexValue.text())-1
                self.IndexValue.setText(str(newindex))
                labImage = QPixmap(self.fullpath)
                labImage2 = labImage.scaled(281, 151)
                self.image.setPixmap(labImage2)
            else:
                labImage = QPixmap("none.png")
                labImage2 = labImage.scaled(281, 151)
                self.image.setPixmap(labImage2)
        except:
            pass
