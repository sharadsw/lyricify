import gi
gi.require_version('Playerctl', '1.0')
from gi.repository import Playerctl, GLib 

import lyrics, view

player = Playerctl.Player()

first_play = False
current_song = ""

def on_play(player):
    # Return if a song wasn't changed but only paused and resumed
    if(current_song == player.get_title()):
        return

    artist = player.get_artist()
    song = player.get_title()

    song_url = lyrics.create_song_url(artist, song)
    song_lyrics = lyrics.get_lyrics(song_url)
    lyrics.get_album_image(song_url)

    print(song_lyrics)
    view.win.update_view(artist, song, song_lyrics)

def on_pause(player):
    current_song = player.get_title()

player.on('play', on_play)
player.on('pause', on_pause)

if player.get_property('status') == "Playing" and first_play == False:
    first_play = True
    on_play(player)

GLib.MainLoop().run()
