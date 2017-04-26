# lyricify
Lyricify is a CLI/GUI application that retrieves the lyrics of the current Spotify song for Linux. It uses dbus to retrieve the current song and scrapes [genius.com](https://www.genius.com) for the lyrics.

### Dependencies
General:
* Spotify
* Python3
* GTK+ 3

Python modules:
* dbus
* requests
* bs4