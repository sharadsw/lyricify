# lyricify
Lyricify is a CLI/GUI application that retrieves the lyrics of the current Spotify song for Linux. It uses dbus to detect the current song and scrapes [genius.com](https://www.genius.com) for the lyrics.

## Dependencies
* requests
* BeautifulSoup
* GTK+ 3
* PyGObject

## Install
Make sure all dependencies are installed.
```
git clone https://github.com/sharadsw/lyricify
cd lyricify
python setup.py install --user
```
## Usage
Command-line
```
lyricify
```

GUI
```
lyricify -ui
```
![Screenshot](https://user-images.githubusercontent.com/16229739/169935460-c9bd042c-d2e8-477f-a0fb-6ad9034b7dc4.png)
