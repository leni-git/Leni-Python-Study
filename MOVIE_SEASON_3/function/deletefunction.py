# -*- coding: utf-8 -*-

import user
from PyQt5.QtWidgets import QDialog, QMessageBox


class Delete(QDialog):
    def __init__(self, socket, administration):
        QDialog.__init__(self)
        Delete.socket = socket
        Delete.administration = administration

    def delete_btn(self):
        button = self.sender().text()
        if button == 'YES':
            movie = user.get_movies()
            movie_name = Delete.delete.ui.lineEdit.text()
            for i in range(len(movie)):
                if movie[i].get_movie_name() == movie_name:
                    Delete.socket.send_message(Delete.socket.client_socket, 'CLIENT_MOVIE_DEL# %d' % i)
                    message = Delete.socket.recv_message(Delete.socket.client_socket)
                    Delete.socket.send_message(Delete.socket.client_socket, 'MOVIE_INFO_READY')
                    user.set_movies(Delete.socket.socket_connect_file())
                    if message[0] == 'SUCCESS':
                        if QMessageBox.question(Delete.delete, 'Close', 'success delete movie',
                                                QMessageBox.Yes) == QMessageBox.Yes:
                            Delete.administration.load_movies()
                            self.close()

