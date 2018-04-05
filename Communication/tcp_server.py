import socket

HOST = ''
PORT = 7001
BUFSIZE = 1024
ADDR = (HOST, PORT)


class Socket:
    def __init__(self):
        # ================================================
        # Make server_socket and add reuse_address option.
        # ================================================
        print('socket class >> >> >> >> >> >> ')
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(ADDR)
        self.server_socket.listen(10)

        self.client = None

    def connection(self):
        self.client, client_ip = self.server_socket.accept()
        print('\nclient ip >> {}'.format(client_ip))
        print('\nsend file? [ y/n ]')
        answer = input(' >>')

        return answer

    def file_send(self):
        try:
            print('\ntry to read file {}'.format('-'*10))
            with open('test_file.wav', 'rb') as test_file:
                data = test_file.read()
        except Exception as e:
            print('\n\tfile can\'t open >> {}'.format(e))

        try:
            print('try to send file {}'.format('-'*10))
            data_len = self.client.send(data)
        except Exception as e:
            data_len = 0
            print('\n\tfile can\'t send >> {}'.format(e))

        print('\tdata_len = {}'.format(data_len))

    def disconnection(self):
        self.client.close()


if __name__ == '__main__':
    sock = Socket()
    continue_value = True

    def continue_function():
        if sock.connection() == 'y':
            sock.file_send()
            sock.disconnection()
            print('\nclose socket, try to connect again? [ y/n ]')
            answer = input(' >>')

            if answer == 'y':
                print('\nawait connection\n')
                return True
            else:
                return False
        else:
            sock.disconnection()
            print('\nclose socket, program end')
            return False

    while continue_value:
        continue_value = continue_function()