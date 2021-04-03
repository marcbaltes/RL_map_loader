import tkinter as tk
from tkinter import filedialog

from kivy.app import App
from kivy.base import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class PathButton(Button):
    @staticmethod
    def get_path():
        root = tk.Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        print(folder_selected)
        return folder_selected

class rootwi(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        return rootwi()

if __name__ == '__main__':
    MyApp().run()