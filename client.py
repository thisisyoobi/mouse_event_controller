'''
Date : 2022-01-09
Writer : Yoobi

Patch Note
[2022-01-09]
- print Mouse Position
'''

from pynput import mouse

def on_move(x,y):
    print('Position : x:%s, y:%s' %(x,y))

def on_click(x, y, button, pressed):
    print('Button: %s, Position: (%s, %s), Pressed: %s ' %(button, x, y, pressed))

def on_scroll(x, y, dx, dy):
    print('Scroll: (%s, %s) (%s, %s).' %(x, y, dx, dy))

with mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll) as listener:
    listener.join()