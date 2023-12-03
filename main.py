import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"
user_date = "2008-10-01" #input("Which year do you want a music list from? Type te date in this format YYYY-MM_DD\n")

response = requests.get(url=f"{URL}{user_date}")
site_data = response.text

soup = BeautifulSoup(site_data, "html.parser")
song_names = soup.select("li ul li h3")

music_list = [title.getText().strip() for title in song_names]
print(music_list)
