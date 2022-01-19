'''
Date : 2022-01-07
Writer : Yoobi

Patch Note
[2022-01-09]
- print Mouse Position
'''

# set modules
from pynput import mouse

# printing moving mouse info
def on_move(x,y):
    print('Position : x:%s, y:%s' %(x,y))

# printing clicking mouse info
def on_click(x, y, button, pressed):
    print('Button: %s, Position: (%s, %s), Pressed: %s ' %(button, x, y, pressed))

# printing scrolling mouse info
def on_scroll(x, y, dx, dy):
    print('Scroll: (%s, %s) (%s, %s).' %(x, y, dx, dy))

# holding listen mode and when an evnet occurs as listener
with mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll) as listener:
    listener.join()