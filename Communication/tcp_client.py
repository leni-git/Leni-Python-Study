import socket


HOST = '192.168.0.134'
PORT = 7001
ADDR = (HOST, PORT)
BUFF_SIZE = 1024

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
clientSocket.connect(ADDR)


def send_recv(clientSocket):
    clientSocket.send('안녕하세요'.encode())
    text = clientSocket.recv(BUFF_SIZE)
    text = text.decode()

    return text


while True:
    print("choice >> 1. send 2. pass 0. break")
    put = input(">>")

    if put == '0':
        break
    elif put == '1':
        print(send_recv(clientSocket))
    else:
        pass

