'''
Date : 2022-01-14
Writer : Yoobi

Patch Note
[2022-01-14]
- server threaded socket receiver
'''

import socket
import sys
from _thread import *
from urllib import parse

# 쓰레드에서 실행되는 코드
# 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신
def threaded(client_socket, addr):
    print('Connected by :', addr[0], ':', addr[1])

    # 클라이언트가 접속을 끊을 때 까지 반복
    while True:

        try:
            # 데이터 수신
            data = client_socket.recv(1024)
            print(data.decode())

            if not data:
                print('Disconnected by ' + addr[0], ':', addr[1])
                break

        except ConnectionResetError as e:

            print('Disconnected by ' + addr[0], ':', addr[1])
            break

    client_socket.close()

# 서버 정보 setting
HOST = '0.0.0.0'
PORT = 21

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

print('server start')

# 클라이언트가 접속하면 accept 함수에서 새로운 소켓 리턴
# 새로운 쓰레드에서 해당 소켓을 사용하여 통신
while True:
    print('wait')

    client_socket, addr = server_socket.accept()
    start_new_thread(threaded, (client_socket, addr))

server_socket.close()