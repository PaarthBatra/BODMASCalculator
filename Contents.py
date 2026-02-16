__author__ = 'pbatra'


#Version 1.0
# last change date 2nd Oct 2013



from PyQt4 import QtGui, QtCore
#import PyQt4
import sys
#This is the current prod version
class Contents(QtGui.QDialog):
    def __init__(self):
        super(Contents,self).__init__()
        self.initUI()



    def initUI(self):
        #e=QtGui.QDialog()                           # create e as new Dialog box
        self.setWindowTitle("Contents")                # Dialog box title
        #self.show()                                     # Show dialog box , Commenting this will help make this modal /
                            #  i.e. when user will open the about me dialog , User wont be able to anything until he closes this dialog


        Content="""
---------------------------------------------------------------------------------------------------------
                                                HELP DOCUMENTATION
                                            Website : www.versionpb.com
                                               Author : Paarth Batra
---------------------------------------------------------------------------------------------------------

    This documentation is designed to help you familiarize yourself with the interface and
    functions of BODMAS Calculator 2.0.9.0


---------------------------------------------------------------------------------------------------------
                                            **** ONLINE HELP ****
---------------------------------------------------------------------------------------------------------


    You can also refer Online Documentation
        @ http://www.versionpb.com/documentation/bodmas-calculator-help

        or
    send E mail @ paarth.batra@gmail.com
    paarth_batra@yahoo.co.in
    paarthh2@rediffmail.com

---------------------------------------------------------------------------------------------------------
                                            **** INTERFACE ****
---------------------------------------------------------------------------------------------------------

    We display a nice GUI with Buttons . You can enter values from Mouse click as well as
    keyboard entry

---------------------------------------------------------------------------------------------------------
                                            Menu Options and Use
---------------------------------------------------------------------------------------------------------

    View Menu : Currently it have only standard view . if required we may have more views
    like full-screen or scientific views in future .

    Edit Menu :

    Copy : This option have a shortcut as Control-C and when pressed or clicked it will
    copy anything which is written in the Calculator lower area

    Copy Expression : This option is for copying of the current Expression .

    Paste : Paste option is for pasing any expression or numerical values in it . For
    Example you have a bodmas expression like (23 +8 )*7 you can directly paste it in
    Calculator , however if you have any string or non-bodmas expression copied and
    you try pasting it . Nothing will happen


    Help Menu

    Contents : Contains Help and License regarding information

    About :  Information about author version and release date

---------------------------------------------------------------------------------------------------------
                                            Buttons and their uses
---------------------------------------------------------------------------------------------------------

    brackets button ( , ) : both of these buttons are introduced and can be used as
    BODMAS brackets . you can not enter ) in the start of any expression .

    ^ : power button , currently this is diabled as currently if you want to give power
    to any number you need to right 5*5 . This feature may be added in future releases

    Expression = : This button is used to show current expression in the upper part of calculator
    and its result in the lower part of the calculator display field .

    <== : this is a backspace button

    CE : This button clears current content in the lower display part of the calculator

    C : This is clear button . Clicking this will reset everything .

    +- : This is Negate button and currently works only on very basic values

    underscore: This Button is for computing square root. This function is valid only for stand
    alone computations

    0-9 numeric buttons : this are basic 0-9 digits in Maths

    / : Division operator

    % : Computation of percentage

    * : Multiplication operator

    1/x : Reciprocal function and works only on single digits

    - : Subtraction operator

    . : Mathematics dot

    + : Addition operator

    = : = operator

---------------------------------------------------------------------------------------------------------
                                            LICENSE
---------------------------------------------------------------------------------------------------------
    BODMAS Calculator is free software, feel free to share it with friends. Any ideas or
    suggestions will be appreciated.

    This software can be used by anyone for non-profit use .

---------------------------------------------------------------------------------------------------------



Documentation by Paarth Batra
visit: http://www.versionpb.com
send comments or questions to paarth_batra@yahoo.co.in
"""




        self.setWindowIcon(QtGui.QIcon('pkldll'))
        #self.setGeometry(0,0,500,200)
        #scrollingWidget = QtGui.QScrollBar(self)
        #scrollingWidget.setMinimum(0)
        #scrollingWidget.setMaximum(100)
        scrollArea=QtGui.QScrollArea(self)
        scrollArea.setGeometry(0,0,500,250)
        scrollArea.setWidgetResizable(True)
        scrollArea.setEnabled(True)
        #scrollArea.setWidget(scrollingWidget)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        q=self.frameGeometry()                               # We get a rectangle specifying the geometry of the main window. This includes any window frame.
        cp=QtGui.QDesktopWidget().availableGeometry().center()          #We figure out the screen resolution of our monitor. And from this resolution, we get the center point.
        q.moveCenter(cp)                                            #Now we set the center of the rectangle to the center of the screen
        self.move(q.topLeft())


        # Setting style sheet for the about us dialog window


        label=QtGui.QLabel(self)
        label.setGeometry(190,0,100,100)
        label.show()
        font1= QtGui.QFont("Comic Sans MS",6)
        font1.setItalic(False)
        font1.setBold(False)


        # Putting a Button on the About us Dialog box
        OkButton=QtGui.QPushButton("OK",self)
        OkButton.move(400,210)
        OkButton.show()
        OkButton.setFocus()
        OkButton.clicked.connect(self.close)

        # Setting a font for the label
        font= QtGui.QFont("Comic Sans MS",8)
        font.setItalic(False)
        font.setBold(False)

        # Putting a Label on About us Dialog Box
        labelAboutUs=QtGui.QLabel(self)
        labelAboutUs.setText(Content)
        labelAboutUs.setFont(font)
        labelAboutUs.move(5,10)
        labelAboutUs.show()

        scrollArea.setWidget(labelAboutUs)
        OkButton.setStyleSheet("background-color: #DCDCDC;")



        self.setFocus(True)
        self.setModal(True)
        self.exec_()



def main():

    app = QtGui.QApplication(sys.argv)
    ex2=Contents()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


