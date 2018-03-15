# -*- coding:utf-8 -*-

def check_choice(ob, *arr) :

	max_number = None
	message = "what can I help you with\n >> "

	while True :
		try :
			if ob == "menu()" :
				if arr[0] == "0" :
					max_number = 5
				elif arr[0] == "1" :
					max_number = 3

			elif ob == "check_movie_amend()" :
				message = "movie nunber  >> "
				max_number = arr[0]

			elif ob == "management_menu()" :
				max_number = 4

			elif ob == "print_movie()" :
				message = "movie nunber  >> "
				max_number = arr[0]

			ch = input(message)

			if ch < 1 or ch > max_number :
				raise Exception("")

		except Exception, TypeError :
			print "\n★ ★ ★ what? 다시 선택해 주세요 ★ ★ ★\n\n"
			continue
			
		else :
			if ob == "print_movie()" or ob == "check_movie_amend()" :
				return ch-1
			return ch

def check_movie_add(movies) :

	name, movie_index, number, times = None, None, None, None

	while True :
		try :
			name = raw_input(" + name : ")
			for i in range(len(movies)) :
				if movies[i].get_movie_name() == name :
					movie_index = i

			times = raw_input(" + time : ")

			if movie_index == None :
				number = input(" + number : ")
				print "반환할거야"
				return number, name, times

			else : 
				return movie_index, times

		except TypeError, Exception :
			print "\n★ ★ ★ what? 다시 선택해 주세요 ★ ★ ★\n\n"
			continue

def check_movie_amend(index, movies) :
	print "\n- - - - - - - - - - - - - - - - - - "
	print "\n - name : ", movies[index].get_movie_name()
	print " - number : ", movies[index].get_movie_room()
	print " - times\n   ",
	print movies[index].get_movie_times()
	print "\n- - - - - - - - - - - - - - - - - - "

	while True :
		try :
			time_choice = raw_input("선택할 시간 >> ")
			before_time_index = movies[index].get_movie_times().index(time_choice)
			after_time = raw_input("변경할 시간 >> ")
			return str(before_time_index), after_time

		except Exception, TypeError :
			print "\n★ ★ ★ what? 다시 선택해 주세요 ★ ★ ★\n\n"
			continue

def check_time(movie) :
	print "\n- - - - 시간을 선택해주세요 - - - - \n"
   	print movie.get_movie_times()
   	print "- - - - - - - - - - - - - - - - - - "

   	while True :
   		try : 
   			time = raw_input(" time >> ")
   			time_index = movie.get_movie_times().index(time)
   			return time_index

   		except Exception, TypeError :
   			print "\n★ ★ ★ what? 다시 선택해 주세요 ★ ★ ★\n\n"
   			continue

def check_count(sale) :

	count, total = None, None

	while True :
		print "\n- - - - 관람 인원을 선택하세요 - - - -\n"
		try :
			adult = input("성인 : ")
			teenager  = input("청소년 : ")
			children = input("어린이 : ")

			count = adult+teenager+children
			total = adult*8000 + teenager*7000 + children*4000

			if sale == "Yes" :
				total *= 0.7
				total = int(total)			

			return count, total

		except Exception, TypeError :
			print "\n★ ★ ★ what? 다시 선택해 주세요 ★ ★ ★\n\n"
   			continue

def check_pay(total) :

	while True :
		try :
			print "\n총 결제 금액은 ", str(total), "원 입니다."
			pay_choice = raw_input("결제 하시겠습니까? (y/n) : ")
			if pay_choice == "y" :
				return  True
			elif pay_choice == "n" : 
				return False
			else : 
				raise Exception

		except Exception, TypeError :
			print "\n★ ★ ★ what? 다시 선택해 주세요 ★ ★ ★\n\n"
			continue

def check_seats(count, seat) :

	seats = None

	while True :
		try : 
			print "\n- - - - 좌석을 선택해 주세요 - - - -\n"
			print "좌석을 ,로 구분해주세요. [ex] A1, A2, A3"
			seats = raw_input(" >> ")
			seats_temp = seats.split(", ")

			if len(seats_temp) != count : 
				print "len error"
				raise Exception
				
			else : 
				result = True
				for i in range(count) :
					string = seats_temp[i]
					if seat.get((string[0], int(string[1]))) == 1 :
						print "\n이미 예약된 좌석 입니다. 다른 좌석을 선택해주세요."
						result = None
						break

				if result :
					return seats
				elif not result :
					continue

		except Exception as e:
			print e
			print "\n★ ★ ★ what? 다시 선택해 주세요 ★ ★ ★\n\n"
			continue

