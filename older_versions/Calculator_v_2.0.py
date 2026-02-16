
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created: Thu Aug 15 13:33:16 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!




# Input logic - Paarth Batra
# Version 2.0
# Using different logic for addition of text - No file handling . calculations on the fly

# GUI
# Version 2.0
# Addition of the About Me gui using a call to a About Module - 22nd August 2013

from PyQt4 import QtCore, QtGui
import os
from About import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(263, 354)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(229, 239, 255);"))
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setAnimated(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))



        self.lineEditu = QtGui.QLineEdit(self.centralwidget)
        self.lineEditu.setGeometry(QtCore.QRect(0, 0, 261, 25))
        self.lineEditu.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEditu.setAlignment(QtCore.Qt.AlignRight)


        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 20, 261, 50))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))

        font= QtGui.QFont("Comic Sans",20)
        font.setItalic(False)
        font.setBold(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setText(_fromUtf8("0"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.lineEdit.setAlignment(QtCore.Qt.AlignRight)                    # Align Text in Line edit to the right


        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 70, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 70, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 70, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 70, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(160, 70, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(110, 110, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(60, 110, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(160, 110, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_11 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 110, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setAutoFillBackground(False)
        self.pushButton_11.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_12 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(210, 110, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setAutoFillBackground(False)
        self.pushButton_12.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_13 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(110, 150, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setAutoFillBackground(False)
        self.pushButton_13.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_14 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(60, 150, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setAutoFillBackground(False)
        self.pushButton_14.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_15 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(160, 150, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setAutoFillBackground(False)
        self.pushButton_15.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.pushButton_16 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(10, 150, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setAutoFillBackground(False)
        self.pushButton_16.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.pushButton_17 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(210, 150, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_17.setAutoFillBackground(False)
        self.pushButton_17.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.pushButton_18 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(110, 190, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_18.setAutoFillBackground(False)
        self.pushButton_18.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.pushButton_19 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(60, 190, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_19.setAutoFillBackground(False)
        self.pushButton_19.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.pushButton_20 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(160, 190, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_20.setAutoFillBackground(False)
        self.pushButton_20.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_20.setObjectName(_fromUtf8("pushButton_20"))
        self.pushButton_21 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(10, 190, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setAutoFillBackground(False)
        self.pushButton_21.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.pushButton_22 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(210, 190, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_22.setAutoFillBackground(False)
        self.pushButton_22.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_22.setObjectName(_fromUtf8("pushButton_22"))
        self.pushButton_23 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(110, 230, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_23.setAutoFillBackground(False)
        self.pushButton_23.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_23.setObjectName(_fromUtf8("pushButton_23"))
        self.pushButton_24 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(60, 230, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_24.setAutoFillBackground(False)
        self.pushButton_24.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_24.setObjectName(_fromUtf8("pushButton_24"))
        self.pushButton_25 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(160, 230, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_25.setAutoFillBackground(False)
        self.pushButton_25.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_25.setObjectName(_fromUtf8("pushButton_25"))
        self.pushButton_26 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(10, 230, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_26.setAutoFillBackground(False)
        self.pushButton_26.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_26.setObjectName(_fromUtf8("pushButton_26"))
        self.pushButton_27 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(210, 230, 41, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_27.setAutoFillBackground(False)
        self.pushButton_27.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_27.setObjectName(_fromUtf8("pushButton_27"))
        self.pushButton_28 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(110, 270, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_28.setAutoFillBackground(False)
        self.pushButton_28.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_28.setObjectName(_fromUtf8("pushButton_28"))
        self.pushButton_30 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(160, 270, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_30.setAutoFillBackground(False)
        self.pushButton_30.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_30.setObjectName(_fromUtf8("pushButton_30"))
        self.pushButton_31 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_31.setGeometry(QtCore.QRect(10, 270, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_31.setAutoFillBackground(False)
        self.pushButton_31.setStyleSheet(_fromUtf8("background-color: rgb(192, 228, 255);\n"
"\n"
""))
        self.pushButton_31.setObjectName(_fromUtf8("pushButton_31"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 263, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setAcceptDrops(True)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionStandard = QtGui.QAction(MainWindow)
        self.actionStandard.setObjectName(_fromUtf8("actionStandard"))
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        #self.actionAbout.triggered.connect(QtGui.qApp.quit)             #Putting action in the About menu Paarth 22nd Aug 2013
        self.actionAbout.triggered.connect(lambda:self.CallAboutUs())    # Calling About me window from class About





        self.menuHelp.addAction(self.actionAbout)

        self.menuView.addAction(self.actionStandard)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:ui.clearAll())
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")),lambda:ui.clearCE())
        QtCore.QObject.connect(self.pushButton_11, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.backspace)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Signals
        QtCore.QObject.connect(self.pushButton_26, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:ui.addTxt("1"))
        QtCore.QObject.connect(self.pushButton_24, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:ui.addTxt("2"))
        QtCore.QObject.connect(self.pushButton_23, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:ui.addTxt("3"))
        QtCore.QObject.connect(self.pushButton_21, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:ui.addTxt("4"))
        QtCore.QObject.connect(self.pushButton_19, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:ui.addTxt("5"))
        QtCore.QObject.connect(self.pushButton_18, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:ui.addTxt("6"))
        QtCore.QObject.connect(self.pushButton_16, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:ui.addTxt("7"))
        QtCore.QObject.connect(self.pushButton_14, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:ui.addTxt("8"))
        QtCore.QObject.connect(self.pushButton_13, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:ui.addTxt("9"))
        QtCore.QObject.connect(self.pushButton_31, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:ui.addTxt("0"))
        QtCore.QObject.connect(self.pushButton_28, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:ui.addTxt("."))
        QtCore.QObject.connect(self.pushButton_30, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:ui.addTxt("+"))
        QtCore.QObject.connect(self.pushButton_25, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:ui.addTxt("-"))
        QtCore.QObject.connect(self.pushButton_27, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:ui.addTxt("="))

        # for keyboard Enter key
        #QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.AddEntrypb)
    def CallAboutUs(self):
        CallAbout=About()

    def clearCE(self):
        ui.lineEdit.clear()
        ui.lineEdit.setText("0")
        ui.setlineE=0
        ui.lineE=0

    def clearAll(self):
        ui.lineEditu.clear()
        ui.lineEdit.clear()
        ui.lineEdit.setText("0")
        ui.lineE=0
        ui.lineEU=""
        ui.setlineE=0
        ui.setlineEU=""

    def findOperator(self,input):

        # This Function is created to find the Last operator present in the total string passed.
        #   This will be further called by calculateStrVal function to do the calculations

        # Introduced in CalculatorQt 2.0 on 18th Augu 2013
        # Author - Paarth
        plus=input.rfind("+")
        minus=input.rfind("-")
        multiply=input.rfind("*")
        divide=input.rfind("/")
        list=[plus,minus,multiply,divide]
        maxi=max(list)
        if maxi > -1 :
            print "Maximum is", maxi
            operator=input[maxi]
            print "operator is ",input[maxi]
            return operator



    def calculateStrVal(self,input):
    # This function will take the string anything example 2+3+5-45 , calculate the result and retrun result back to addTxt function
    # Introduced in CalculatorQt 2.0 on 18th Augu 2013
    # Author - Paarth

    #This will find the last operator in the string passed
        operator=ui.findOperator(input)
        print " Operator is ",operator

    #variable to find the last position of operator in the string passed
        temp=input.rfind(operator)

            #finding a as the value of last operator example a in 2+3+4-5 is -5
        a=input[temp:]
        print "A is ",a

            # find b checking if b is a single value or have operators in it

            #finding b as the value of last operator example b in 2+3+4-5 is 2+3+4
        b=input[:temp]
        print "B is ",b

            #If to see if b have any operators in it, if not above b was final b i.e. if string was 2+3 then b is 2 this is if condition
            #else if string was 2+3+1 where b is 2+3 we go to else
        if b.find("+") == -1 and b.find("-") == -1 and b.find("*") == -1 and b.find("/") == -1:
            print "A and B are :",a ,"  ",b
        else:
            print "As b contains operators passing b to calculateStrVal as ",b

                #Find b by passing b to same function . This is use of recursive function
            b=ui.calculateStrVal(b)


        print "B is ",b
            #creating variable result which gives result of a and b , so if we had 3-4 , a = -4 , b =3 then result is -4+3 i.e. -1.0
        result=str(float(a)+float(b))


        print "from CalculateStrVal : Result is ",result
            # dot will find the position of . in the result , so in -1.0 it will be 2
        dot=result.find(".")
        print "position  dot is ",dot

            #this will keep string after . so in -1.0 this will be 0
        strAfterDot=result[dot+1:]
        print "Value ater dot is ",strAfterDot

            #Check if result have anything more than 0 then send result else send value before .
        if int(strAfterDot) > 0:
            return result
        else:
            return result[:dot]


    def addTxt(self,input):



        # This function will take the string anything example 2 from Calculator GUI as input , Check what should be done with this input and perform action
        # Introduced in CalculatorQt 2.0 on 18th Augu 2013
        # Author - Paarth
        print "New Cycle : \n\n\n\n\n\n\n\n\n\n\n\n\n"
        print "Value entered is ",input
        print "From add Txt before setting : lineE and lineEu are ",self.lineE,self.lineEU
            #if for the very first input only
        if self.lineE == 0 and self.lineEU == "" and str(input) in ("1","2","3","4","5","6","7","8","9"):
            self.lineE=input
            self.lineEU=input
            self.setlineE=input
            self.setlineEU=""
            print "from if: value entered is ",input
        # elif 1 for a wrong input at the very first input
        elif self.lineE == 0 and self.lineEU == "" and str(input) in ("+","-","*","/",".","0"):
             print "from elif 1:Wrong input dear , Nothing changes"
        # Elif 2 for entering . twice
        elif self.lineE[-1:] in ("1","2","3","4","5","6","7","8","9","0",".") and self.lineEU[-1:] in ("1","2","3","4","5","6","7","8","9","0",".") and str(input) in (".") and self.lineE.find(".") != -1:
            print "from elif 2:Wrong input dear , Nothing changes"
        # Elif 3 for a second level entry for inputs except operators
        elif self.lineE[-1:] in ("1","2","3","4","5","6","7","8","9","0",".") and self.lineEU[-1:] in ("1","2","3","4","5","6","7","8","9","0",".") and str(input) in ("1","2","3","4","5","6","7","8","9","0",".") and self.setlineEU[-1:] == "":
            self.lineE=self.lineE+input
            self.lineEU=self.lineEU+input
            self.setlineE=self.lineE
            self.setlineEU=""
            print "from elif 3 : "
        #Elif 4 for a operator entry
        elif self.lineE[-1:] in ("1","2","3","4","5","6","7","8","9","0",".") and self.lineEU[-1:] in ("1","2","3","4","5","6","7","8","9","0",".") and  str(input) in ("+", "-","*","/") and self.setlineEU[-1:] == "":
            self.lineE=self.lineE
            self.lineEU=self.lineEU+input
            self.setlineE=self.lineE
            self.setlineEU=self.lineEU
            print "from elif 4 when input is operator: value entered is",input
        #Elif 5 for digit entry when last lineEU is operator
        elif self.lineE[-1:] in ("1","2","3","4","5","6","7","8","9","0") and self.lineEU[-1:] in ("+", "-","*","/") and  str(input) in ("1","2","3","4","5","6","7","8","9","0"):
            self.lineE=input
            self.lineEU=self.lineEU+input
            self.setlineE=self.lineE
            self.setlineEU=self.setlineEU
        #Elif 6 Digit entry when last in setLineEU in operator and last in lineEU is not operator and entry is digit
        elif self.lineE[-1:] in ("1","2","3","4","5","6","7","8","9","0",".") and self.lineEU[-1:] in ("1","2","3","4","5","6","7","8","9","0",".") and  str(input) in ("1","2","3","4","5","6","7","8","9","0",".") and self.setlineEU[-1:] in ("+", "-","*","/"):
            self.lineE=self.setlineE+input
            self.lineEU=self.lineEU+input
            self.setlineE=self.lineE
            self.setlineEU=self.setlineEU


        #Elif 7 when last in setLineEU is operator and last in lineEU is not operator and entry is operator
        elif self.lineE[-1:] in ("1","2","3","4","5","6","7","8","9","0",".") and self.lineEU[-1:] in ("1","2","3","4","5","6","7","8","9","0",".") and  str(input) in ("+", "-","*","/") and self.setlineEU[-1:] in ("+", "-","*","/"):
            print " Value which will be calculated for lineE is ",self.lineEU
            StrToPass=self.lineEU
            print " Passing string to calculateStrVal",StrToPass
            re=ui.calculateStrVal(StrToPass)

            self.lineE=re
            self.lineEU=self.lineEU+input
            self.setlineE=self.lineE
            self.setlineEU=self.lineEU
            print "from elif 7 when last in setLineEU is operator and last in lineEU is not operator and entry is operator value entered is",input
        #Elif 8 when operator entered is =
        elif str(input) == "=":
            StrToPass=self.setlineEU+self.setlineE
            print " Passing string to calculateStrVal",StrToPass
            re=ui.calculateStrVal(StrToPass)

            self.lineE=re
            self.lineEU=""
            self.setlineE=self.lineE
            self.setlineEU=self.lineEU
            print "from elif 8 where passed input is ="
        #Elif 9 , anything after = was pressed , almost same as first time entry
        elif self.lineE[-1:] in ("1","2","3","4","5","6","7","8","9","0") and self.lineEU == "" and str(input) in ("1","2","3","4","5","6","7","8","9"):
            self.lineEU=self.lineE+"+"+input
            self.lineE=input
            self.setlineE=input
            self.setlineEU=self.lineEU
            print "from elif 9: value entered is ",input
        #Elif 10 , anything after = was pressed , almost same as first time entry
        elif self.lineE[-1:] in ("1","2","3","4","5","6","7","8","9","0") and self.lineEU == "" and  str(input) in ("+", "-","*","/") and self.setlineEU[-1:] == "":
            self.lineE=self.lineE
            self.lineEU=self.lineE+input
            self.setlineE=self.lineE
            self.setlineEU=self.lineEU
            print "from elif 10 when input is operator: anything after =",input

        else:
            print "From Else: value entered is",input

        print "From add Txt after setting : lineE and lineEu are ",self.lineE,self.lineEU
        self.lineEdit.setText(self.setlineE)
        self.lineEditu.setText(self.setlineEU)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator", None))
        self.pushButton_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_2.setText(_translate("MainWindow", "MC", None))
        self.pushButton_3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_3.setText(_translate("MainWindow", "MR", None))
        self.pushButton_4.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_4.setText(_translate("MainWindow", "MS", None))
        self.pushButton_6.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_6.setText(_translate("MainWindow", "M-", None))
        self.pushButton_7.setWhatsThis(_translate("Main Window", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_7.setText(_translate("MainWindow", "M+", None))
        self.pushButton_8.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_8.setText(_translate("MainWindow", "C", None))
        self.pushButton_9.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_9.setText(_translate("MainWindow", "CE", None))
        self.pushButton_10.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_10.setText(_translate("MainWindow", "+-", None))
        self.pushButton_11.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_11.setText(_translate("MainWindow", "<--", None))
        self.pushButton_12.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_12.setText(_translate("MainWindow", "/", None))
        self.pushButton_13.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_13.setText(_translate("MainWindow", "9", None))
        self.pushButton_14.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_14.setText(_translate("MainWindow", "8", None))
        self.pushButton_15.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_15.setText(_translate("MainWindow", "/", None))
        self.pushButton_16.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_16.setText(_translate("MainWindow", "7", None))
        self.pushButton_17.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_17.setText(_translate("MainWindow", "%", None))
        self.pushButton_18.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_18.setText(_translate("MainWindow", "6", None))
        self.pushButton_19.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_19.setText(_translate("MainWindow", "5", None))
        self.pushButton_20.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_20.setText(_translate("MainWindow", "*", None))
        self.pushButton_21.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_21.setText(_translate("MainWindow", "4", None))
        self.pushButton_22.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_22.setText(_translate("MainWindow", "1/x", None))
        self.pushButton_23.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_23.setText(_translate("MainWindow", "3", None))
        self.pushButton_24.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_24.setText(_translate("MainWindow", "2", None))
        self.pushButton_25.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_25.setText(_translate("MainWindow", "-", None))
        self.pushButton_26.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.pushButton_26.setText(_translate("MainWindow", "1", None))
        self.pushButton_27.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_27.setText(_translate("MainWindow", "=", None))
        self.pushButton_28.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_28.setText(_translate("MainWindow", ".", None))
        self.pushButton_30.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_30.setText(_translate("MainWindow", "+", None))
        self.pushButton_31.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400;\">555</span></p></body></html>", None))
        self.pushButton_31.setText(_translate("MainWindow", "0", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuHelp.setTitle(_translate("MainWindow", "help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionStandard.setText(_translate("MainWindow", "Standard", None))
        self.actionCopy.setText(_translate("MainWindow", "Copy", None))
        self.actionPaste.setText(_translate("MainWindow", "Paste", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()

    ui.lineE=0
    ui.lineEU=""
    ui.setlineE=0
    ui.setlineEU=""

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

