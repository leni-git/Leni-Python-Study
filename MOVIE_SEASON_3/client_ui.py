# -*- coding: utf8 -*-

import user

from PyQt5.QtWidgets import QApplication
# Custom Package import
# Information Package import.
from information.re_socketinfo import ClientSocket
# Function Package import.
from function.loginfunction import Login
from function.uifile.uiLogin import Ui_LoginWindow

# Mosquitto sub import.
from sub import Paho_Mqtt

# import sys module
# It used to exit client.
import sys

# This it main
if __name__ == '__main__':

    # Basic value
    socket = ClientSocket()
    message = socket.recv_message(socket.client_socket)
    Login.mosquitto = Paho_Mqtt()

    if message[0] == 'LOGIN':
        app = QApplication(sys.argv)

        Login.login = Login(socket)
        Login.login.ui = Ui_LoginWindow()
        Login.login.ui.setupUi(Login.login)
        Login.login.show()

        if not app.exec_():
            print 'push exit button'


