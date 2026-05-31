# Author - Paarth Batra
# Base Version 2.0
# Using different logic for addition of text - No file handling . calculations on the fly

# GUI
# Version 2.0
# Addition of the About Me gui using a call to a About Module - 22nd August 2013 - About Me module /
# is now modal i.e. User can not do anything if this window is open

#22nd Aug 2013
# Version 2.1   - Changes :
#               Addition of setfocus on maine QlineEdit()
#Version 2.2        - To be finished
#23rd Aug 2013
#               Put SimulateBackspace in addStr and put all in CalculatorInputLogic module
#               Change QLineEdit to QLabel ---Add lineEdit and lineEditu logic in Simulatebackspace
#               Move CalculatorInputLogic in a different Class named CalculatorInputLogic

# Add Events for digit keys to call addTxt

#Version 2.5 - Change
#24th Aug 2013
# Move all code out of UI_Window class to a function in class calculator whic inherits Qt.MainWindow to get KeyPress events on label
# Done

#Version 2.7
#25th Aug 2013
#Using CalculatorInputLogic_v_2_1
#               put C-Clear All , CE-Clear Entry , <-- Backspace and other logics to CalculatorInputLogic


# Version 2.8 -
# 27th Aug 2013
# Use Calculator logic v 2_3 to use standalone  sqrt, 1/x functions , percentage

#This was  once prod version

#version 2.8.2
# Use of CalculatorInputLogic v2.7 fr support of ()

#version 2.8.3
# () can be inputted by keyboard
#use of CalculatorInputLogic v2.8

#version 2.8.4
#include of Show Expression function on button SE=

#Version 2.8.5 - GUI Changes
# make SE Button bigger     - done
#Add copy and paste options
#Add www.versionpb.com       - done

#version 2.9

# Compile with new about and Contents menu item

# version 3.0.0.0
# 29th June 2016
# Add Register Free Link
# Click on Contents should open Web Link
# Change Icon from my image to calculator Image

# import sip # SIP is generally not needed explicitly in PyQt6
import atexit
import functools
from PyQt6 import QtWidgets, QtGui, QtCore
import os
from About import *
from Contents import *
from CalculatorInputLogic import *
import webbrowser
# import win32clipboard as w # Removed dependency


