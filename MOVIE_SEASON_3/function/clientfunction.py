# -*- coding: utf-8 -*-

from print_file import *
from errorcheck import *

class Client_Function():

	def movie_system_start(self, g, movies, sale) :

		while True :
			choice = check_choice(menu(g), g)
			print str(choice)
			
			if choice == 3 :
				if g == "1" : return 0
				while True : 
					management_choice = check_choice(management_menu())

					if management_choice == 4 : 
						break
					# Movie add - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
					if management_choice == 1 :
						print "- - - - - - - - - - - - - - - - - - "
						movie_add = check_movie_add(movies)
						if len(movie_add) == 2 :
							return choice, management_choice, movie_add[0], movie_add[1]
						elif  len(movie_add) == 3 :
							print "추가하는 부분 clientfunction"
							return choice, management_choice, movie_add[0], movie_add[1], movie_add[2]

					else :
						if len(movies) == 0 : 
							print """\n- - - 상영중인 영화가 없습니다 - - -\n죄송죄송 돌아가주세요 영화가 부족해요 티티\n\n\n"""

						else :
							# Movie amend - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
							print "- - - - - - - - - - - - - - - - - - "
							if management_choice == 2 :
								print "\n수정을 원하시는 영화를 선택해주세요.\n영화 상영시간만 수정하실 수 있습니다.\n"
								movie_index = check_choice(print_movie("check_movie_amend()", movies), len(movies))
								movie_amend = check_movie_amend(movie_index, movies)
								return choice, management_choice, movie_index, movie_amend[0], movie_amend[1]

							# Movie delete - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
							elif management_choice == 3:
								print "\n삭제를 원하시는 영화를 선택해주세요.\n영화 시간만 삭제하실 수 없습니다.\n"
								movie_index= check_choice(print_movie("check_movie_amend()", movies), len(movies))
								return choice, management_choice, movie_index
			elif choice == 5 :
				return 0

			else :
				if len(movies) == 0 :
					print """\n- - - 상영중인 영화가 없습니다 - - -\n죄송죄송 돌아가주세요 영화가 부족해요 티티\n\n\n"""

				else :
					if choice == 4 :
						print "\n- - - - 영화 총 수입 입니다 - - - -"
						result = 0
						for i in range(len(movies)):
							print "  \"%-10s\" ic : %10d won" % (movies[i].get_movie_name(), movies[i].get_movie_total())
							result += movies[i].get_movie_total()
						print "- - - - - - - - - - - - - - - - - -"
						print "     Total >> ", str(result)
						print "- - - - - - - - - - - - - - - - - -"

					else :
						movie_index = check_choice(print_movie("print_movie()", movies), len(movies))
						time_index = check_time(movies[movie_index])

						if choice == 2 :
							print_seat(movies[movie_index].get_movie_seats()[time_index])

						elif choice == 1 :
							count, total = check_count(sale)
							print_seat(movies[movie_index].get_movie_seats()[time_index])
							seats = check_seats(count, movies[movie_index].get_movie_seats()[time_index])
							if check_pay(total) :
								return choice, movie_index, time_index, total, seats
							else :
								print "\nMenu 화면으로 돌아갑니다.\n"
