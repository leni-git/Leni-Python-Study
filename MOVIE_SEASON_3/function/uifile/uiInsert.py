# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insert.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Insert(object):
    def setupUi(self, Insert):
        Insert.setObjectName("Insert")
        Insert.resize(407, 331)
        self.widget = QtWidgets.QWidget(Insert)
        self.widget.setGeometry(QtCore.QRect(60, 30, 291, 251))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addWidget(self.splitter)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.splitter_3 = QtWidgets.QSplitter(self.widget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.pushButton = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.splitter_3)

        self.retranslateUi(Insert)
        self.pushButton.clicked.connect(Insert.btn_ok_action)
        self.pushButton_2.clicked.connect(Insert.btn_cancel_action)
        QtCore.QMetaObject.connectSlotsByName(Insert)

    def retranslateUi(self, Insert):
        _translate = QtCore.QCoreApplication.translate
        Insert.setWindowTitle(_translate("Insert", "Dialog"))
        self.label.setText(_translate("Insert", "NAME"))
        self.label_2.setText(_translate("Insert", "LOCATION"))
        self.label_3.setText(_translate("Insert", "TIME"))
        self.pushButton.setText(_translate("Insert", "OK"))
        self.pushButton_2.setText(_translate("Insert", "CANCEL"))

