import kivy
import os
import tkinter as tk
import math
from tkinter import filedialog

from functools import partial
from kivy.app import App
from kivy.base import Builder
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.config import Config 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

kivy.require("1.10.1")
Config.set('graphics', 'resizable', True)

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

class MapLoader(Widget):

    def test(self):
        print("jasdjkasd")
    
    def load_maps(self):
        if map_path != '':
            # remove previous maps
            for c in list(self.children):
                if isinstance(c, ScrollView) or isinstance(c, GridLayout): self.remove_widget(c)

            path = map_path.replace("/", "\\")
            os.chdir(path)
            os_path, dirs, files = next(os.walk(path))
            dir_count = len(dirs)

            grid = GridLayout(pos=(self.x+50, self.height-300), 
                            size=(200, 200), 
                            rows=math.ceil(dir_count/3), cols=3,
                            col_default_width=250, row_default_height=250,
                            spacing=(30, 30), size_hint_y=None, padding=(30, 30))   
            grid.bind(minimum_height=grid.setter('height'))
                   
            for i in range(dir_count):
                print(dirs)
                grid.add_widget(Button(text=dirs[i]))

            root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height), 
                            pos=(self.x, self.y-80))
            root.add_widget(grid)
            self.add_widget(root)

    def update_RLPATH(self):
        self.ids["RLPATH"].text = "RL Path: " + rl_path
    
    def update_MAPPATH(self):
        self.ids["MAPPATH"].text = "Map Folder Path: " + map_path
        self.load_maps()


class MapLoaderApp(App):

    
    def build(self):
        self.title = "Custom Map Loader"
        return MapLoader()


if __name__ == '__main__':
    Window.clearcolor = (0.15, 0.15, 0.2, 1)
    Window.size = (1000, 600)
    MapLoaderApp().run()