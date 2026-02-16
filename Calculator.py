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

import sip
import atexit
import functools
import PyQt4
import os
from About import *
from Contents import *
from CalculatorInputLogic import *
import webbrowser
import win32clipboard as w


class Calculator(QtGui.QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()

        #Variables

        self.lineE = "0"
        self.lineEU = ""
        self.setlineE = "0"
        self.setlineEU = ""

        self.initUI()

    def keyPressEvent(self, qKeyEvent):
        print "hi"
        print(qKeyEvent.key())
        if qKeyEvent.key() == QtCore.Qt.Key_0:
            print "Key pressed 0"
            print " it will call addTxt now i.e. ui.CallAddTxt(0)"
            ui.CallAddTxt("0")
        if qKeyEvent.key() == QtCore.Qt.Key_1:
            print "Key pressed 1"
            print " it will call addTxt now i.e. ui.CallAddTxt(1)"
            ui.CallAddTxt("1")
        if qKeyEvent.key() == QtCore.Qt.Key_2:
            print "Key pressed 2"
            print " it will call addTxt now i.e. ui.CallAddTxt(2)"
            ui.CallAddTxt("2")
        if qKeyEvent.key() == QtCore.Qt.Key_3:
            print "Key pressed 3"
            ui.CallAddTxt("3")
        if qKeyEvent.key() == QtCore.Qt.Key_4:
            print "Key pressed 4"
            ui.CallAddTxt("4")
        if qKeyEvent.key() == QtCore.Qt.Key_5:
            print "Key pressed 5"
            ui.CallAddTxt("5")
        if qKeyEvent.key() == QtCore.Qt.Key_6:
            print "Key pressed 6"
            ui.CallAddTxt("6")
        if qKeyEvent.key() == QtCore.Qt.Key_7:
            print "Key pressed 7"
            ui.CallAddTxt("7")
        if qKeyEvent.key() == QtCore.Qt.Key_8:
            print "Key pressed 8"
            ui.CallAddTxt("8")
        if qKeyEvent.key() == QtCore.Qt.Key_9:
            print "Key pressed 9"
            ui.CallAddTxt("9")
        if qKeyEvent.key() == QtCore.Qt.Key_Period:
            print "Key pressed ."
            ui.CallAddTxt(".")
        if qKeyEvent.key() == QtCore.Qt.Key_Plus:
            print "Key pressed +"
            ui.CallAddTxt("+")
        if qKeyEvent.key() == QtCore.Qt.Key_Minus:
            print "Key pressed -"
            ui.CallAddTxt("-")
        if qKeyEvent.key() == QtCore.Qt.Key_Asterisk:
            print "Key pressed *"
            ui.CallAddTxt("*")
        if qKeyEvent.key() == QtCore.Qt.Key_Slash:
            print "Key pressed /"
            ui.CallAddTxt("/")
        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            print('Enter pressed')
            ui.CallAddTxt("=")
        if qKeyEvent.key() == QtCore.Qt.Key_Backspace :
            print('Enter pressed')
            ui.CallAddTxt("backspace")
        if qKeyEvent.key() == QtCore.Qt.Key_Escape:
            ui.CallAddTxt("C")
            print ("Escape Key was pressed : Clearing all")
        if qKeyEvent.key() == QtCore.Qt.Key_Delete:
            ui.CallAddTxt("CE")
            print ("Delete Key was pressed : Clearing Entry")
        if qKeyEvent.key() == QtCore.Qt.Key_ParenLeft:
            print('Left Bracket pressed')
            ui.CallAddTxt("(")
        if qKeyEvent.key() == QtCore.Qt.Key_ParenRight:
            print('Left Bracket pressed')
            ui.CallAddTxt(")")


    def initUI(self):
        print "This is calculator version 3.0 ."

        self.setWindowTitle("Calculator")
        self.resize(263, 370)
        self.setFixedSize(263, 370)              # making the calculator resizable
        self.setWindowIcon(QtGui.QIcon('pkldll'))
        self.setAutoFillBackground(False)
        self.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(229, 239, 255);")

        centralWidget=QtGui.QWidget(self)
        centralWidget.show()
        self.setCentralWidget(centralWidget)

        font= QtGui.QFont("Comic Sans",10)
        font.setItalic(False)
        font.setBold(False)
        self.versionpb= QtGui.QLabel(centralWidget)
        self.versionpb.setGeometry(QtCore.QRect(0, 0, 261, 25))
        self.versionpb.setText("www.versionpb.com")
        self.versionpb.show()

        self.lineEditu = QtGui.QLabel(centralWidget)
        self.lineEditu.setGeometry(QtCore.QRect(0, 0, 261, 25))
        self.lineEditu.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditu.setAlignment(QtCore.Qt.AlignRight)
        self.lineEditu.show()
        self.lineEditu.setFont(font)

        self.lineEdit = QtGui.QLabel(centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 20, 261, 50))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        font = QtGui.QFont("Comic Sans",20)
        font.setItalic(False)
        font.setBold(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("0")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight)                    # Align Text in Line edit to the right
        self.lineEdit.setFocus()                                            #Setting Default focus on main line Edit
        self.lineEdit.show()

        pushButton_2 = QtGui.QPushButton(centralWidget)
        pushButton_2.setGeometry(QtCore.QRect(10, 70, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        pushButton_2.setFont(font)
        pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_2.setAutoFillBackground(False)
        pushButton_2.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_3 = QtGui.QPushButton(centralWidget)
        pushButton_3.setGeometry(QtCore.QRect(60, 70, 41, 31))
        pushButton_3.setFont(font)
        pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_3.setAutoFillBackground(False)
        pushButton_3.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_4 = QtGui.QPushButton(centralWidget)
        pushButton_4.setGeometry(QtCore.QRect(110, 70, 41, 31))
        pushButton_4.setFont(font)
        pushButton_4.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        #pushButton_6 = QtGui.QPushButton(centralWidget)
        #pushButton_6.setGeometry(QtCore.QRect(210, 70, 41, 31))
        #pushButton_6.setFont(font)
        #pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #pushButton_6.setAutoFillBackground(False)
        #pushButton_6.setStyleSheet("background-color: rgb(192, 228, 255);\n"
#"\n"
#"")

        pushButton_7 = QtGui.QPushButton(centralWidget)
        pushButton_7.setGeometry(QtCore.QRect(160, 70, 91, 31))
        pushButton_7.setFont(font)
        pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_7.setAutoFillBackground(False)
        pushButton_7.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_8 = QtGui.QPushButton(centralWidget)
        pushButton_8.setGeometry(QtCore.QRect(110, 110, 41, 31))

        pushButton_8.setFont(font)
        pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_8.setAutoFillBackground(False)
        pushButton_8.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_9 = QtGui.QPushButton(centralWidget)
        pushButton_9.setGeometry(QtCore.QRect(60, 110, 41, 31))

        pushButton_9.setFont(font)
        pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_9.setAutoFillBackground(False)
        pushButton_9.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_10 = QtGui.QPushButton(centralWidget)
        pushButton_10.setGeometry(QtCore.QRect(160, 110, 41, 31))

        pushButton_10.setFont(font)
        pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_10.setAutoFillBackground(False)
        pushButton_10.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_11 = QtGui.QPushButton(centralWidget)
        pushButton_11.setGeometry(QtCore.QRect(10, 110, 41, 31))

        pushButton_11.setFont(font)
        pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_11.setAutoFillBackground(False)
        pushButton_11.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_12 = QtGui.QPushButton(centralWidget)
        pushButton_12.setGeometry(QtCore.QRect(210, 110, 41, 31))

        pushButton_12.setFont(font)
        pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_12.setAutoFillBackground(False)
        pushButton_12.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_13 = QtGui.QPushButton(centralWidget)
        pushButton_13.setGeometry(QtCore.QRect(110, 150, 41, 31))

        pushButton_13.setFont(font)
        pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_13.setAutoFillBackground(False)
        pushButton_13.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_14 = QtGui.QPushButton(centralWidget)
        pushButton_14.setGeometry(QtCore.QRect(60, 150, 41, 31))

        pushButton_14.setFont(font)
        pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_14.setAutoFillBackground(False)
        pushButton_14.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_15 = QtGui.QPushButton(centralWidget)
        pushButton_15.setGeometry(QtCore.QRect(160, 150, 41, 31))

        pushButton_15.setFont(font)
        pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_15.setAutoFillBackground(False)
        pushButton_15.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_16 = QtGui.QPushButton(centralWidget)
        pushButton_16.setGeometry(QtCore.QRect(10, 150, 41, 31))

        pushButton_16.setFont(font)
        pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_16.setAutoFillBackground(False)
        pushButton_16.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_17 = QtGui.QPushButton(centralWidget)
        pushButton_17.setGeometry(QtCore.QRect(210, 150, 41, 31))

        pushButton_17.setFont(font)
        pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_17.setAutoFillBackground(False)
        pushButton_17.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_18 = QtGui.QPushButton(centralWidget)
        pushButton_18.setGeometry(QtCore.QRect(110, 190, 41, 31))
        pushButton_18.setFont(font)
        pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_18.setAutoFillBackground(False)
        pushButton_18.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_19 = QtGui.QPushButton(centralWidget)
        pushButton_19.setGeometry(QtCore.QRect(60, 190, 41, 31))

        pushButton_19.setFont(font)
        pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_19.setAutoFillBackground(False)
        pushButton_19.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_20 = QtGui.QPushButton(centralWidget)
        pushButton_20.setGeometry(QtCore.QRect(160, 190, 41, 31))

        pushButton_20.setFont(font)
        pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_20.setAutoFillBackground(False)
        pushButton_20.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_21 = QtGui.QPushButton(centralWidget)
        pushButton_21.setGeometry(QtCore.QRect(10, 190, 41, 31))

        pushButton_21.setFont(font)
        pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_21.setAutoFillBackground(False)
        pushButton_21.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_22 = QtGui.QPushButton(centralWidget)
        pushButton_22.setGeometry(QtCore.QRect(210, 190, 41, 31))

        pushButton_22.setFont(font)
        pushButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_22.setAutoFillBackground(False)
        pushButton_22.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_23 = QtGui.QPushButton(centralWidget)
        pushButton_23.setGeometry(QtCore.QRect(110, 230, 41, 31))

        pushButton_23.setFont(font)
        pushButton_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_23.setAutoFillBackground(False)
        pushButton_23.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_24 = QtGui.QPushButton(centralWidget)
        pushButton_24.setGeometry(QtCore.QRect(60, 230, 41, 31))

        pushButton_24.setFont(font)
        pushButton_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_24.setAutoFillBackground(False)
        pushButton_24.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_25 = QtGui.QPushButton(centralWidget)
        pushButton_25.setGeometry(QtCore.QRect(160, 230, 41, 31))

        pushButton_25.setFont(font)
        pushButton_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_25.setAutoFillBackground(False)
        pushButton_25.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_26 = QtGui.QPushButton(centralWidget)
        pushButton_26.setGeometry(QtCore.QRect(10, 230, 41, 31))

        pushButton_26.setFont(font)
        pushButton_26.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_26.setAutoFillBackground(False)
        pushButton_26.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_27 = QtGui.QPushButton(centralWidget)
        pushButton_27.setGeometry(QtCore.QRect(210, 230, 41, 71))

        pushButton_27.setFont(font)
        pushButton_27.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_27.setAutoFillBackground(False)
        pushButton_27.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_28 = QtGui.QPushButton(centralWidget)
        pushButton_28.setGeometry(QtCore.QRect(110, 270, 41, 31))

        pushButton_28.setFont(font)
        pushButton_28.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_28.setAutoFillBackground(False)
        pushButton_28.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_30 = QtGui.QPushButton(centralWidget)
        pushButton_30.setGeometry(QtCore.QRect(160, 270, 41, 31))

        pushButton_30.setFont(font)
        pushButton_30.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_30.setAutoFillBackground(False)
        pushButton_30.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        pushButton_31 = QtGui.QPushButton(centralWidget)
        pushButton_31.setGeometry(QtCore.QRect(10, 270, 91, 31))

        pushButton_31.setFont(font)
        pushButton_31.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_31.setAutoFillBackground(False)
        pushButton_31.setStyleSheet("background-color: rgb(192, 228, 255);\n"
"\n"
"")

        self.versionpb= QtGui.QLabel("<qt><a href> www.versionpb.com</qt>",centralWidget)
        self.versionpb.setGeometry(QtCore.QRect(150, 301, 100, 20))
        #self.versionpb.setText("www.versionpb.com")
        self.versionpb.show()

        self.versionpbRegister= QtGui.QLabel(centralWidget)
        self.versionpbRegister.setText('<qt><a href="http://www.versionpb.com/register-your-product/" >Register for Free !</qt>')
        self.versionpbRegister.setGeometry(QtCore.QRect(15, 301, 100, 20))
        self.versionpbRegister.show()
        self.versionpbRegister.setMaximumHeight(15)





        menuBar = QtGui.QMenuBar(centralWidget)
        menuBar.setGeometry(QtCore.QRect(0, 0, 263, 21))

        menuView = QtGui.QMenu(menuBar)
        menuView.show()
        menuEdit = QtGui.QMenu(menuBar)
        menuHelp = QtGui.QMenu(menuBar)


        self.setMenuBar(menuBar)
        statusBar = QtGui.QStatusBar(centralWidget)
        self.setStatusBar(statusBar)

        toolBar = QtGui.QToolBar(centralWidget)
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

        self.addToolBar(QtCore.Qt.TopToolBarArea, toolBar)
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
        QtCore.QObject.connect(pushButton_26, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("1"))
        QtCore.QObject.connect(pushButton_24, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("2"))
        QtCore.QObject.connect(pushButton_23, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("3"))
        QtCore.QObject.connect(pushButton_21, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("4"))
        QtCore.QObject.connect(pushButton_19, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("5"))
        QtCore.QObject.connect(pushButton_18, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("6"))
        QtCore.QObject.connect(pushButton_16, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("7"))
        QtCore.QObject.connect(pushButton_14, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("8"))
        QtCore.QObject.connect(pushButton_13, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("9"))
        QtCore.QObject.connect(pushButton_31, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("0"))
        QtCore.QObject.connect(pushButton_28, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("."))
        QtCore.QObject.connect(pushButton_30, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("+"))
        QtCore.QObject.connect(pushButton_25, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("-"))
        QtCore.QObject.connect(pushButton_20, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("*"))
        QtCore.QObject.connect(pushButton_15, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("/"))
        QtCore.QObject.connect(pushButton_27, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("="))
        QtCore.QObject.connect(pushButton_9, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("CE"))
        QtCore.QObject.connect(pushButton_8, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("C"))
        QtCore.QObject.connect(pushButton_11, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("backspace"))
        QtCore.QObject.connect(pushButton_12, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("sqrt"))
        QtCore.QObject.connect(pushButton_22, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("Reci"))
        QtCore.QObject.connect(pushButton_10, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("+-"))
        QtCore.QObject.connect(pushButton_17, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("%"))
        QtCore.QObject.connect(pushButton_2, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("("))
        QtCore.QObject.connect(pushButton_3, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt(")"))
        QtCore.QObject.connect(pushButton_4, QtCore.SIGNAL("clicked()"), lambda:ui.CallAddTxt("^"))
        QtCore.QObject.connect(pushButton_7, QtCore.SIGNAL("clicked()"), lambda:CalculatorInputLogic().showExpression(ui))

        self.actionCopy.triggered.connect(lambda: ui.Copy())
        self.actionCopyE.triggered.connect(lambda: ui.CopyE())
        self.actionPaste.triggered.connect(lambda: ui.Paste())

        self.versionpb.linkActivated.connect(lambda:self.openurl())
        #About is a Class in About Module to show About us dialog
        actionAbout.triggered.connect(lambda: About())      #Putting action in the About menu Paarth 23rd Aug 2013
        self.actionContents.triggered.connect(lambda :self.openContents())
        self.versionpbRegister.linkActivated.connect(lambda:self.openRegisterurl())

    def openContents(self):
        b = webbrowser
        b.open('http://www.versionpb.com/products/bodmas-calculator/bodmas-calculator-documentation/')

    def CallAddTxt(self,input):
        print "Values Passed are : input : ",input,"lineE : ",self.lineE,"lineEU : ",ui.lineEU,"setlineE : ",ui.setlineE,"setlineEU : ",ui.setlineEU
        CalculatorInputLogic().addTxt(ui,input)
        print "Values After function are : input : ",input,"lineE : ",ui.lineE,"lineEU : ",ui.lineEU,"setlineE : ",ui.setlineE,"setlineEU : ",ui.setlineEU

    def openRegisterurl(self):
        b = webbrowser
        b.open('http://www.versionpb.com/register-your-product/')

    def Copy(self):

            #w.OpenClipboard()

        command = 'echo ' + ui.lineE + '| clip'
        os.system(command)

        print ui.lineE
            #command = 'echo ' + ui.lineE + '| clip'
            #os.system(command)

    def CopyE(self):
        command = 'echo ' + ui.lineEU + '| clip'
        os.system(command)

    def Paste(self):
        #if ui.lineEdit.hasFocus():
        w.OpenClipboard()
        data = w.GetClipboardData()
        print "Passing data as",data
        try:
            v=eval(data)
            print v
            ui.lineEdit.setText(data)
            ui.lineE = data
        except Exception as E:
            print E
            print "Wrong data"
        w.CloseClipboard()
        #print txt

    def openurl(self):
        b = webbrowser
        b.open('http://www.versionpb.com')

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui=Calculator()

    lineE = "0"
    lineEU = ""
    setlineE = "0"
    setlineEU = ""

    sys.exit(app.exec_())

