# -*- coding: utf-8 -*-

import user
# import PyQt5 module.
from PyQt5.QtWidgets import QDialog, QMessageBox


class Edit(QDialog):
    def __init__(self, socket, administration):
        QDialog.__init__(self)
        Edit.socket = socket
        Edit.administration = administration
        self.movie = user.get_movies()
        self.movie_index = None
        self.time_index = None

    def set(self):
        Edit.edit.ui.lineEdit.textChanged['QString'].connect(self.location)

    def time(self, action):
        self.ui.lineEdit_3.setText(action.text())
        self.time_index = action.listWidget().row(action)

    def location(self):
        self.ui.lineEdit_2.setText('None')
        for i in range(len(self.movie)):
            if self.movie[i].get_movie_name() == self.ui.lineEdit.text():
                self.movie_index = i
                self.ui.lineEdit_2.setText(str(self.movie[i].get_movie_room()))
                time = self.movie[i].get_movie_times()
                self.ui.listWidget.addItems(time)
                for j in range(len(time)):
                    self.ui.listWidget.item(j).setText(time[j])
                break

    def btn_edit_action(self):
        print self.ui.lineEdit.text()
        print self.ui.lineEdit_2.text()
        print self.ui.lineEdit_3.text()
        Edit.socket.send_message(Edit.socket.client_socket, 'CLIENT_MOVIE_CHANGE# %d# %d# %s'
                                 % (self.movie_index, self.time_index, self.ui.lineEdit_3.text()))
        message = Edit.socket.recv_message(Edit.socket.client_socket)
        Edit.socket.send_message(Edit.socket.client_socket, 'MOVIE_INFO_READY')
        user.set_movies(Edit.socket.socket_connect_file())
        if message[0] == 'SUCCESS':
            if QMessageBox.question(Edit.edit, 'Close', 'success edit movie', QMessageBox.Yes) == QMessageBox.Yes:
                Edit.administration.load_movies()
                self.close()

    def btn_cancel_action(self):
        self.close()
