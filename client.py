import os
import socket
from kivy.config import Config
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.text import LabelBase


Builder.load_file('bg.kv')


Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1280)
Config.set('graphics', 'height', 720)


class MyLayout(Widget):
    pass


class MyApp(App):
    def build(self):
        return MyLayout()


LabelBase.register(name='NAMU-1990', fn_regular='static/assets/NAMU-1990.ttf')


# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#     addr = ('localhost', 8888)
#     sock.connect(addr)
#     MyApp().run()
#     while True:
#         try:
#             com = input()
#             if com:
#                 sock.sendto(com.encode(), addr)
#                 msg = sock.recv(1024)
#                 msg = msg.decode()
#                 print(msg)
#             else:
#                 print("No input!")
#         except KeyboardInterrupt:
#             break
if __name__ == '__main__':
    MyApp().run()
            # Scatter:
            #     scale: 2
            #     add_widget: image
            #     Image:
            #         id: image
            #         source: 'images/deck.png'