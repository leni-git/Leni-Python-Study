# -*- conding: utf-8 -*-

# import shutil, pickle

# import socket module.
from socket import *


# Socket information
class SocketInfo:
	def __init__(self):
		pass

	__HOST = ''
	__PORT = 36789
	__FPORT = 46789
	__BUFSIZE = 1024
	__ADDR = (__HOST, __PORT)
	__FADDR = (__HOST, __FPORT)

	def get_port(self):
		return self.__PORT
	def get_addr(self):
		return self.__ADDR
	def get_faddr(self):
		return self.__FADDR
	def get_bufsize(self):
		return self.__BUFSIZE

	def set_host(self, h):
		self.__HOST=h