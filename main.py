import requests
import os
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Retrieve Spotify API credentials from environment variable
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_SECRET_ID = os.getenv("SPOTIFY_SECRET_ID")
SPOTIFY_REDIRECT = os.getenv("SPOTIFY_REDIRECT_URL")
SPOTIFY_USERNAME = os.getenv("SPOTIFY_USERNAME")

# ULR of the Billboard Hot 100 Chart
URL = "https://www.billboard.com/charts/hot-100/"

# Prompts user for date input in YYY-MM-DD
user_date = input("Which year do you want a music list from? Type te date in this format YYYY-MM_DD\n")

# Initialize Spotify client with user authorization
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIFY_REDIRECT,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_SECRET_ID,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_USERNAME,
    )
)

# Request the webpage of the Billboard Hot 100 chart for the given date
response = requests.get(url=f"{URL}{user_date}")
site_data = response.text

# Parse the HTML content of the webpage
soup = BeautifulSoup(site_data, "html.parser")

# Select the HTML elements that contain song names
song_names = soup.select("li ul li h3")

# Extract and clean the text from the selected elements to get a list of song names
music_list = [title.getText().strip() for title in song_names]
# print(music_list) # Test Print

# Get the current Spotify user's ID
user_id = sp.current_user()["id"]

# Initialize a list to store Spotify URIs of songs
song_uri_list = []
date_year = user_date.split("-")[0]

# Search for each song on Spotify and add its URI to the list
for name in music_list:
    found = sp.search(q=f"track:{name} year:{date_year}", type="track")
    print(found)
    try:
        uri = found["tracks"]["items"][0]["uri"]
        song_uri_list.append(uri)
    except IndexError:
        print(f"{name} Not Found ")

# Create a new private playlist for the user with the songs from the specified year
playlist = sp.user_playlist_create(user=user_id, name=f"{date_year} Billboard 100", public=False)
# print(playlist) # test print

# Add the found songs to the newly created playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri_list)
