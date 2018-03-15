# -*- coding: utf-8 -*-

class PersonInfo():
	__person_id = None
	__person_pw = None
	__person_name = None
	__person_grade = None
	__person_ad_agree = None

	def __init__(self, *arr): 
		if len(arr)==5 :
			self.__person_id, self.__person_pw, self.__person_name, self.__person_grade = arr[0], arr[1], arr[2], arr[3]
			self.__person_ad_agree = arr[4]
		else : pass


	def get_person_id(self): return self.__person_id
	def get_person_pw(self): return self.__person_pw
	def get_person_name(self): return self.__person_name
	def get_person_grade(self): return self.__person_grade
	def get_person_ad_agree(self): return self.__person_ad_agree

	def set_person_id(self, i): self.__person_id = i
	def set_person_pw(self, p): self.__person_pw = p
	def set_person_name(self, n): self.__person_name = n
	def set_person_grade(self, g): self.__person_grade = g
	def set_person_ad_agree(self, a): self.__person_ad_agree = a