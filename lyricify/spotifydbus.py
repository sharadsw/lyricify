import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

import lyrics, view

class SpotifyDBus():

    def __init__(self):
        dbus_loop = DBusGMainLoop(set_as_default=True)
        self.spotify_bus = dbus.SessionBus(dbus_loop).get_object("org.mpris.MediaPlayer2.spotify",
                                                                 "/org/mpris/MediaPlayer2")
        self.spotify_bus.connect_to_signal("PropertiesChanged",
                                           self.on_change)
        self.set_properties()
        self.lyricify()

        GLib.MainLoop().run()

    def set_properties(self):
        metadata = self.spotify_bus.Get("org.mpris.MediaPlayer2.Player",
                                        "Metadata",
                                        dbus_interface="org.freedesktop.DBus.Properties")
        self.song = metadata['xesam:title']
        self.artist = metadata['xesam:artist'][0]

    def on_change(self, interface, changed_properties, invalidated_properties):
        metadata = changed_properties.get("Metadata", {})
        if(self.song == metadata['xesam:title'] and self.artist == metadata['xesam:artist'][0]):
            return
        self.song = metadata['xesam:title']
        self.artist = metadata['xesam:artist'][0]
        print("{} - {}".format(self.artist, self.song))
        self.lyricify()

    def lyricify(self):
        song_url = lyrics.create_song_url(self.artist, self.song)
        song_lyrics = lyrics.get_lyrics(song_url)
        lyrics.get_album_image(song_url)
        view.win.update_view(self.artist, self.song, song_lyrics)

def main():
    SpotifyDBus()

if __name__=="__main__":
    main()
