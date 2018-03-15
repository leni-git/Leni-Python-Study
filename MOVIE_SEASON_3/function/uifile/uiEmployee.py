# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'employee.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EmployeeWindow(object):
    def setupUi(self, EmployeeWindow):
        EmployeeWindow.setObjectName("EmployeeWindow")
        EmployeeWindow.resize(800, 600)
        EmployeeWindow.setMinimumSize(QtCore.QSize(800, 600))
        EmployeeWindow.setMaximumSize(QtCore.QSize(800, 600))
        EmployeeWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        EmployeeWindow.setStyleSheet("QPushButton:hover { background-color: rgb(255, 228, 245)}")
        EmployeeWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        EmployeeWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(EmployeeWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 150, 371, 268))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_reservation = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_reservation.setEnabled(True)
        self.btn_reservation.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_reservation.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("reservation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reservation.setIcon(icon)
        self.btn_reservation.setIconSize(QtCore.QSize(36, 36))
        self.btn_reservation.setAutoDefault(False)
        self.btn_reservation.setFlat(False)
        self.btn_reservation.setObjectName("btn_reservation")
        self.horizontalLayout.addWidget(self.btn_reservation)
        self.btn_information = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_information.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_information.setObjectName("btn_information")
        self.horizontalLayout.addWidget(self.btn_information)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_administration = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_administration.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_administration.setObjectName("btn_administration")
        self.horizontalLayout_2.addWidget(self.btn_administration)
        self.btn_totalincome = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_totalincome.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_totalincome.setObjectName("btn_totalincome")
        self.horizontalLayout_2.addWidget(self.btn_totalincome)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btn_exit = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_exit.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout.addWidget(self.btn_exit)
        EmployeeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EmployeeWindow)
        self.statusbar.setObjectName("statusbar")
        EmployeeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EmployeeWindow)
        #self.btn_reservation.clicked.connect(EmployeeWindow.btn_reservation_action)
        self.btn_information.clicked.connect(EmployeeWindow.employee_btn_action)
        self.btn_totalincome.clicked.connect(EmployeeWindow.employee_btn_action)
        self.btn_administration.clicked.connect(EmployeeWindow.employee_btn_action)
        self.btn_exit.clicked.connect(EmployeeWindow.employee_btn_action)
        self.btn_reservation.clicked.connect(EmployeeWindow.employee_btn_action)
        QtCore.QMetaObject.connectSlotsByName(EmployeeWindow)

    def retranslateUi(self, EmployeeWindow):
        _translate = QtCore.QCoreApplication.translate
        EmployeeWindow.setWindowTitle(_translate("EmployeeWindow", "MainWindow"))
        self.btn_reservation.setText(_translate("EmployeeWindow", "Reservation"))
        self.btn_information.setText(_translate("EmployeeWindow", "Information"))
        self.btn_administration.setText(_translate("EmployeeWindow", "Administration"))
        self.btn_totalincome.setText(_translate("EmployeeWindow", "Total Income"))
        self.btn_exit.setText(_translate("EmployeeWindow", "Exit"))

