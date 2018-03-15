# -*- conding: utf-8 -*-

# import shutil, pickle

# import socket module.
from socket import *

# Custom Package import
from aes128_message import AES128_HMAC_Encrypt, AES128_HMAC_Decrypt
import binascii
import pickle


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
        self.__HOST = h


class ClientSocket:
    def __init__(self):
        # make message connection socket and try to connect server socket.
        ClientSocket.__KEY = 'password123qwe'
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        try:
            self.client_socket.connect(SocketInfo().get_addr())
            print 'Connect SERVER (%s:%s)' % SocketInfo().get_addr()
        except Exception as e:
            print 'Can\'t connect SERVER (%s:%s)' % SocketInfo().get_addr()
            print 'Error > ', e
            # ADD [ PAGE ] dialog retry or exit.

    def socket_connect_file(self):
        file_socket = socket(AF_INET, SOCK_STREAM)
        file_socket.connect(SocketInfo().get_faddr())

        try:
            __FILE_SIZE = self.recv_message(file_socket)
            self.send_message(file_socket, 'MOVIE_SIZE_READY')

            movies = self.recv_message(file_socket, 'data_message', int(__FILE_SIZE[0]))
            movies = pickle.loads(movies)
            #self.send_message(self.client_socket, 'CLIENT_START_READY')
            #message = ClientSocket.recv_message(ClientSocket.client_socket)
            #if message == 'MOVIE_SYSTEM_START':
            return movies
        except Exception as e:
            print 'Error > ', e, ' File receive error'
        # ADD [ MESSAGE ] if fail, have to send this message and will retry.
        # ClientSocket.send_message(self.client_socket, 'CLIENT_START_ERROR')
        # return 'fail'
        finally:
            file_socket.close()

    @staticmethod
    def recv_message(sock, *arr):
        if len(arr) != 0:
            if arr[0] == 'data_message':
                # receive data message.
                temp = sock.recv(arr[1])
                client_message = AES128_HMAC_Decrypt(ClientSocket.__KEY,
                                                     binascii.unhexlify(temp[:32]), binascii.unhexlify(temp[32:]))
                return client_message

        else:
            # receive command message.
            temp = sock.recv(SocketInfo().get_bufsize())
            client_message = AES128_HMAC_Decrypt(ClientSocket.__KEY,
                                                 binascii.unhexlify(temp[:32]), binascii.unhexlify(temp[32:]))
            print 'server_message > ', client_message
            return client_message.split('# ')

    @staticmethod
    def send_message(sock, command):
        print 'send command > ', command
        command = AES128_HMAC_Encrypt(ClientSocket.__KEY, command)
        sock.send(command)

    def close(self):
        self.client_socket.close()
