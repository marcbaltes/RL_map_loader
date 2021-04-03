import kivy
import tkinter as tk
from tkinter import filedialog

from kivy.app import App
from kivy.base import Builder
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import Button

kivy.require("1.10.1")

map_path = ""
rl_path = ""
import_map = ""

class RLPathButton(Button):
    @staticmethod
    def get_path():
        global rl_path
        root = tk.Tk()
        root.withdraw()
        rl_path = filedialog.askdirectory()
        return rl_path

class MapPathButton(Button):
    @staticmethod
    def get_path():
        global map_path
        root = tk.Tk()
        root.withdraw()
        map_path = filedialog.askdirectory()
        return map_path

class ImportButton(Button):
    @staticmethod
    def get_path():
        global import_map
        root = tk.Tk()
        root.withdraw()
        import_map = filedialog.askdirectory(initialdir = map_path)
        return import_map

class MapLoader(Widget):
    def test(self):
        print("jasdjkasd")

    def update_RLPATH(self):
        self.ids["RLPATH"].text = "RL Path: " + rl_path
    
    def update_MAPPATH(self):
        self.ids["MAPPATH"].text = "Map Folder Path: " + map_path


class MapLoaderApp(App):

    
    def build(self):
        return MapLoader()


if __name__ == '__main__':
    Window.clearcolor = (0.15, 0.15, 0.2, 1)
    Window.size = (1000, 600)
    MapLoaderApp().run()