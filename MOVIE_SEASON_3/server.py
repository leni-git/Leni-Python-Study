# -*- coding: utf-8 -*-

# import random, time modules
# It's used to loading today.
import random
from time import ctime
# import socket, select module
# select module can multi sockets connection.
from socket import *
from select import *

# Custom Package import.
from pub import *
from aes128_message import *
# Information Package import.
from information.movieinfo import *
from information.socketinfo import *
from information.personinfo import *
# Function Package import.
from function.moviefunction import *
from function.personfunction import *

# import sys module
# It used to exit server.
import sys
# import os module
# It used to send file size.
import os

# file_create.txt

# function  Module value define
movie_function = Movie_Function()
person_function = Person_Function()
mosquitto = Paho_Mqtt()

# basic values.
# key = value for decryption and encryption.
key = 'password123qwe'
# name_topic = value for .. I don't know
# name_topic = None


# basic methods.
# recv_message(csock): Will decrypt 'temp' and return string type message list after decoding.
def recv_message(csock):
    try:
        temp = csock.recv(SocketInfo().get_bufsize())
        client_message = AES128_HMAC_Decrypt(key, binascii.unhexlify(temp[:32]), binascii.unhexlify(temp[32:]))
        return client_message.split("# ")
    except Exception as e:
        print 'Error > ', e


# send_message(csock, server_commend): Will encrypt 'server_command' and send 'server_message'.
def send_message(csock, server_command):
    server_message = AES128_HMAC_Encrypt(key, server_command)
    csock.send(server_message)


# make 'server_socket' object -> binding -> waiting for connect other client sockets.
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(SocketInfo().get_addr())
server_socket.listen(10)
# make 'file_socket' object -> binding -> waiting for connect other client file sockets.
file_socket = socket(AF_INET, SOCK_STREAM)
file_socket.bind(SocketInfo().get_faddr())
file_socket.listen(10)
# make 'connection list'
connection_list = [server_socket, file_socket]

# start ROOF
# It's server's functions.
# Server doesn't have any GUI.
# start Server
print '영화 서버를 시작합니다. %s 포트로 접속을 기다립니다.' % str(SocketInfo().get_port())
while connection_list:
    try:
        print "INFO : waiting for connection..."

        # select 로 요청을 받고, 10 초 마다 블럭킹을 해제하도록 함
        read_socket, write_socket, error_socket = select(connection_list, [], [], 10)

        for sock in read_socket:
            # 새로운 접속, 연결을 막 시작하였을 때 server가 해야하는 동작을 서술한다.
            if sock == server_socket:
                client_socket, addr_info = server_socket.accept()
                connection_list.append(client_socket)
                print "INFO : [%s] 클라이언트(%s)가 새롭게 연결 되었습니다." % (ctime(), addr_info[0])

                # 서버소켓이 아닌 경우 Login을 하라는 message를 전송한다.
                if connection_list[-1] != server_socket: 
                    send_message(connection_list[-1], "LOGIN")

                print "connect data to > ", addr_info

            # File 전송을 요청하는 socket 연결 시 동작한다.
            elif sock == file_socket :
                if message[0] == "MOVIE_INFO_READY" :

                        size = os.path.getsize("documents/SERVER_MOVIE_LIST.txt")
                        if size % 16 != 0 :
                            size += (16 - size % 16)
                        # iv의 길이를 추가한 뒤에 전체길이를 2배 늘려준다.
                        size += 32
                        size = size*2
                        print "size : %d" % size

                        fsock, faddr_info = file_socket.accept()
                        send_message(fsock, str(size))

                        fock_message = recv_message(fsock)

                        if fock_message[0] == "MOVIE_SIZE_READY" :
                            with open("documents/SERVER_MOVIE_LIST.txt") as file:
                                send_message(fsock, file.read())

                        fsock.close()

            # If a client socket is not first connection, this function will work.
            else:
                message = recv_message(sock)

                if message:
                    print "INFO : [%s] 클라이언트로부터 전달 받았습니다." % ctime()
                    
                    if message[0] == "LOGIN_CLIENT":
                        print 'LOGIN START'
                        g, n, a, s = person_function.check_person_info(message[1], message[2])

                        if g == -1 and n == -1:
                            send_message(sock, "LOGIN")
                        else:
                            send_message(sock, "MOVIE_INFO# %s# %s# %s# %s" % (g, n, a, s))

                    # It doesn't use Client_ui file.
                    # elif message[0] == "CLIENT_START_READY" :
                        # send_message(sock, "MOVIE_SYSTEM_START")

                    elif message[0] == "CLIENT_NEXT" :
                        send_message(sock, "MOVIE_INFO")

                    elif message[0] == "CLIENT_MOVIE_CHOICE" :
                        seats = message[-1].split(", ")
                        result = movie_function.movie_choice(movie_function.get_movies(),  int(message[1]),  int(message[2]),  int(message[3]),  seats)

                        if result:
                            ticket = random.randrange(1, 100000000)
                            send_message(sock, "SUCCESS# MOVIE_CHOICE# %d" % ticket)
                        elif not result:
                            send_message(sock, "ERROR# MOVIE_CHOICE")

                    elif message[0] == "CLIENT_MOVIE_ADD":
                        times = message[-1].split(", ")

                        if len(message) == 3:
                            result = movie_function.movie_add_times(int(message[1]), times)
                        elif len(message) == 4:
                            result = movie_function.movie_add(MovieInfo(int(message[1]), message[2], times))

                        if result:
                            send_message(sock,"SUCCESS# CLIENT_MOVIE_ADD")
                            mosquitto.mosquitto_start("ad/yes", movie_function.get_movies()[-1])
                        else:
                            print "out of add : ", result
                            send_message(sock, "ERROR# CLIENT_MOVIE_ADD")

                    elif message[0] == "CLIENT_MOVIE_CHANGE":
                        result = movie_function.movie_amend(int(message[1]), int(message[2]), message[3])

                        if result:
                                send_message(sock, "SUCCESS# CLIENT_MOVIE_CHANGE")
                        elif not result:
                                send_message(sock, "ERROR# CLIENT_MOVIE_CHANGE")

                    elif message[0] == "CLIENT_MOVIE_DEL":
                        result = movie_function.movie_del(int(message[1]))
                        print "movie_del result : ", str(result)
                        if result:
                                send_message(sock, "SUCCESS# CLIENT_MOVIE_DEL")
                        elif not result:
                                send_message(sock, "ERROR# CLIENT_MOVIE_DEL")

                    else:
                        print "\t", message

                else:
                    connection_list.remove(sock)
                    sock.close()
                    print "INFO : [%s] 사용자와의 연결이 끊어졌습니다." % ctime()

    # 부드럽게 종료하기
    except KeyboardInterrupt:
        server_socket.close()
        sys.exit()
