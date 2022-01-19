'''
Date : 2022-01-14
Writer : Yoobi

Patch Note
[2022-01-14]
- client socket sender
'''

from datetime import datetime
from requests import get #공인 ip를 가져오기 위힘
import socket #사설 ip를 가져오기 위함
import getmac #MAC주소 가져오기 위함

HOST = '127.0.0.1'
PORT = 21

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

current_time = datetime.now()
public_ip = get("https://api.ipify.org").text
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
private_ip = s.getsockname()[0]
s.close()

message = str(current_time) + " " + public_ip + " " + private_ip + " " + getmac.get_mac_address()

client_socket.send(message.encode())

client_socket.close()
