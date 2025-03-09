import requests
import pprint
from bs4 import BeautifulSoup

# date = input("What date would you like to travel to? (YYYY-MM-DD): ")
# url = f"https://www.billboard.com/charts/hot-100/{date}"
url = f"https://www.billboard.com/charts/hot-100/2020-02-02"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url, headers=header)
response.raise_for_status()

html = response.text
soup = BeautifulSoup(html, "html.parser")

# song_list = soup.select('div.o-chart-results-list-row-container li.lrv-u-width-100p h3#title-of-a-story')
song_list = soup.select('div ul li ul li h3')
song_titles = [song.getText().strip() for song in song_list]
pprint.pprint(song_titles)
# print(len(song_titles))