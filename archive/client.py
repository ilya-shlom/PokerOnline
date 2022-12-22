import os
import socket
from time import sleep

from kivy.clock import mainthread
from classes import *
from kivy.config import Config
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.text import LabelBase


Builder.load_file('archive/bg.kv')
LabelBase.register(name='NAMU-1990', fn_regular='static/assets/NAMU-1990.ttf')

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1280)
Config.set('graphics', 'height', 720)


class MyLayout(Widget):
    def update_trump(self, card: str):
        self.ids.trump.source = f'images/cards/{card}.png'




class MyApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lobby = Lobby(2, 123, False)
        self.lobby.start_new_game()
        self.layout = MyLayout()

    def build(self):
        self.layout.add_widget(Card)
        return self.layout

    def on_start(self):
        self.layout.update_trump(self.lobby.current_deck.trump)

    @mainthread
    def update(self):
        print("Что делать...")


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
