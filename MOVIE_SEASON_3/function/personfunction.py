# -*- coding: utf-8 -*-
import pickle, xmltodict, ssl
from datetime import datetime
from urllib2 import Request, urlopen

class Person_Function():

	f = None
	persons = None
	sale = "Noop"

	def __init__(self): 
		self.persons = self.read_person_info()

		# try: 
		# 	self.f = open("documents/SERVER_PERSON_INFO.txt", "rb")
		# 	self.persons = pickle.load(self.f)
		# except Exception as e : 
		# 	self.f = open("documents/SERVER_PERSON_INFO.txt", "wb")
		# 	pickle.dump([], self.f)
		# finally : 
		# 	self.f.close()

	# File Read
	def read_person_info(self) :
		try: 
		 	self.f = open("documents/SERVER_PERSON_INFO.txt", "rb")
		 	return pickle.load(self.f)
		except: 
			self.f = open("documents/SERVER_PERSON_INFO.txt", "wb")
		 	pickle.dump([], self.f)
			print "ERROR : Can't read person info"
		finally : 
			self.f.close()

	# File Backup
	def backup_person_info(self):
		shutil.copy2("documents/SERVER_PERSON_INFO.txt", "documents/SERVER_PERSON_INFO_BACKUP.txt")

	def check_person_info(self, ii, p):

		for i in range(len(self.persons)):
			if self.persons[i].get_person_id() == ii:
				print self.persons[i].get_person_id()
				person_i = i

		if self.persons[person_i].get_person_pw() == p:
			print self.persons[person_i].get_person_pw()

			# Client에 해당하는 지역을 불러와서 평균적인 강수량을 얻어온다 - - - - - - - - - - - - - - - - - - - - - -
			location = 159
			url = 'https://data.kma.go.kr/OPEN_API/SYNM/2017/08/XML/stndays_'+str(location)+'.xml'
			#url = 'https://data.kma.go.kr/OPEN_API/SYNM/2017/08/XML/stndays_159.xml'
			#print url
			request = Request(url)
			request.get_method = lambda: 'GET'

                	# 16, 17번 문장이 의미하는 바 알아오기.
                	gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
                	response_body = urlopen(request, context=gcontext).read()

                	response_data = response_body.decode('utf-8', 'ignore').encode('utf-8')
                	python_data = xmltodict.parse(response_data)['stndays']['info']

                	average = float(python_data[-1]['rn_day']) / (len(python_data)-4)
                	try :
                		today = float(python_data[datetime.today().day-1]['rn_day'])
                	except :
                		today = 0.0

          		if today > average :
          			print "today is big"
          			self.sale = "Yes"

                	return self.persons[person_i].get_person_grade(), self.persons[person_i].get_person_name(), self.persons[person_i].get_person_ad_agree(), self.sale

           	return -1, -1, -1, -1