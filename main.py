import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget, QPushButton
from home import Ui_MainWindow


class MainWindow(QMainWindow, QPushButton):
    def __init__(self):
        super(MainWindow, self).__init__()

        loadUi('ui/home.ui', self)

        self.visualiseB = self.findChild(
            QtWidgets.QPushButton, 'visualise_button')
        self.visualiseB.clicked.connect(self.goto_visualize)

        self.annotateB = self.findChild(
            QtWidgets.QPushButton, 'annotate_button')
        self.annotateB.clicked.connect(self.goto_annotate)

    def goto_visualize(self):
        visualise = visualisationScreen()
        widget.addWidget(visualise)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_annotate(self):
        annotate = annotationScreen()
        widget.addWidget(annotate)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class visualisationScreen(QWidget):
    def __init__(self):
        super(visualisationScreen, self).__init__()
        loadUi('ui/visualize.ui', self)
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
