# -*- coding: utf8 -*-

import user
# import PyQt5 module.
from PyQt5.QtWidgets import QDialog, QMessageBox


class Insert(QDialog):
    def __init__(self, socket, administration):
        QDialog.__init__(self)
        Insert.socket = socket
        Insert.administration = administration
        self.movie_index = None

    def set(self):
        Insert.insert.ui.lineEdit.textChanged['QString'].connect(self.location)

    def location(self):
        movie = user.get_movies()
        for i in range(len(movie)):
            if movie[i].get_movie_name() == self.ui.lineEdit.text():
                self.movie_index = i
                self.ui.lineEdit_2.setEnabled(False)
                self.ui.lineEdit_2.setText(str(movie[i].get_movie_room()))
                break
            else:
                self.ui.lineEdit_2.setEnabled(True)
                self.ui.lineEdit_2.clear()

    def btn_ok_action(self):
        command = None
        if self.movie_index is None:
            command = 'CLIENT_MOVIE_ADD# %s# %s# %s'% (self.ui.lineEdit_2.text(), self.ui.lineEdit.text(), self.ui.lineEdit_3.text())
        else:
            command = 'CLIENT_MOVIE_ADD# %d# %s' % (self.movie_index, self.ui.lineEdit_3.text())

        Insert.socket.send_message(Insert.socket.client_socket, command)
        message = Insert.socket.recv_message(Insert.socket.client_socket)
        Insert.socket.send_message(Insert.socket.client_socket, 'MOVIE_INFO_READY')
        user.set_movies(Insert.socket.socket_connect_file())
        if message[0] == 'SUCCESS':
            if QMessageBox.question(Insert.insert, 'Question', 'Insert Success', QMessageBox.Yes) == QMessageBox.Yes:
                self.close()
            Insert.administration.load_movies()

    def btn_cancel_action(self):
        result = QMessageBox.question(Insert.insert, 'Question', 'Are you sure to cancel?',
                                      QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.close()
