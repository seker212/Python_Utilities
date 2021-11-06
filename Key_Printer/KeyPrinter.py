from sys import exit
from keyboard import on_press

def pressed(event):
    print(event.name, end='\r\n')
    
on_press(pressed)

if __name__ == '__main__':
    print('===========')
    print('KEY PRINTER')
    print('===========')
    while 1:
        try:
            pass
        except KeyboardInterrupt:
            exit(0)