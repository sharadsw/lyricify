# lyricify
Lyricify is a CLI/GUI application that retrieves the lyrics of the current Spotify song for Linux. It uses dbus to retrieve the current song and scrapes [genius.com](https://www.genius.com) for the lyrics.

### Dependencies
* Spotify
* Python3
* GTK+ 3
* PyGObject
* Requests
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

GUI
```
lyricify -ui
```

![screenshot](http://i.cubeupload.com/mNew80.png)
