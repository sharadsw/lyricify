# lyricify
Lyricify is a CLI/GUI application that retrieves the lyrics of the current Spotify song for Linux. It uses dbus to retrieve the current song and scrapes [genius.com](https://www.genius.com) for the lyrics.

### Dependencies
General:
* Spotify
* Python3
* GTK+ 3
* PyGObject
* Requests module
* Beautiful Soup

### Installation
Make sure all dependencies are installed.
```
git clone https://github.com/TheRealSS/lyricify
cd lyricify
python setup.py install
```
### Usage
Command-line
```
lyricify
```
This will print lyrics of the current song to the terminal.

GUI
```
lyricify -ui
```
This will open a GTK window that displays the lyrics.
![screenshot](https://i.cubeupload.com/3Knx86.jpg)