'''
Date : 2022-01-19
Writer : Yoobi

Patch Note
[2022-01-19]
- mix mouse event & socket
'''

### socket client part ###
# set modules
from datetime import datetime
from requests import get #공인 ip를 가져오기 위힘
import socket #사설 ip를 가져오기 위함
import getmac #MAC주소 가져오기 위함

### mouse event part ###
# set modules
from pynput import mouse

###################################
### mouse event functions start ###
###################################

# printing moving mouse info
def on_move(x,y):
    print('Position : x:%s, y:%s' %(x,y))

# printing clicking mouse info
def on_click(x, y, button, pressed):
    print('Button: %s, Position: (%s, %s), Pressed: %s ' %(button, x, y, pressed))
    if str(button) == "Button.left" and str(pressed) == "True":
        socket_sender(x, y)

# printing scrolling mouse info
def on_scroll(x, y, dx, dy):
    print('Scroll: (%s, %s) (%s, %s).' %(x, y, dx, dy))

def mouse_listener():
    # holding listen mode and when an event occurs as listener
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

#################################
### mouse event functions end ###
#################################

######################################
### socket sending data part start ###
######################################

def socket_sender(x, y):
    # set target server info
    HOST = '127.0.0.1'
    PORT = 21

    # connecting with server
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # set data
    current_time = datetime.now()
    public_ip = get("https://api.ipify.org").text
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    private_ip = s.getsockname()[0]
    s.close()

    # set sending msg
    message = str(current_time) + " " + public_ip + " " + private_ip + " " + getmac.get_mac_address() + "$$" + str(x) + "$$" + str(y)

    # send to server
    client_socket.send(message.encode())

    # socket closing
    client_socket.close()

####################################
### socket sending data part end ###
####################################

if __name__ == '__main__':
    print("a")
    mouse_listener()