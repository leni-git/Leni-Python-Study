# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enjoy.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EnjoyWindow(object):
    def setupUi(self, EnjoyWindow):
        EnjoyWindow.setObjectName("EnjoyWindow")
        EnjoyWindow.resize(800, 600)
        EnjoyWindow.setMinimumSize(QtCore.QSize(800, 600))
        EnjoyWindow.setMaximumSize(QtCore.QSize(800, 600))
        EnjoyWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(EnjoyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 220, 241, 141))
        self.label.setObjectName("label")
        EnjoyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EnjoyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        EnjoyWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EnjoyWindow)
        self.statusbar.setObjectName("statusbar")
        EnjoyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EnjoyWindow)
        QtCore.QMetaObject.connectSlotsByName(EnjoyWindow)

    def retranslateUi(self, EnjoyWindow):
        _translate = QtCore.QCoreApplication.translate
        EnjoyWindow.setWindowTitle(_translate("EnjoyWindow", "EnjoyWindow"))
        self.label.setText(_translate("EnjoyWindow", "<html><head/><body><p align=\"center\">I\'ll make Insert page.</p><p align=\"center\">coming soon...</p></body></html>"))

