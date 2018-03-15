# -*- coding: utf8 -*-

# import socket module.
from socket import *

# Custom Package import.
from sub import *
from aes128_message import *
# Information Package import.
from information.socketinfo import *
from information.personinfo import *
# Function Package import.
from function.clientfunction import *

# import sys module
# It used to exit client.
import sys
import pickle
import struct


# Main Start.
if __name__ == '__main__':
    # key = value for decryption and encryption.
    key = 'password123qwe'

    # function Module value define.
    client_user = PersonInfo()
    client_function = Client_Function()
    mosquitto = Paho_Mqtt()

    # basic values.
    # movies = movie list loading from server.
    movies = None
    # sale = Percentage of sale.
    sale = None

    # recv_message(csock, *type_name):
    #       Will decrypt 'temp' and return string type message list
    #       when It's not a data_massage. If It's a data_message, return string type message.
    def recv_message(csock, *type_name):
        if len(type_name) != 0:
            if type_name[0] == "data_message":
                temp = csock.recv(type_name[1])
        else:
            temp = csock.recv(SocketInfo().get_bufsize())

        client_message = AES128_HMAC_Decrypt(key, binascii.unhexlify(temp[:32]), binascii.unhexlify(temp[32:]))

        if len(type_name) != 0:
            if type_name[0] == "data_message":
                return client_message
        else:
            return client_message.split("# ")

    # send_message(csock, server_command): Will encrypt 'server_command' and send 'server_message'
    def send_message(csock, server_command):
        server_message = AES128_HMAC_Encrypt(key, server_command)
        csock.send(server_message)

    # make 'serverSocket' object -> try to connect server socket.
    serverSocket = socket(AF_INET, SOCK_STREAM)
    try:
        serverSocket.connect(SocketInfo().get_addr())
    except Exception as e:
        print('영화 서버(%s:%s)에 연결 할 수 없습니다.' % SocketInfo().get_addr())
        sys.exit()

    print('영화 서버(%s:%s)에 연결 되었습니다.' % SocketInfo().get_addr())

    # start ROOF
    while True:
        try:
            message = recv_message(serverSocket)
            print " >> server say : ", message
            if not message:
                print('영화 서버(%s:%s)와의 연결이 끊어졌습니다.' % SocketInfo().get_addr())
                serverSocket.close()
                sys.exit()
            else:
                # connect Server socket, now you have to login.
                # [ PAGE ] login
                if message[0] == "LOGIN":
                        client_user.set_person_id(raw_input("ID : "))
                        client_user.set_person_pw(raw_input("PW : "))
                        send_message(serverSocket, "LOGIN_CLIENT# %s# %s" % (client_user.get_person_id(), client_user.get_person_pw()))

                # File 전송하는 socket 연결 시 동작하는 부분
                elif message[0] == "MOVIE_INFO":

                    if len(message) == 5:
                        print message
                        client_user.set_person_grade(message[1])
                        client_user.set_person_name(message[2])
                        client_user.set_person_ad_agree(message[3])
                        sale = message[4]
                        mosquitto.mosquitto_start(client_user.get_person_ad_agree())

                    send_message(serverSocket, "MOVIE_INFO_READY")

                    fsock = socket(AF_INET, SOCK_STREAM)
                    fsock.connect(SocketInfo().get_faddr())

                    try:
                        FILE_SIZE = recv_message(fsock)
                        send_message(fsock, "MOVIE_SIZE_READY")

                    except:
                        print "try1 error"

                    try:
                        movies = recv_message(fsock, "data_message", int(FILE_SIZE[0]))
                        movies = pickle.loads(movies)

                    except Exception as e:
                        print "ERROR : ", e
                        print (" File receive Error")
                    finally:
                        fsock.close()

                    send_message(serverSocket, "CLIENT_START_READY")

                # [ PAGE ] dialog, Thx to visit our site.
                # [ PAGE ] dialog, sometime sale information show.
                elif message[0] == "MOVIE_SYSTEM_START":
                        print client_user.get_person_name(), "님 환영합니다."
                        if sale == "Yes":
                            print "비가 많이오는데, 영화를 보러오다니! 할인 30% 해드립니다!!"
                        # inside = return value from Client function.
                        inside = client_function.movie_system_start(client_user.get_person_grade(), movies, sale)

                        # isinstnace(object, classinfo): return True if 'object' is 'classinfo's' instance.
                        if isinstance(inside, int):
                            if inside == 0:
                                raise KeyboardInterrupt

                        else:
                            print type(inside), "\n inside > ",
                            print inside

                            if inside[0] == 1:
                                send_message(serverSocket, "CLIENT_MOVIE_CHOICE# %d# %d# %d# %s" % (inside[1], inside[2], inside[3], inside[4]))

                            elif inside[0] == 3:
                                if inside[1] == 1:
                                    if len(inside) == 4:
                                        send_message(serverSocket, "CLIENT_MOVIE_ADD# %d# %s" % (inside[2], inside[3]))

                                    elif len(inside) == 5:
                                        send_message(serverSocket, "CLIENT_MOVIE_ADD# %d# %s# %s" % (inside[2], inside[3], inside[4]))

                                elif inside[1] == 2:
                                    send_message(serverSocket, "CLIENT_MOVIE_CHANGE# %d# %s# %s" % (inside[2], inside[3], inside[4]))

                                elif inside[1] == 3:
                                    send_message(serverSocket, "CLIENT_MOVIE_DEL# %d" % inside[2])

                elif message[0] == "SUCCESS":
                    if message[1] == "MOVIE_CHOICE":
                        print "에매번호는", message[2], "입니다."

                    send_message(serverSocket, "CLIENT_NEXT")

                elif message[0] == "ERROR":
                    if message[1] == "MOVIE_CHOICE":
                        print "예매가 진행되지 않았습니다."

                    send_message(serverSocket, "CLIENT_NEXT")

                else:
                    print " >> else server say : ", message

        except KeyboardInterrupt as e:
            serverSocket.close()
            sys.exit()
