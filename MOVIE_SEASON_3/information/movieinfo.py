# -*- coding: utf-8 -*-

import copy

# Moive Impormation
class MovieInfo():
	__movie_room = None # 상영관 번호.
    	__movie_name = None # 영화 이름.
    	__movie_times = None # 상영시간.
	__movie_seats = [] # 상영시간에 따른 좌석 정보.
	__movie_total = 0 # 영화에 대한 총 수입.

	__seat = {} # 각 좌석에 대한 정보.

	# 생성자 define
	def __init__(self, r, n, t):
		for i in range(ord('A'), ord('F')):
			for j in range(1, 6): self.__seat[(chr(i), j)] = 0

	 	self.__movie_room, self.__movie_name, self.__movie_times  = r, n, t

		# 여기서 TotalSeat을 초기화 해주지 않으면 그전값이 저장되어있다. why?
			# Maybe I think, Each Objects are the same?
	      # 안 하였을 때 길이를 측정하면 각각 4, 4가 나오고 초기화하면 3, 1로 정상적으로 나온다.
		self.__movie_seats = []
		self.__movie_times.sort()
	 	# 각 상영시간에 해당하는 좌석 정보를 저장할 딕셔너리 선언
	      # copy로 딕셔너리를 복사해주어야 각각에 해당하는 좌석 예매 정보를 가질 수 있다.
		for i in range(len(self.__movie_times)): 
			self.__movie_seats.append(self.__seat.copy())


	def get_movie_room(self) : return self.__movie_room
	def get_movie_name(self) : return self.__movie_name
	def get_movie_times(self) : return self.__movie_times
	def get_movie_seats(self) : return self.__movie_seats
	def get_movie_total(self) : return self.__movie_total

	def set_movie_copy(self, time) :
		print "set_movie_copy"
		for i in range(ord('A'), ord('F')) :
			for j in range(1, 6) : 
				self.__seat[(chr(i), j)] = 0

		for i in range(len(time)) :
			self.__movie_times.append(time[i])
			self.__movie_times.sort()
			home = self.__movie_times.index(time[i])
			self.__movie_seats.insert(home, self.__seat.copy())

	def set_movie_room(self, r) : self.__movie_room = r
	def set_movie_name(self, n) : self.__movie_name = n
	def set_movie_time(self, i, t) : self.__movie_times[i] = t
	def set_movie_times(self, t) : self.__movie_times = t
	def set_movie_total(self, t) : self.__movie_total += t
	