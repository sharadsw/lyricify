import requests, bs4, os

URL = "https://genius.com/"

def create_song_url(artist, song):
    artist = artist.split(" ")
    song = song.split(" ")
    song_url = ("-".join(artist).lower() + "-" + "-".join(song).lower() + "-lyrics").capitalize()

    return song_url

def get_lyrics(song_url):
    response = requests.get(URL + song_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    lyrics = soup.select('p')

    del response

    return lyrics[0].getText()

def get_album_image(song_url):
    response = requests.get(URL + song_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    album_image = soup.select('.cover_art-image')
    image_src = album_image[0].get('src')

    # Download album image to /image/album.jpg
    r = requests.get(image_src)
    image_file = open(os.getcwd() + "/img/album.jpg", 'wb')
    for chunk in r.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    del r
    del response

#def main():
#    artist = "Radiohead"
#    song = "Daydreaming"
#
#    song_url = create_song_url(artist, song)
#    lyrics = get_lyrics(song_url)
#    get_album_image(song_url)
#
#    print(artist + " - " + song)
#    print(lyrics)
#
#if __name__=='__main__':
#    main()
