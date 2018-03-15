# -*- coding: utf-8 -*-

import pickle

class Movie_Function():

	__f = None
	__movies = None

	def __init__(self):
		self.__movies = self.read_movie_info()
		# try: 
		# 	self.f = open("documents/SERVER_MOVIE_LIST.txt", "rb")
		# 	self.movies = pickle.load(self.f)
		# except Exception as e : 
		# 	self.f = open("documents/SERVER_MOVIE_LIST.txt", "wb")
		# 	print "ERROR skdafjsaidrj"
		# 	pickle.dump([], self.f)		
		# finally : 
		# 	self.f.close()

	# File Read
	def read_movie_info(self) :
		try: 
			self.__f = open("documents/SERVER_MOVIE_LIST.txt", "rb")
			return pickle.load(self.__f)
		except: 
			self.__f = open("documents/SERVER_MOVIE_LIST.txt", "wb")
		 	pickle.dump([], self.__f)	
			print "ERROR : Can not read movie info"
		finally : 
			self.__f.close()

	def write_movie_info(self) :
		try :
			self.__f = open("documents/SERVER_MOVIE_LIST.txt", "wb")
			pickle.dump(self.__movies, self.__f)
			self.__f.close()
			
		except Exception as e :
			print e
			print "ERROR : Can not write_movie_info"

			
	# File Backup
	def backup_movie_info(self):
		shutil.copy2("documents/SERVER_MOVIE_LIST.txt", "documents/SERVER_MOVIE_LIST_BACKUP.txt")

	def get_movies(self) : return self.__movies
	
	# Movie Time Add
	def movie_add_times(self, movie_index, times) :
		try :
			self.__movies[movie_index].set_movie_copy(times)
			self.write_movie_info()
			return True

		except Exception as e :
			print e
			return None

	def movie_choice(self, movies, movie_index, time_index, total, seats):
		print "영화 예매해야 합니다."
		try :
			for i in range(len(seats)) :
				string = seats[i]
				if self.__movies[movie_index].get_movie_seats()[time_index][(string[0], int(string[1]))] == 1 :
					return None

			for i in range(len(seats)) :
				string = seats[i]
				self.__movies[movie_index].get_movie_seats()[time_index][(string[0], int(string[1]))] = 1 

			self.__movies[movie_index].set_movie_total(total)
			self.write_movie_info()
			return True

		except Exception as e :
			print e
			return None

	def movie_add(self, movie) :
		try :
			self.__movies.append(movie)
			self.write_movie_info()
			return True
		except Exception as e:
			print e
			return None
		

	def movie_amend(self, movie_index, time_index, time) :
		try :
			self.__movies[movie_index].set_movie_time(time_index, time)
			self.write_movie_info()
			return True
		except Exception as e:
			print e
			return None

		

	def movie_del(self, movie_index) :
		try :
			print "movie_del : ", str(movie_index)
			del self.__movies[movie_index]
			self.write_movie_info()
			return True
		except Exception as e:
			return None