# -*- coding: utf8 -*-

import user
# import PyQt5 module.
from PyQt5.QtWidgets import QMainWindow, qApp, QMessageBox

# Custom ui Packager import.
from uifile.uiEnjoy import Ui_EnjoyWindow
# Function Package import.
from employeefunction import Employee
from uifile.uiEmployee import Ui_EmployeeWindow
from reservationfunction import Reservation
from uifile.uiReservation import Ui_reservationWindow



import sys


class Login(QMainWindow):
    def __init__(self, socket):
        QMainWindow.__init__(self)

        Login.socket = socket
        qApp.setStyleSheet("QMainWindow, QDialog { background-color: rgb(255, 255, 255) }")

    @staticmethod
    def closeEvent(event):
        result = QMessageBox.question(Login.login, "Confirm Exit...", "Are you sure you want to exit ?",
                                      QMessageBox.Yes | QMessageBox.No)
        event.ignore()

        if result == QMessageBox.Yes:
            event.accept()

    @staticmethod
    def func_login():
        # Try to check customer if Enter id and pw by user.
        Login.socket.send_message(Login.socket.client_socket, 'LOGIN_CLIENT# %s# %s' %
                                  (Login.login.ui.le_id.text(), Login.login.ui.le_pw.text()))
        message = Login.socket.recv_message(Login.socket.client_socket)
        if message[0] == 'MOVIE_INFO':
            # user define.
            user.set_info(message[1], message[2], message[3], message[4])
            Login.socket.send_message(Login.socket.client_socket, 'MOVIE_INFO_READY')
            # fsock function start, get movies data from server socket.employee' and go there.\
            user.set_movies(Login.socket.socket_connect_file())
            if user.get_user_grade() == '0':
                Login.window_employee = Employee(Login.socket, Login.login)
                Login.window_employee.ui = Ui_EmployeeWindow()
                Login.window_employee.ui.setupUi(Login.window_employee)
                Login.window_employee.show()
            elif user.get_user_grade() == '1':
                Reservation.reservation = Reservation(Login.socket, Login.login)
                Reservation.reservation.ui = Ui_reservationWindow()
                Reservation.reservation.ui.setupUi(Reservation.reservation)
                Reservation.load_movies()
                Reservation.reservation.show()

            Login.mosquitto.mosquitto_start(user.get_ad_agree())
            Login.login.hide()

    @staticmethod
    def menu():
        print 'menu'

    @staticmethod
    def func_enjoy():
        # open page 'uiEnjoy'
        Login.window_enjoy = QMainWindow()
        Login.window_enjoy.ui = Ui_EnjoyWindow()
        Login.window_enjoy.ui.setupUi(Login.window_enjoy)
        Login.window_enjoy.show()
        print 'func_enjoy'



