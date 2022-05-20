import os
import string
import requests
import bs4

URL = "https://genius.com/"
LYRICS_SELECTOR = 'div[class*="Lyrics__Container"]'
ART_SELECTOR = 'img[class*="SizedImage__Image"]'


def create_song_url(artist, song):
    # Remove special characters and multiple spaces
    table = str.maketrans("", "", string.punctuation)
    song = song.translate(table).replace("  ", " ")

    artist = artist.split(" ")
    song = song.split(" ")
    song_url = ("-".join(artist).lower() + "-" +
                "-".join(song).lower() + "-lyrics").capitalize()

    return song_url


def get_lyrics(song_url):
    soup = make_soup(song_url)
    lyrics = soup.select(LYRICS_SELECTOR)
    lyrics_text = ""
    for div in lyrics:
        lyrics_text += div.getText(separator="\n")
        lyrics_text += "\n"

    return lyrics_text


def get_album_image(image_src):
    # Download album art to ~/.cache/lyricify/album.jpg
    home_dir = os.getenv("HOME")
    img_dir = os.path.join(home_dir, ".cache/lyricify/")

    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    img_path = os.path.join(img_dir, "album.jpg")
    response = requests.get(image_src)
    image_file = open(img_path, "w+b")
    for chunk in response.iter_content(100000):
        image_file.write(chunk)
    image_file.close()


def make_soup(song_url):
    response = requests.get(URL + song_url)

    return bs4.BeautifulSoup(response.text, "html.parser")
