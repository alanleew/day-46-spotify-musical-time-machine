import requests
import pprint
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# date = input("What date would you like to travel to? (YYYY-MM-DD): ")
# url = f"https://www.billboard.com/charts/hot-100/{date}"
# url = f"https://www.billboard.com/charts/hot-100/2020-02-02"
# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
#
# response = requests.get(url, headers=header)
# response.raise_for_status()
#
# html = response.text
# soup = BeautifulSoup(html, "html.parser")
#
# # song_list = soup.select('div.o-chart-results-list-row-container li.lrv-u-width-100p h3#title-of-a-story')
# song_list = soup.select('div ul li ul li h3')
# song_titles = [song.getText().strip() for song in song_list]
# # print(len(song_titles))
# pprint.pprint(song_titles)

SPOTIFY_CLIENT_ID = "8b23f792cb2c491c93b3d84e84b90022"
SPOTIFY_CLIENT_SECRET = "c9a64762489e4f6cb2d1afb06ede63ea"
# APP_REDIRECT_URI = "http://localhost:1234"
APP_REDIRECT_URI = "https://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=APP_REDIRECT_URI,
        scope="playlist-modify-private",
        # scope = "user-library-read",
    )
)

user_id = sp.current_user()["id"]
print(user_id)