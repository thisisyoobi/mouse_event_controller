'''
Date : 2022-01-19
Writer : Yoobi

Patch Note
[2022-01-19]
- 
'''

### socket server part ###
# set modules
import socket
import sys
from _thread import *
from urllib import parse

### mouse evenet server part ###
# set modules
from pynput.mouse import Button, Controller

# this class have serveral mouse controll functions
class RemoteMouse:
    def __init__(self):
        self.mouse = Controller()

    def getPosition(self):
        return self.mouse.position

    def setPos(self, xPos, yPos):
        self.mouse.position = (xPos, yPos)

    def movePos(self, xPos, yPos):
        self.mouse.move(xPos, yPos)

    def click(self):
        self.mouse.click(Button.left)

    def doubleClick(self):
        self.mouse.click(Button.left, 2)

    def clickRight(self):
        self.mouse.click(Button.right)

    def drag(self, from_x, from_y, to_x, to_y, is_absolute=True):
        if is_absolute is True:
            self.mouse.position = (from_x, from_y)
        else:
            self.mouse.position = self.getPosition()
            self.click()
            self.mouse.move(from_x, from_y)
        self.click()
        self.mouse.press(Button.left)

        if is_absolute is True:
            self.mouse.position = (to_x, to_y)
        else:
            self.mouse.move(to_x, to_y)
        self.mouse.release(Button.left)

# setPos and click it
def mouse_controller(x, y):
    mouse = RemoteMouse()
    print('X: %s, Y:%s' %mouse.getPosition())
    
    mouse.setPos(500, 500)
    mouse.click()

    print('X: %s, Y:%s' %mouse.getPosition())
    return

# 쓰레드에서 실행되는 코드
# 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신
def threaded(client_socket, addr):
    print('Connected by :', addr[0], ':', addr[1])

    # 클라이언트가 접속을 끊을 때 까지 반복
    while True:

        try:
            # 데이터 수신
            data = client_socket.recv(1024)

            if not data:
                print('Disconnected by ' + addr[0], ':', addr[1])
                break
            
            data = data.decode()
            data = data.split("$$")
            print(data)
            x = data[1]
            y = data[2]
            print(x)
            print(y)
            # clicking
            mouse_controller(x, y)


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
