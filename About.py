__author__ = 'pbatra'

#Version 2.0 
# last change date 7th Sept 2013
# Removed background image
# Changed look and Feel


from PyQt6 import QtWidgets, QtGui, QtCore
import sys
#This is the current prod version
class About(QtWidgets.QDialog):
    def __init__(self):
        super(About,self).__init__()
        self.initUI()

    def initUI(self):
        #e=QtGui.QDialog()                           # create e as new Dialog box
        self.setWindowTitle("About us")                # Dialog box title
        #self.show()                                     # Show dialog box , Commenting this will help make this modal /
                            #  i.e. when user will open the about me dialog , User wont be able to anything until he closes this dialog

        self.setWindowIcon(QtGui.QIcon('pkldll'))
        self.setFixedSize(300,200)                          #Setting size of About us
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        q=self.frameGeometry()                               # We get a rectangle specifying the geometry of the main window. This includes any window frame.
        # cp=QtGui.QDesktopWidget().availableGeometry().center()          #We figure out the screen resolution of our monitor. And from this resolution, we get the center point.
        # PyQt6: QDesktopWidget is removed. Use QScreen.availableGeometry()
        screen = QtGui.QGuiApplication.primaryScreen()
        cp = screen.availableGeometry().center()
        
        q.moveCenter(cp)                                            #Now we set the center of the rectangle to the center of the screen
        self.move(q.topLeft())                                         #We move the top-left point of the application window to the top-left point of the q rectangle

        # Setting style sheet for the about us dialog window


        label=QtWidgets.QLabel(self)
        label.setGeometry(190,0,100,100)
        label.show()
        font1= QtGui.QFont("Comic Sans MS",6)
        font1.setItalic(False)
        font1.setBold(False)


        labelTag=QtWidgets.QLabel(self)
        labelTag.setGeometry(190,80,140,100)
        labelTag.setText("Its all about What do u want !\n\n"
                         "Sno. 280820130000001")
        labelTag.setFont(font1)
        labelTag.show()
        # Putting a Button on the About us Dialog box
        OkButton=QtWidgets.QPushButton("OK",self)
        OkButton.move(220,170)
        OkButton.show()
        OkButton.setFocus()
        OkButton.clicked.connect(self.close)

        # Setting a font for the label
        font= QtGui.QFont("Comic Sans MS",8)
        font.setItalic(False)
        font.setBold(False)

        # Putting a Label on About us Dialog Box
        labelAboutUs=QtWidgets.QLabel(self)
        labelAboutUs.setText("\nSimple BODMAS Calcular : \n"
                             "It Does Maths using BODMAS Rule \n\n\n"
                             "Author - Paarth Batra \n"
                             "Version - 3.0.0.0\n"
                             "Releasedate - 02 Oct 2013\n\n"
                             "Contact :\n"
                             "paarthh2@rediffmail.com\n"
                             "paarth_batra@yahoo.co.in \n"

                             )
        labelAboutUs.setFont(font)
        labelAboutUs.move(5,10)
        labelAboutUs.show()

        self.setStyleSheet("background-color: white;")
        label.setStyleSheet("image: url(pbcabtdll);")
        labelAboutUs.setStyleSheet("color:#003300;")
        OkButton.setStyleSheet("background-color: #DCDCDC;")

        self.setFocus()
        self.setModal(True)
        self.exec()



#def main():

 #   app = QtGui.QApplication(sys.argv)
  #  ex2=About()
   # sys.exit(app.exec_())


#if __name__ == '__main__':
 #   main()