class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()

        #Variables

        self.lineE = "0"
        self.lineEU = ""
        self.setlineE = "0"
        self.setlineEU = ""

        self.initUI()

    def keyPressEvent(self, qKeyEvent):
        print("hi")
        print(qKeyEvent.key())
        key = qKeyEvent.key()
        
        if key == QtCore.Qt.Key.Key_0:
            print("Key pressed 0")
            print(" it will call addTxt now i.e. ui.CallAddTxt(0)")
            self.CallAddTxt("0")
        if key == QtCore.Qt.Key.Key_1:
            print("Key pressed 1")
            print(" it will call addTxt now i.e. ui.CallAddTxt(1)")
            self.CallAddTxt("1")
        if key == QtCore.Qt.Key.Key_2:
            print("Key pressed 2")
            print(" it will call addTxt now i.e. ui.CallAddTxt(2)")
            self.CallAddTxt("2")
        if key == QtCore.Qt.Key.Key_3:
            print("Key pressed 3")
            self.CallAddTxt("3")
        if key == QtCore.Qt.Key.Key_4:
            print("Key pressed 4")
            self.CallAddTxt("4")
        if key == QtCore.Qt.Key.Key_5:
            print("Key pressed 5")
            self.CallAddTxt("5")
        if key == QtCore.Qt.Key.Key_6:
            print("Key pressed 6")
            self.CallAddTxt("6")
        if key == QtCore.Qt.Key.Key_7:
            print("Key pressed 7")
            self.CallAddTxt("7")
        if key == QtCore.Qt.Key.Key_8:
            print("Key pressed 8")
            self.CallAddTxt("8")
        if key == QtCore.Qt.Key.Key_9:
            print("Key pressed 9")
            self.CallAddTxt("9")
        if key == QtCore.Qt.Key.Key_Period:
            print("Key pressed .")
            self.CallAddTxt(".")
        if key == QtCore.Qt.Key.Key_Plus:
            print("Key pressed +")
            self.CallAddTxt("+")
        if key == QtCore.Qt.Key.Key_Minus:
            print("Key pressed -")
            self.CallAddTxt("-")
        if key == QtCore.Qt.Key.Key_Asterisk:
            print("Key pressed *")
            self.CallAddTxt("*")
        if key == QtCore.Qt.Key.Key_Slash:
            print("Key pressed /")
            self.CallAddTxt("/")
        if key == QtCore.Qt.Key.Key_Return:
            print('Enter pressed')
            self.CallAddTxt("=")
        if key == QtCore.Qt.Key.Key_Backspace :
            print('Enter pressed')
            self.CallAddTxt("backspace")
        if key == QtCore.Qt.Key.Key_Escape:
            self.CallAddTxt("C")
            print("Escape Key was pressed : Clearing all")
        if key == QtCore.Qt.Key.Key_Delete:
            self.CallAddTxt("CE")
            print("Delete Key was pressed : Clearing Entry")
        if key == QtCore.Qt.Key.Key_ParenLeft:
            print('Left Bracket pressed')
            self.CallAddTxt("(")
        if key == QtCore.Qt.Key.Key_ParenRight:
            print('Right Bracket pressed')
            self.CallAddTxt(")")
        if key == QtCore.Qt.Key.Key_AsciiCircum:
            print('^ (Power) pressed')
            self.CallAddTxt("^")


    def initUI(self):
        print("This is calculator version 3.0 .")

        self.setWindowTitle("Calculator")
        self.resize(263, 390)
        self.setFixedSize(263, 390)              # making the calculator resizable
        self.setWindowIcon(QtGui.QIcon('pkldll'))
        self.setAutoFillBackground(False)
        self.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(229, 239, 255);")

        centralWidget=QtWidgets.QWidget(self)
        centralWidget.show()
        self.setCentralWidget(centralWidget)

        font= QtGui.QFont("Comic Sans",10)
        font.setItalic(False)
        font.setBold(False)
        self.headerLabel= QtWidgets.QLabel(centralWidget)
        self.headerLabel.setGeometry(QtCore.QRect(0, 0, 261, 25))
        self.headerLabel.setText("www.versionpb.co.in")
        self.headerLabel.show()

        self.lineEditu = QtWidgets.QLabel(centralWidget)
        self.lineEditu.setGeometry(QtCore.QRect(0, 0, 261, 25))
        self.lineEditu.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditu.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.lineEditu.show()
        self.lineEditu.setFont(font)

        self.lineEdit = QtWidgets.QLabel(centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 20, 261, 50))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        font = QtGui.QFont("Comic Sans",20)
        font.setItalic(False)
        font.setBold(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("0")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)                    # Align Text in Line edit to the right
        self.lineEdit.setFocus()                                            #Setting Default focus on main line Edit
        self.lineEdit.show()

        pushButton_2 = QtWidgets.QPushButton(centralWidget)
        pushButton_2.setGeometry(QtCore.QRect(10, 70, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        # font.setWeight(75) # setWeight legacy
        font.setWeight(QtGui.QFont.Weight.Bold)
        pushButton_2.setFont(font)
        pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_2.setAutoFillBackground(False)
        pushButton_2.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_3 = QtWidgets.QPushButton(centralWidget)
        pushButton_3.setGeometry(QtCore.QRect(60, 70, 41, 31))
        pushButton_3.setFont(font)
        pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_3.setAutoFillBackground(False)
        pushButton_3.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_4 = QtWidgets.QPushButton(centralWidget)
        pushButton_4.setGeometry(QtCore.QRect(110, 70, 41, 31))
        pushButton_4.setFont(font)
        pushButton_4.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        #pushButton_6 = QtWidgets.QPushButton(centralWidget)
        #pushButton_6.setGeometry(QtCore.QRect(210, 70, 41, 31))
        #pushButton_6.setFont(font)
        #pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        #pushButton_6.setAutoFillBackground(False)
        #pushButton_6.setStyleSheet("background-color: rgb(192, 228, 255);\n"
#"\n"
#"")

        pushButton_7 = QtWidgets.QPushButton(centralWidget)
        pushButton_7.setGeometry(QtCore.QRect(160, 70, 91, 31))
        pushButton_7.setFont(font)
        pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_7.setAutoFillBackground(False)
        pushButton_7.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_8 = QtWidgets.QPushButton(centralWidget)
        pushButton_8.setGeometry(QtCore.QRect(110, 110, 41, 31))

        pushButton_8.setFont(font)
        pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_8.setAutoFillBackground(False)
        pushButton_8.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_9 = QtWidgets.QPushButton(centralWidget)
        pushButton_9.setGeometry(QtCore.QRect(60, 110, 41, 31))

        pushButton_9.setFont(font)
        pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_9.setAutoFillBackground(False)
        pushButton_9.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_10 = QtWidgets.QPushButton(centralWidget)
        pushButton_10.setGeometry(QtCore.QRect(160, 110, 41, 31))

        pushButton_10.setFont(font)
        pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_10.setAutoFillBackground(False)
        pushButton_10.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_11 = QtWidgets.QPushButton(centralWidget)
        pushButton_11.setGeometry(QtCore.QRect(10, 110, 41, 31))

        pushButton_11.setFont(font)
        pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_11.setAutoFillBackground(False)
        pushButton_11.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_12 = QtWidgets.QPushButton(centralWidget)
        pushButton_12.setGeometry(QtCore.QRect(210, 110, 41, 31))

        pushButton_12.setFont(font)
        pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_12.setAutoFillBackground(False)
        pushButton_12.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_13 = QtWidgets.QPushButton(centralWidget)
        pushButton_13.setGeometry(QtCore.QRect(110, 150, 41, 31))

        pushButton_13.setFont(font)
        pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_13.setAutoFillBackground(False)
        pushButton_13.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_14 = QtWidgets.QPushButton(centralWidget)
        pushButton_14.setGeometry(QtCore.QRect(60, 150, 41, 31))

        pushButton_14.setFont(font)
        pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_14.setAutoFillBackground(False)
        pushButton_14.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_15 = QtWidgets.QPushButton(centralWidget)
        pushButton_15.setGeometry(QtCore.QRect(160, 150, 41, 31))

        pushButton_15.setFont(font)
        pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_15.setAutoFillBackground(False)
        pushButton_15.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_16 = QtWidgets.QPushButton(centralWidget)
        pushButton_16.setGeometry(QtCore.QRect(10, 150, 41, 31))

        pushButton_16.setFont(font)
        pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_16.setAutoFillBackground(False)
        pushButton_16.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_17 = QtWidgets.QPushButton(centralWidget)
        pushButton_17.setGeometry(QtCore.QRect(210, 150, 41, 31))

        pushButton_17.setFont(font)
        pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_17.setAutoFillBackground(False)
        pushButton_17.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_18 = QtWidgets.QPushButton(centralWidget)
        pushButton_18.setGeometry(QtCore.QRect(110, 190, 41, 31))
        pushButton_18.setFont(font)
        pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_18.setAutoFillBackground(False)
        pushButton_18.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_19 = QtWidgets.QPushButton(centralWidget)
        pushButton_19.setGeometry(QtCore.QRect(60, 190, 41, 31))

        pushButton_19.setFont(font)
        pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_19.setAutoFillBackground(False)
        pushButton_19.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_20 = QtWidgets.QPushButton(centralWidget)
        pushButton_20.setGeometry(QtCore.QRect(160, 190, 41, 31))

        pushButton_20.setFont(font)
        pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_20.setAutoFillBackground(False)
        pushButton_20.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_21 = QtWidgets.QPushButton(centralWidget)
        pushButton_21.setGeometry(QtCore.QRect(10, 190, 41, 31))

        pushButton_21.setFont(font)
        pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_21.setAutoFillBackground(False)
        pushButton_21.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_22 = QtWidgets.QPushButton(centralWidget)
        pushButton_22.setGeometry(QtCore.QRect(210, 190, 41, 31))

        pushButton_22.setFont(font)
        pushButton_22.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_22.setAutoFillBackground(False)
        pushButton_22.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_23 = QtWidgets.QPushButton(centralWidget)
        pushButton_23.setGeometry(QtCore.QRect(110, 230, 41, 31))

        pushButton_23.setFont(font)
        pushButton_23.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_23.setAutoFillBackground(False)
        pushButton_23.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_24 = QtWidgets.QPushButton(centralWidget)
        pushButton_24.setGeometry(QtCore.QRect(60, 230, 41, 31))

        pushButton_24.setFont(font)
        pushButton_24.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_24.setAutoFillBackground(False)
        pushButton_24.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_25 = QtWidgets.QPushButton(centralWidget)
        pushButton_25.setGeometry(QtCore.QRect(160, 230, 41, 31))

        pushButton_25.setFont(font)
        pushButton_25.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_25.setAutoFillBackground(False)
        pushButton_25.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_26 = QtWidgets.QPushButton(centralWidget)
        pushButton_26.setGeometry(QtCore.QRect(10, 230, 41, 31))

        pushButton_26.setFont(font)
        pushButton_26.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_26.setAutoFillBackground(False)
        pushButton_26.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_27 = QtWidgets.QPushButton(centralWidget)
        pushButton_27.setGeometry(QtCore.QRect(210, 230, 41, 71))

        pushButton_27.setFont(font)
        pushButton_27.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_27.setAutoFillBackground(False)
        pushButton_27.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_28 = QtWidgets.QPushButton(centralWidget)
        pushButton_28.setGeometry(QtCore.QRect(110, 270, 41, 31))

        pushButton_28.setFont(font)
        pushButton_28.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_28.setAutoFillBackground(False)
        pushButton_28.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_30 = QtWidgets.QPushButton(centralWidget)
        pushButton_30.setGeometry(QtCore.QRect(160, 270, 41, 31))

        pushButton_30.setFont(font)
        pushButton_30.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_30.setAutoFillBackground(False)
        pushButton_30.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_31 = QtWidgets.QPushButton(centralWidget)
        pushButton_31.setGeometry(QtCore.QRect(10, 270, 91, 31))

        pushButton_31.setFont(font)
        pushButton_31.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        pushButton_31.setAutoFillBackground(False)
        pushButton_31.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        self.versionpbRegister= QtWidgets.QLabel(centralWidget)
        self.versionpbRegister.setText('<a href="http://www.versionpb.co.in/register-your-product/" >Register for Free !</a>')
        self.versionpbRegister.setGeometry(QtCore.QRect(5, 301, 120, 20))
        self.versionpbRegister.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.versionpbRegister.setOpenExternalLinks(True)
        self.versionpbRegister.show()
        # self.versionpbRegister.setMaximumHeight(15) 

        self.versionpb= QtWidgets.QLabel('<a href="http://www.versionpb.co.in">www.versionpb.co.in</a>',centralWidget)
        self.versionpb.setGeometry(QtCore.QRect(130, 301, 130, 20))
        self.versionpb.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.versionpb.setOpenExternalLinks(True) 
        self.versionpb.show()





        menuBar = QtWidgets.QMenuBar(self)
        menuBar.setGeometry(QtCore.QRect(0, 0, 263, 21))

        menuView = QtWidgets.QMenu(menuBar)
        menuView.show()
        menuEdit = QtWidgets.QMenu(menuBar)
        menuHelp = QtWidgets.QMenu(menuBar)


        self.setMenuBar(menuBar)
        statusBar = QtWidgets.QStatusBar(self)
        self.setStatusBar(statusBar)

        toolBar = QtWidgets.QToolBar(centralWidget)
        toolBar.setAcceptDrops(True)



        self.actionCopy = QtGui.QAction(centralWidget)
        self.actionCopy.setText("Copy")
        self.actionCopy.setShortcut('Ctrl+C')

        self.actionCopyE = QtGui.QAction(centralWidget)
        self.actionCopyE.setText("Copy-Expression")
        self.actionCopyE.setShortcut('Ctrl+E')

        self.actionPaste = QtGui.QAction(centralWidget)
        self.actionPaste.setText("Paste")
        self.actionPaste.setShortcut('Ctrl+V')

        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, toolBar)
        actionStandard = QtGui.QAction(centralWidget)
        actionAbout = QtGui.QAction(centralWidget)

        self.actionContents = QtGui.QAction(centralWidget)
        self.actionContents.setText("Contents")
        self.actionContents.setShortcut('F1')

        menuHelp.addAction(self.actionContents)
        menuHelp.addAction(actionAbout)
        menuView.addAction(actionStandard)
        menuEdit.addAction(self.actionCopy)
        menuEdit.addAction(self.actionCopyE)
        menuEdit.addAction(self.actionPaste)
        menuBar.addAction(menuView.menuAction())
        menuBar.addAction(menuEdit.menuAction())
        menuBar.addAction(menuHelp.menuAction())

        #Showing all objects
        self.show()
        pushButton_2.show()
        pushButton_3.show()
        pushButton_4.show()
        #pushButton_6.show()
        pushButton_7.show()
        pushButton_8.show()
        pushButton_9.show()
        pushButton_10.show()
        pushButton_11.show()
        pushButton_12.show()
        pushButton_13.show()
        pushButton_14.show()
        pushButton_15.show()
        pushButton_16.show()
        pushButton_17.show()
        pushButton_18.show()
        pushButton_19.show()
        pushButton_20.show()
        pushButton_21.show()
        pushButton_22.show()
        pushButton_23.show()
        pushButton_24.show()
        pushButton_25.show()
        pushButton_26.show()
        pushButton_27.show()
        pushButton_28.show()
        pushButton_30.show()
        pushButton_31.show()
        menuBar.show()

        #Setting Push Button names
        pushButton_2.setText("(")
        pushButton_3.setText(")")
        pushButton_4.setText("^")
        #pushButton_6.setText("M-")
        pushButton_7.setText("Expression =")
        pushButton_8.setText("C")
        pushButton_9.setText("CE")
        pushButton_10.setText("+-")
        pushButton_11.setText(u"\u21D0")        #Source http://www.alanwood.net/unicode/arrows.html
        pushButton_12.setText(u"\u221A")        #Squareroot Symbol : Source :http://www.fileformat.info/info/unicode/char/221a/index.htm
        pushButton_13.setText("9")
        pushButton_14.setText("8")
        pushButton_15.setText("/")
        pushButton_16.setText("7")
        pushButton_17.setText("%")
        pushButton_18.setText("6")
        pushButton_19.setText("5")
        pushButton_20.setText("*")
        pushButton_21.setText("4")
        pushButton_22.setText("1/x")
        pushButton_23.setText("3")
        pushButton_24.setText("2")
        pushButton_25.setText("-")
        pushButton_26.setText("1")
        pushButton_27.setText("=")
        pushButton_28.setText(".")
        pushButton_30.setText("+")
        pushButton_31.setText("0")



        menuView.setTitle( "View")
        menuEdit.setTitle("Edit")
        menuHelp.setTitle("help")
        toolBar.setWindowTitle("toolBar")
        actionStandard.setText("Standard")

        actionAbout.setText("About")

        #Signals
        # QtCore.QObject.connect(...) is old style. Use obj.signal.connect(...)
        pushButton_26.clicked.connect(lambda:self.CallAddTxt("1"))
        pushButton_24.clicked.connect(lambda:self.CallAddTxt("2"))
        pushButton_23.clicked.connect(lambda:self.CallAddTxt("3"))
        pushButton_21.clicked.connect(lambda:self.CallAddTxt("4"))
        pushButton_19.clicked.connect(lambda:self.CallAddTxt("5"))
        pushButton_18.clicked.connect(lambda:self.CallAddTxt("6"))
        pushButton_16.clicked.connect(lambda:self.CallAddTxt("7"))
        pushButton_14.clicked.connect(lambda:self.CallAddTxt("8"))
        pushButton_13.clicked.connect(lambda:self.CallAddTxt("9"))
        pushButton_31.clicked.connect(lambda:self.CallAddTxt("0"))
        pushButton_28.clicked.connect(lambda:self.CallAddTxt("."))
        pushButton_30.clicked.connect(lambda:self.CallAddTxt("+"))
        pushButton_25.clicked.connect(lambda:self.CallAddTxt("-"))
        pushButton_20.clicked.connect(lambda:self.CallAddTxt("*"))
        pushButton_15.clicked.connect(lambda:self.CallAddTxt("/"))
        pushButton_27.clicked.connect(lambda:self.CallAddTxt("="))
        pushButton_9.clicked.connect(lambda:self.CallAddTxt("CE"))
        pushButton_8.clicked.connect(lambda:self.CallAddTxt("C"))
        pushButton_11.clicked.connect(lambda:self.CallAddTxt("backspace"))
        pushButton_12.clicked.connect(lambda:self.CallAddTxt("sqrt"))
        pushButton_22.clicked.connect(lambda:self.CallAddTxt("Reci"))
        pushButton_10.clicked.connect(lambda:self.CallAddTxt("+-"))
        pushButton_17.clicked.connect(lambda:self.CallAddTxt("%"))
        pushButton_2.clicked.connect(lambda:self.CallAddTxt("("))
        pushButton_3.clicked.connect(lambda:self.CallAddTxt(")"))
        pushButton_4.clicked.connect(lambda:self.CallAddTxt("^"))
        pushButton_7.clicked.connect(lambda:CalculatorInputLogic().showExpression(self))

        self.actionCopy.triggered.connect(lambda: self.Copy())
        self.actionCopyE.triggered.connect(lambda: self.CopyE())
        self.actionPaste.triggered.connect(lambda: self.Paste())

        #Link activated connections removed as setOpenExternalLinks(True) handles them.
        # self.versionpb.linkActivated.connect(lambda:self.openurl())
        #About is a Class in About Module to show About us dialog
        actionAbout.triggered.connect(lambda: About())      #Putting action in the About menu Paarth 23rd Aug 2013
        self.actionContents.triggered.connect(lambda :self.openContents())
        # self.versionpbRegister.linkActivated.connect(lambda:self.openRegisterurl())

    def openContents(self):
        b = webbrowser
        b.open('http://www.versionpb.co.in/products/bodmas-calculator/bodmas-calculator-documentation/')

    def CallAddTxt(self,input):
        print("Values Passed are : input : ",input,"lineE : ",self.lineE,"lineEU : ",self.lineEU,"setlineE : ",self.setlineE,"setlineEU : ",self.setlineEU)
        CalculatorInputLogic().addTxt(self,input)
        print("Values After function are : input : ",input,"lineE : ",self.lineE,"lineEU : ",self.lineEU,"setlineE : ",self.setlineE,"setlineEU : ",self.setlineEU)
    
    # helper functions openRegisterurl and openurl Removed as they are no longer needed


    def Copy(self):
        """Copy current result (lower display) to clipboard."""
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.lineE)

    def CopyE(self):
        # command = 'echo ' + ui.lineEU + '| clip'
        # os.system(command)
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.lineEU)

    def Paste(self):
        #if ui.lineEdit.hasFocus():
        # w.OpenClipboard()
        # data = w.GetClipboardData()
        clipboard = QtWidgets.QApplication.clipboard()
        data = clipboard.text()
        
        print("Passing data as",data)
        try:
            v = CalculatorInputLogic().safe_eval(data)
            print(v)
            self.lineEdit.setText(data)
            self.lineE = data
        except Exception as E:
            print(E)
            print("Wrong data — only valid math expressions can be pasted")
        # w.CloseClipboard()
        #print txt

    def openurl(self):
        b = webbrowser
        b.open('http://www.versionpb.co.in')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui=Calculator()

    lineE = "0"
    lineEU = ""
    setlineE = "0"
    setlineEU = ""

    sys.exit(app.exec())
