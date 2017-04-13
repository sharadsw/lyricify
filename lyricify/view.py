import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib

import os

class LyricifyUI(Gtk.Window):

    def __init__(self):
        self.lyrics = ""
        self.artist = ""
        self.song = ""

        Gtk.Window.__init__(self, title="Lyricify")
        self.set_default_size(300, 500)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        vbox.set_homogeneous(False)

        hbox = Gtk.Box(spacing=2)

        # Add blank.jpg initally
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename="img/album.jpg",
            width=100,
            height=100,
            preserve_aspect_ratio=True)

        self.album_image = Gtk.Image.new_from_pixbuf(pixbuf)

        hbox.pack_start(self.album_image, True, False, 0)

        vbox_music = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)

        self.artist_label = Gtk.Label()
        vbox_music.pack_start(self.artist_label, True, False, 0)

        self.song_label = Gtk.Label()
        vbox_music.pack_start(self.song_label, True, False, 0)

        hbox.pack_start(vbox_music, True, False, 0)
        vbox.pack_start(hbox, True, False, 0)

        self.lyrics_label = Gtk.Label()
        vbox.pack_start(self.lyrics_label, True, False, 0)

        self.add(vbox)

        GLib.timeout_add_seconds(2, self.update_view)

    def update_view(self):
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename="img/album.jpg",
            width=100,
            height=100,
            preserve_aspect_ratio=True)

        self.album_image.set_from_pixbuf(pixbuf)
        self.lyrics_label.set_label(self.lyrics)
        self.artist_label.set_label(self.artist)
        self.song_label.set_label(self.song)

        return True

    def set_data(self, artist, song, lyrics):
        self.artist = artist
        self.song = song
        self.lyrics = lyrics

def main():
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

win = LyricifyUI()

if __name__=='__main__':
    main()
