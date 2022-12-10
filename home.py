# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/home.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.visualise_button = QtWidgets.QPushButton(self.centralwidget)
        self.visualise_button.setGeometry(QtCore.QRect(430, 350, 191, 121))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(36)
        self.visualise_button.setFont(font)
        self.visualise_button.setObjectName("visualise_button")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(490, 200, 381, 91))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(64)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.annotate_button = QtWidgets.QPushButton(self.centralwidget)
        self.annotate_button.setGeometry(QtCore.QRect(760, 350, 191, 121))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(36)
        self.annotate_button.setFont(font)
        self.annotate_button.setObjectName("annotate_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Emotion GUI"))
        self.visualise_button.setText(_translate("MainWindow", "Visualize"))
        self.label1.setText(_translate("MainWindow", "Emotion GUI"))
        self.annotate_button.setText(_translate("MainWindow", "Annotation"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

