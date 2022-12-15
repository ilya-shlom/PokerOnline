import os
import socket
from kivy.config import Config
from classes import MyApp

x = os.environ.get('x', 50)
y = os.environ.get('y', 50)
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', x)
Config.set('graphics', 'top', y)
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    addr = ('localhost', 8888)
    sock.connect(addr)
    MyApp().run()
    while True:
        try:
            com = input()
            if com:
                sock.sendto(com.encode(), addr)
                msg = sock.recv(1024)
                msg = msg.decode()
                print(msg)
            else:
                print("No input!")
        except KeyboardInterrupt:
            break
