# -*- coding: utf8 -*-

import user
# import PyQt5 module.
from PyQt5.QtWidgets import QMainWindow, QFrame, QMessageBox

from uifile.uiMovieList import Ui_Form

from insertfunction import Insert
from uifile.uiInsert import Ui_Insert
from editfunction import Edit
from uifile.uiEdit import Ui_Edit_Dialog
from deletefunction import Delete
from uifile.uiDelete import Ui_Dialog


class Administration(QMainWindow):
    def __init__(self, socket, employee):
        QMainWindow.__init__(self)
        Administration.socket = socket
        Administration.employee = employee

    @staticmethod
    def load_movies():
        # How to delete.
        if Administration.administration.ui.movielist.count() != 0:
            for i in range(Administration.administration.ui.movielist.count()):
                Administration.administration.ui.movielist.takeAt(0)

        movies = user.get_movies()
        for i in range(len(movies)):
            wid = Administration.movie_form(movies[i])
            Administration.administration.ui.movielist.addWidget(wid)

        print Administration.administration.ui.movielist.count()
        Administration.administration.ui.scrollAreaWidgetContents.setLayout(Administration.administration.ui.movielist)

    @staticmethod
    def movie_form(movie):
        temp = QFrame()
        temp.ui = Ui_Form()
        temp.ui.setupUi(temp)
        temp.ui.moviename.setText(movie.get_movie_name())
        temp.ui.label_2.setText(str(movie.get_movie_room()))
        temp.ui.label_3.setText(str(movie.get_movie_times()))
        return temp

    def closeEvent(self, event):
        print 'close Administration'
        result = QMessageBox.question(Administration.administration, 'Confirm Exit...', 'Are you sure you want to exit?',
                                      QMessageBox.Yes | QMessageBox.No)

        if result == QMessageBox.Yes:
            self.close()
            Administration.employee.show()

    def administration_btn_action(self):
        button = self.sender().text()

        if button == "Insert":
            Insert.insert = Insert(Administration.socket, self)
            Insert.insert.ui = Ui_Insert()
            Insert.insert.ui.setupUi(Insert.insert)
            Insert.insert.set()
            Insert.insert.show()

        elif button == "Edit":
            Edit.edit = Edit(Administration.socket, self)
            Edit.edit.ui = Ui_Edit_Dialog()
            Edit.edit.ui.setupUi(Edit.edit)
            Edit.edit.set()
            Edit.edit.show()

        elif button == "Delete":
            Delete.delete = Delete(Administration.socket, self)
            Delete.delete.ui = Ui_Dialog()
            Delete.delete.ui.setupUi(Delete.delete)
            Delete.delete.show()
