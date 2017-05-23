import sys
import argparse
import dbus
from subprocess import call
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

from lyricify import lyrics
from lyricify.view import LyricifyUI


class SpotifyCtl():

    def __init__(self, ui=None):
        self.connect_to_spotify()
        self.set_properties()
        self.ui = ui

        if self.ui:
            self.win = LyricifyUI()
            self.win.connect('delete-event', self.on_exit)

        self.lyricify()

        GLib.MainLoop().run()

    def connect_to_spotify(self):
        try:
            dbus_loop = DBusGMainLoop(set_as_default=True)
            self.spotify_bus = dbus.SessionBus(dbus_loop).get_object(
                "org.mpris.MediaPlayer2.spotify",
                "/org/mpris/MediaPlayer2")
            self.spotify_bus.connect_to_signal("PropertiesChanged",
                                               self.on_change)
        except:
            print("\nCould not connect to Spotify, exiting...")
            sys.exit()

    def set_properties(self):
        metadata = self.spotify_bus.Get(
            "org.mpris.MediaPlayer2.Player",
            "Metadata",
            dbus_interface="org.freedesktop.DBus.Properties")

        self.song = metadata['xesam:title']
        self.artist = metadata['xesam:artist'][0]

    def on_change(self, interface, changed_properties, invalidated_properties):
        metadata = changed_properties.get("Metadata", {})
        if(self.song == metadata['xesam:title'] and
           self.artist == metadata['xesam:artist'][0]):
            return

        self.song = metadata['xesam:title']
        self.artist = metadata['xesam:artist'][0]

        self.lyricify()

    def on_exit(self, window, event):
        self.win.hide_on_delete()
        self.ui = False

        return True

    def lyricify(self):
        song_url = lyrics.create_song_url(self.artist, self.song)
        try:
            song_lyrics = lyrics.get_lyrics(song_url)
            if self.ui:
                lyrics.get_album_image(song_url)
        except Exception as e:
            print(e)
            print("\nUnable to find lyrics/album art for the song, sorry!")
            return

        if self.ui:
            self.win.update_view(self.artist, self.song, song_lyrics)
        else:
            call("clear")
            print("{} - {}\n\n{}".format(self.artist, self.song, song_lyrics))


def main():
    parser = argparse.ArgumentParser(description='Get lyrics for Spotify song')
    parser.add_argument('-ui', action='store_true',
                        help='Open a GUI for lyrics')
    args = parser.parse_args()

    try:
        SpotifyCtl(ui=args.ui)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
        main()
