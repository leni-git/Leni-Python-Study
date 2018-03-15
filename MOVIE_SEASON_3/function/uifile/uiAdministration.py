# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administration.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_movieListWindow(object):
    def setupUi(self, movieListWindow):
        movieListWindow.setObjectName("movieListWindow")
        movieListWindow.resize(1200, 800)
        movieListWindow.setMinimumSize(QtCore.QSize(1200, 800))
        movieListWindow.setMaximumSize(QtCore.QSize(1200, 800))
        self.centralwidget = QtWidgets.QWidget(movieListWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 690, 1161, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 1161, 661))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1159, 659))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 1161, 661))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.movielist = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.movielist.setObjectName("movielist")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        movieListWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(movieListWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 28))
        self.menubar.setObjectName("menubar")
        movieListWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(movieListWindow)
        self.statusbar.setObjectName("statusbar")
        movieListWindow.setStatusBar(self.statusbar)

        self.retranslateUi(movieListWindow)
        self.pushButton.clicked.connect(movieListWindow.administration_btn_action)
        self.pushButton_2.clicked.connect(movieListWindow.administration_btn_action)
        self.pushButton_3.clicked.connect(movieListWindow.administration_btn_action)
        QtCore.QMetaObject.connectSlotsByName(movieListWindow)

    def retranslateUi(self, movieListWindow):
        _translate = QtCore.QCoreApplication.translate
        movieListWindow.setWindowTitle(_translate("movieListWindow", "MainWindow"))
        self.pushButton.setText(_translate("movieListWindow", "Insert"))
        self.pushButton_2.setText(_translate("movieListWindow", "Edit"))
        self.pushButton_3.setText(_translate("movieListWindow", "Delete"))

