# RL Epic Games Custom Map Loader
New workaround for Epic Games users to load any custom map into Rocket League via the Steam Workshop

## Installing and Running the App
1. Download or clone this repo
2. Unzip the file and naviagte to dist/Map Loader. Inside there is a file called 'Map Loader.exe' (or may just be called Map Loader). Double click to launch the application.

If that doesn't work, you can compile the source code below using these steps:
1. Make sure Python 3 is installed: https://www.python.org/downloads/ along with Tkinter: https://tkdocs.com/tutorial/install.html
	- You may have the option to install Tkinter during the installation of Python. I can't remember but just in case download Python first and see if there are any boxes you can check that allow you to install Tkinter along with the Python installation.
2. Install kivy (App GUI): `pip install kivy`
3. Run using `python main.py` or `python3 main.py`
	- Alternatively just double click 'main.py' in the folder to launch the app

## Usage
1. Create a new folder, name it whatever you want. Just remember where you put it. This will be the folder that stores all your maps
2. Find a map you would like to download on the Steam Workshop (ex: https://steamcommunity.com/sharedfiles/filedetails/?id=1671658424&searchtext=rings)
3. Copy the URL of that map and then go to https://steamworkshopdownloader.io/ and paste the link on that website to download the .zip file for the map. 
4. Once the file is downloaded, extract it to the new folder you made for the maps. You can name the extracted folder whatever you'd like. That's the name that will show up in the app. Make sure you set up your map folder like this:
>RL MAP FOLDER
>>Folder: Speed Jump - Rings 3
>>> .udk file located somewhere in this folder
>
>>Folder: Lava Rings
>>> .udk file located somewhere in this folder

>>Folder: Giant Rings
>>> .udk file located somewhere in this folder

5. In the app, click the "Locate Rocket League folder" button. From here a file browser will pop up and you need to select the location of where Rocket League is on your system. It should be in a folder named 'rocketleague'. When found click Select Folder. The app will display the path to your folder. It should look something like this: `RL Path: D:/Games HDD/rocketleague`
6. Now click the "Import Maps" button. The file browser will pop up and you need to select the location of the folder you made that has all your maps in it. Select this folder. Again, the app will display the path to your folder. It should look something like this: `Map Folder Path: C:/Users/Marc/Desktop/RL_Maps`
7. You should now be all set to select a map. Click one of the maps you've installed on the app and it should light up green, indicating that map is now loaded. To play the map, open Rocket League and select free play under training. I made it so the map you choose replaces the Labs - Underpass map. So in training, select that map and press play. You should now be in the custom map you downloaded.
8. If you add any maps to the folder while the app is running, you can click the refresh button next to it to reload the maps you have downloaded in the folder.
9. In case things go wrong, there is a "Reset Game Files" button. If the map is unplayable or corrupted it may mess up your game and the original Underpass map. If this happens click this button. It will remove the custom map from your game and replace the Underpass map with it's original file. After that everything should be good to go again 

