# -*- coding: utf8 -*-

import user
import urllib2

# import PyQt5 module.
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap


class Reservation(QMainWindow):
    def __init__(self, socket, before_page):
        QMainWindow.__init__(self)
        Reservation.socket = socket
        Reservation.before_page = before_page
        Reservation.reservation = self
        self.count = 0
        self.all_seat = []
        self.movie_row = None
        self.time_row = None

        # Make Reservation Method

    @staticmethod
    def load_movies():
        movies = user.get_movies()
        for i in range(len(movies)):
            Reservation.reservation.ui.list_movie.addItem(movies[i].get_movie_name())
            Reservation.reservation.ui.list_movie.item(i).setText(movies[i].get_movie_name())
            # print Reservation.reservation.ui.list_movie.item(i).text()

        Reservation.reservation.ui.frame_time.setVisible(False)
        Reservation.reservation.ui.frame_seats.setVisible(False)
        Reservation.reservation.ui.frame_count.setVisible(False)
        Reservation.reservation.ui.frame_info.setVisible(False)
        Reservation.reservation.ui.frame_movie.setVisible(False)

    def btn_ok_action(self):
        result_message = None
        Reservation.socket.send_message(Reservation.socket.client_socket, 'CLIENT_MOVIE_CHOICE# %d# %d# %s# %s'
                                        % (self.movie_row, self.time_row, self.ui.label_total_money.text(), self.ui.label_seats.text()))
        message = Reservation.socket.recv_message(Reservation.socket.client_socket)
        print 'message > ', message
        Reservation.socket.send_message(Reservation.socket.client_socket, 'MOVIE_INFO_READY')
        user.set_movies(Reservation.socket.socket_connect_file())
        if message[0] == 'SUCCESS':
            result_message = 'success reservation\n number : %s' % message[2]
        elif message[0] == 'ERROR':
            result_message = 'fail reservation, try again'
        result = QMessageBox.question(Reservation.reservation, "Confirm Exit", result_message, QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            self.btn_re_action()

    def btn_exit_action(self):
        result = QMessageBox.question(Reservation.reservation, "Confirm Exit...", 'Are you sure you want to exit?',
                                      QMessageBox.Yes | QMessageBox.No)

        if result == QMessageBox.Yes:
            self.close()
            Reservation.before_page.show()

    def btn_re_action(self):
        self.count = 0
        self.all_seat = []
        self.ui.label_seats.setText('plz chose seat')
        self.ui.sbox_adult.setValue(0)
        self.ui.sbox_teenager.setValue(0)
        self.ui.sbox_child.setValue(0)
        self.ui.label_movieposter.setText("movie Poster")
        self.ui.label_info.setText("movie Info")

        self.ui.frame_count.setVisible(False)
        self.ui.frame_movie.setVisible(False)
        self.ui.frame_time.setVisible(False)

        # 실제로 만들 때는 얘들을 리스트로 만들어서 하나씩 호출해서 정의하는 함수로 만들면 좋을 것 같음.
        # 아니면 배열 이름 리스트로 저장하니까 튜플로 묶어서 { 배열이름 : 변수 } 로 저장해서 해당하는 애들만 setChecked(False) 해줘도 될 것 같고.
        cbox = [self.ui.cbox_A1, self.ui.cbox_A2, self.ui.cbox_A3, self.ui.cbox_A4, self.ui.cbox_A5,
                     self.ui.cbox_B1,  self.ui.cbox_B2, self.ui.cbox_B3, self.ui.cbox_B4, self.ui.cbox_B5,
                     self.ui.cbox_C1, self.ui.cbox_C2, self.ui.cbox_C3, self.ui.cbox_C4, self.ui.cbox_C5,
                     self.ui.cbox_D1, self.ui.cbox_D2, self.ui.cbox_D3, self.ui.cbox_D4, self.ui.cbox_D5,
                     self.ui.cbox_E1, self.ui.cbox_E2, self.ui.cbox_E3, self.ui.cbox_E4, self.ui.cbox_E5]

        for i in range(len(cbox)):
            cbox[i].setChecked(False)

    def list_time_action(self, action):
        self.time_row = action.row()
        seats = user.get_movie_seats(self.movie_row, self.time_row)

        cbox = {('A', 1): self.ui.cbox_A1, ('A', 2): self.ui.cbox_A2, ('A', 3): self.ui.cbox_A3, ('A', 4): self.ui.cbox_A4, ('A', 5): self.ui.cbox_A5,
                ('B', 1): self.ui.cbox_B1, ('B', 2): self.ui.cbox_B2, ('B', 3):self.ui.cbox_B3, ('B', 4): self.ui.cbox_B4, ('B', 5): self.ui.cbox_B5,
                ('C', 1): self.ui.cbox_C1, ('C', 2): self.ui.cbox_C2, ('C', 3):self.ui.cbox_C3, ('C', 4): self.ui.cbox_C4, ('C', 5): self.ui.cbox_C5,
                ('D', 1): self.ui.cbox_D1, ('D', 2): self.ui.cbox_D2, ('D', 3):self.ui.cbox_D3, ('D', 4): self.ui.cbox_D4, ('D', 5): self.ui.cbox_D5,
                ('E', 1): self.ui.cbox_E1, ('E', 2): self.ui.cbox_E2, ('E', 3):self.ui.cbox_E3, ('E', 4): self.ui.cbox_E4, ('E', 5): self.ui.cbox_E5}

        #  딕셔너리로 저장해서 확인해서 1인이면 enabled 주면 되긴한데.. 귀찮....
        for i in range(ord('A'), ord('F')):
            for j in range(1, 6):
                if seats[(chr(i), j)] == 1:
                    cbox[(chr(i), j)].setCheckState(1)
                    cbox[(chr(i), j)].setEnabled(False)

        self.ui.frame_count.setVisible(True)
        self.ui.frame_movie.setVisible(True)

    def list_movie_action(self, action):
        self.btn_re_action()
        self.movie_row = action.row()
        movie_times = user.get_movies()[action.row()].get_movie_times()
        Reservation.reservation.ui.list_time.clear()
        for j in range(len(movie_times)):
            Reservation.reservation.ui.list_time.addItem(movie_times[j])
            Reservation.reservation.ui.list_time.item(j).setText(movie_times[j])

        self.ui.label_info.setText(user.get_movies()[action.row()].get_movie_name())
        # link image from url
        img_file = urllib2.urlopen(
            'https://cdn.pixabay.com/photo/2016/03/21/15/10/marilyn-monroe-1270659_960_720.png').read()
        # make a QPixmap value
        img_pix = QPixmap()
        # load Image data from url, get data
        img_pix.loadFromData(img_file)
        self.ui.label_movieposter.setPixmap(img_pix.scaled(210, 300))

        self.ui.label_movie_name.setText(user.get_movies()[action.row()].get_movie_name())
        self.ui.frame_time.setVisible(True)

    def total_is(self):
        self.ui.label_total_count.setText(str(self.ui.sbox_adult.value() + self.ui.sbox_teenager.value() + self.ui.sbox_child.value()))
        self.ui.label_m_adult.setText(str(8000*self.ui.sbox_adult.value()))
        self.ui.label_m_teenager.setText(str(7000 * self.ui.sbox_teenager.value()))
        self.ui.label_m_child.setText(str(4000 * self.ui.sbox_child.value()))
        self.ui.label_total_money.setText(str(int(self.ui.label_m_adult.text())+int(self.ui.label_m_teenager.text())+int(self.ui.label_m_child.text())))

        if int(self.ui.label_total_count.text()) > 0:
            self.ui.frame_seats.setVisible(True)
            self.ui.frame_info.setVisible(True)
        else:
            self.ui.frame_seats.setVisible(False)
            self.ui.frame_info.setVisible(False)

    def select_seats(self):
        string_seat = ''
        if self.sender().isChecked():
            if self.count != int(self.ui.label_total_count.text()):
                self.all_seat.append(self.sender().text())
                for i in range(len(self.all_seat)):
                    if i == 0:
                        string_seat += self.all_seat[i]
                    else:
                        string_seat += (', '+self.all_seat[i])
                self.ui.label_seats.setText(string_seat)
                self.count += 1
            else:
                self.btn_re_action()
        else:
            self.count -= 1
            self.all_seat.remove(self.sender().text())
            if len(self.all_seat) != 0:
                for i in range(len(self.all_seat)):
                    if i == 0:
                        string_seat += self.all_seat[i]
                    else:
                        string_seat += (', ' + self.all_seat[i])
                self.ui.label_seats.setText(string_seat)
            else:
                self.ui.label_seats.setText('plz chose seat')
