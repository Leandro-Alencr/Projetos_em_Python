# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 201)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BotaoInstalar = QtWidgets.QPushButton(self.centralwidget)
        self.BotaoInstalar.setGeometry(QtCore.QRect(0, 0, 571, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.BotaoInstalar.setFont(font)
        self.BotaoInstalar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotaoInstalar.setStyleSheet("QPushButton{\n"
"background-color: rgb(50, 200, 50);\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius: 15px;\n"
"border-color: black\n"
"}")
        self.BotaoInstalar.setObjectName("BotaoInstalar")
        self.BotaoStatus = QtWidgets.QLabel(self.centralwidget)
        self.BotaoStatus.setGeometry(QtCore.QRect(0, 80, 571, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BotaoStatus.setFont(font)
        self.BotaoStatus.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.BotaoStatus.setFrameShape(QtWidgets.QFrame.Panel)
        self.BotaoStatus.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.BotaoStatus.setText("")
        self.BotaoStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.BotaoStatus.setObjectName("BotaoStatus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reinstalador do TeamViewer"))
        self.BotaoInstalar.setText(_translate("MainWindow", "INSTALAR O TEAM VIEWER 13"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
