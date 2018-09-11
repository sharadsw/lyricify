import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf


class LyricifyUI(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Lyricify")
        self.set_default_size(450, 400)

        # Vbox for the entire window
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        vbox.set_homogeneous(False)
        vbox.set_margin_top(20)
        vbox.set_margin_left(5)

        # Hbox containing the album image and song details
        hbox = Gtk.Box(spacing=2)

        self.album_image = Gtk.Image()
        hbox.pack_start(self.album_image, False, False, 20)

        self.music_label = Gtk.Label()
        self.music_label.set_alignment(xalign=0, yalign=0)
        hbox.pack_start(self.music_label, False, False, 0)

        vbox.pack_start(hbox, False, False, 0)

        self.lyrics_label = Gtk.Label()
        self.lyrics_label.set_alignment(xalign=0, yalign=0)

        # Hbox for the lyrics
        hbox_lyrics = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        hbox_lyrics.set_homogeneous(False)
        hbox_lyrics.pack_start(self.lyrics_label, True, False, 0)

        # Adding a scrollbar to the above Hbox
        scrollbox = Gtk.ScrolledWindow()
        scrollbox.add_with_viewport(hbox_lyrics)
        scrollbox.set_min_content_height(400)
        scrollbox.set_margin_left(20)
        scrollbox.set_margin_top(15)

        vbox.pack_start(scrollbox, False, False, 0)

        self.add(vbox)

    def update_view(self, artist, song, lyrics):
        home_dir = os.getenv("HOME")
        img_path = os.path.join(home_dir, ".cache/lyricify/album.jpg")

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename=img_path,
            width=160,
            height=160,
            preserve_aspect_ratio=True)

        self.album_image.set_from_pixbuf(pixbuf)
        self.lyrics_label.set_label(lyrics)
        self.music_label.set_markup("<big>"+song+"</big>\n<b>"+artist+"</b>")

        self.show_all()
