import kivy
import os
import tkinter as tk
import math
import glob

from tkinter import filedialog
from shutil import copy2
from functools import partial
from kivy.app import App
from kivy.base import Builder
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.config import Config 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock

kivy.require("1.10.1")
Config.set('graphics', 'resizable', True)

home_dir = os.getcwd()
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

    def reset(self):
        # reset all button colors
        buttons = self.children[0].children[0].children
        for b in buttons:
            if b.background_color == [0, 1, 0, 1]:
                b.background_color = [1, 1, 1, 1]

        # remove underpass and the backup if it's there 
        full_rl_path = rl_path+"/TAGame/CookedPCConsole"
        for _,_, files in os.walk(full_rl_path):
            for f in files:
                if f == "Labs_Underpass_P_BACKUP.upk":
                    os.remove(full_rl_path+"/Labs_Underpass_P_BACKUP.upk")
                elif f == "Labs_Underpass_P.upk":
                    os.remove(full_rl_path+"\\Labs_Underpass_P.upk")

        # put original bak from this repo
        copy2(home_dir+"\\Labs_Underpass_P.upk", full_rl_path)          
    
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
                   
            # populate grid with the file name and image      
            for i in range(dir_count):
                os.chdir(path+"/"+dirs[i])

                # get image file
                pic = glob.glob("./*.png")
                if len(pic) == 0:
                    pic = glob.glob("./*.jpg")[0]
                else:
                    pic = pic[0]

                # create button and imagev for it
                btn = Button(text=dirs[i])
                btn.bind(on_press=self.select_map)
                grid.add_widget(btn)
                os.chdir("../")

            root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height), 
                            pos=(self.x, self.y-80))
    
            root.add_widget(grid)
            self.add_widget(root)

    def update_RLPATH(self):
        self.ids["RLPATH"].text = "RL Path: " + rl_path
    
    def update_MAPPATH(self):
        self.ids["MAPPATH"].text = "Map Folder Path: " + map_path
        self.load_maps()
    
    def select_map(self, instance):
        # remove the green button
        buttons = self.children[0].children[0].children
        for b in buttons:
            if b.background_color == [0, 1, 0, 1]:
                b.background_color = [1, 1, 1, 1]
        instance.background_color=(0, 1, 0, 1)

        # check if backup is made
        full_rl_path = rl_path+"/TAGame/CookedPCConsole"
        found = False
        for _,_, files in os.walk(full_rl_path):
            for f in files:
                if f == "Labs_Underpass_P_BACKUP.upk":
                    found = True
                    break

        # create backup if needed
        if not found:
            copy2(full_rl_path+"/Labs_Underpass_P.upk", full_rl_path+"/Labs_Underpass_P_BACKUP.upk")

        # copy selected map to directory
        full_map_path = map_path+"/"+instance.text
        os.chdir(full_map_path)
        udk = glob.glob("*.udk")[0]
        full_map_path = full_map_path+"/"+udk
        copy2(full_map_path, full_rl_path+"/Labs_Underpass_P.upk")
       

class MapLoaderApp(App):

    
    def build(self):
        self.title = "Custom Map Loader"
        return MapLoader()


if __name__ == '__main__':
    Window.clearcolor = (0.15, 0.15, 0.2, 1)
    Window.size = (1000, 600)
    MapLoaderApp().run()