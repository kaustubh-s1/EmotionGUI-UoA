import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QLinearGradient, QColor, QPalette, QBrush
from PyQt5 import QtGui
# from realtime_spectogram import RunProgram
import realtime_spectogram as rs
from file_processing import FileProcessing


class MainWindow(QMainWindow, QPushButton):
    def __init__(self):
        super(MainWindow, self).__init__()

        loadUi('ui/home.ui', self)
        pic = QPixmap('static/uoa_logo.png')
        self.imglabel.setPixmap(pic)

        self.visualiseB = self.findChild(
            QtWidgets.QPushButton, 'visualise_button')
        self.visualiseB.clicked.connect(self.goto_visualize)

        self.annotateB = self.findChild(
            QtWidgets.QPushButton, 'annotate_button')
        self.annotateB.clicked.connect(self.goto_annotate)

        self.liveAudioB = self.findChild(
            QtWidgets.QPushButton, 'liveAudio_button')
        self.liveAudioB.clicked.connect(self.goto_liveAudio)

    def goto_visualize(self):
        visualise = visualisationScreen()
        widget.addWidget(visualise)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_annotate(self):
        annotate = annotationScreen()
        widget.addWidget(annotate)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_liveAudio(self):
        liveAudio = rs.RunProgram()
        widget.addWidget(liveAudio)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        liveAudioScreen(liveAudio.getHomeButton())


class visualisationScreen(QWidget):
    def __init__(self):
        super(visualisationScreen, self).__init__()
        loadUi('ui/visualize.ui', self)
        
        # -------------------------------------------------------------
        # to get the dialog box when the 'Select CSV' button is clicked and write the path of file on the text editor
        self.select_csv = self.findChild(
            QtWidgets.QPushButton, 'select_csv')
        self.select_csv.clicked.connect(lambda: self.textEdit.setText(FileProcessing.open_dialog_box(self)))
        #--------------------------------------------------------------

        # -------------------------------------------------------------
        # to get the dialog box when the 'Select CSV' button is clicked and write the path of file on the text editor
        self.select_wav = self.findChild(
            QtWidgets.QPushButton, 'select_wav')
        self.select_wav.clicked.connect(
            lambda: self.textEdit_2.setText(FileProcessing.open_dialog_box(self)))
        #--------------------------------------------------------------
        
        self.homeB = self.findChild(
            QtWidgets.QPushButton, 'pushButton_8')
        self.homeB.clicked.connect(self.goto_home)

    def goto_home(self):
        home = MainWindow()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.setCurrentWidget(home)
        

class annotationScreen(QWidget):
    def __init__(self):
        super(annotationScreen, self).__init__()
        loadUi('ui/annotate.ui', self)
        self.homeB = self.findChild(
            QtWidgets.QPushButton, 'home_button_annotator')
        self.homeB.clicked.connect(self.goto_home)

    def goto_home(self):
        home = MainWindow()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.setCurrentWidget(home)


class liveAudioScreen(QMainWindow, QWidget):
    def __init__(self, homeB):
        super(liveAudioScreen, self).__init__()
        # self.homeB = rs.RunProgram.getHomeButton(self)
        self.homeButton = homeB
        self.homeButton.clicked.connect(self.goto_home)

    def goto_home(self):
        home = MainWindow()
        widget.addWidget(home)
        print("This func is called")
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.setCurrentWidget(home)


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        widget = QtWidgets.QStackedWidget()

        home = MainWindow()

        widget.addWidget(home)
        widget.showMaximized()
        sys.exit(app.exec_())
    except:
        print("Exit")
