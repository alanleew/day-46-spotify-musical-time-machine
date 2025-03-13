import requests
import pprint
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

##############################################################################
### Uses input and scrapes Billboard 100 HTML for 100 song titles from specific date ###
date = input("What date would you like to travel to? (YYYY-MM-DD): ")
url = f"https://www.billboard.com/charts/hot-100/{date}"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url, headers=header)
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, "html.parser")

# song_list = soup.select('div.o-chart-results-list-row-container li.lrv-u-width-100p h3#title-of-a-story')
song_list = soup.select('div ul li ul li h3')
song_titles = [song.getText().strip() for song in song_list]
# pprint.pprint(song_titles)

##############################################################################
### This section uses Spotipy to connect to Spotify ###
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
APP_REDIRECT_URI = "https://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=APP_REDIRECT_URI,
        cache_path=".cache.txt",
        show_dialog=True,
        scope="playlist-modify-private",
        # scope = "user-library-read",
    )
)

uri = []
for song in song_titles:
    search_result = sp.search(
        q=f"track:{song}",
        limit=1,
        type="track"
    )
    try:
        ### This gets link to song
        # print(search_result["tracks"]["items"][-1]["external_urls"]["spotify"])
        ### This gets song ID
        uri.append(search_result["tracks"]["items"][-1]["id"])
    except IndexError:
        print(f"Oopsie, made a whoopsie. {song} doesn't exist in Spotify. NEXT!")


user_id = sp.current_user()["id"]

new_playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100 Hits",
    public=False,
    description=f"Testing to scrape Billboard 100 hits from date: {date}"
)
new_playlist_id = (new_playlist["id"])

# sp_client = spotipy.client.Spotify()
sp.playlist_add_items(
    playlist_id=new_playlist_id,
    items=uri
)
