# -*- coding: utf8 -*-

import user
# import PyQt5 module.
from PyQt5.QtWidgets import QMainWindow

# Function Package import.
from reservationfunction import Reservation
from uifile.uiReservation import Ui_reservationWindow
from administrationfunction import Administration
from uifile.uiAdministration import Ui_movieListWindow


class Employee(QMainWindow):
    def __init__(self, socket, login):
        QMainWindow.__init__(self)
        Employee.socket = socket
        Employee.login = login
        Employee.employee = self
        print 'Employee'

    # @staticmethod
    # def btn_reservation_action():
    #     print 'btn_reservation_action'

    # Make Employee Method
    def employee_btn_action(self):
        sender = self.sender().text()
        if sender == 'Exit':
            # close self, and open parents page.
            self.close()
            Employee.socket.close()
            Employee.login.show()
        elif sender == 'Reservation':
            print 'Open reservation page'
            Reservation.reservation = Reservation(Employee.socket, Employee.employee)
            Reservation.reservation.ui = Ui_reservationWindow()
            Reservation.reservation.ui.setupUi(Reservation.reservation)
            Reservation.load_movies()
            Reservation.reservation.show()
        elif sender == 'Information':
            print 'Open information page, plz edit name'

        elif sender == 'Administration':
            print 'Open Administration page'
            Administration.administration = Administration(Employee.socket, Employee.employee)
            Administration.administration.ui = Ui_movieListWindow()
            Administration.administration.ui.setupUi(Administration.administration)
            Administration.administration.load_movies()
            Administration.administration.show()

        elif sender == 'Total Income':
            print 'Open Total Income page'

        Employee.employee.hide()
