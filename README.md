# "Billboard Hot 100 Playlist Creator"
<br />
</br>

## Overview

This Python application automates the creation of Spotify playlists based on Billboard's Hot 100 chart for a given date. 
It scrapes song data from the Billboard website and uses the Spotify API to search for these tracks and generate a personalized playlist.
<br />


## Features

1. Scrape Billboard's Hot 100 chart for any given date.
2. Automatically search for songs on Spotify.
3. Create a Spotify playlist with the found tracks.



## Prerequisites 
To run this project, you will need:

+ **Python:** The application is written in Python(3.6 and above), a recent version of [Python](https://www.python.org/downloads/).
+ **Pip:** Python's package installer, pip, should be installed for managing Python packages. It usually comes with Python installation.
+ **APIs:** Spotify Developer Account for API credentials.

## Installation

- **Clone the Repository:** git clone https://github.com/SonnyGU/SpotifyPlaylistByDate.git
- **Install the Requests library using pip:** pip install requests beautifulsoup4 spotipy
- **Run the Application:** python main.py

## Setup

1. Set up your Spotify Developer account and create an application to obtain your Client ID, Client Secret, and Redirect URI.
2. Set the following environment variables:
  - SPOTIFY_CLIENT_ID
  - SPOTIFY_SECRET_ID
  - SPOTIFY_REDIRECT_URL
  - SPOTIFY_USERNAME


## Program walk-through:

<p align="center">
Launch the utility: <br/>
<img src="https://i.imgur.com/dHm4kV2.png" height="60%" width="60%" alt="Playlist creation Steps"/>
<br />
<br />
Enter Date when prompted:  <br/>
<img src="https://i.imgur.com/L7cNlL7.png" height="70%" width="70%" alt="Playlist creation Steps"/>
<br />
<br /> 
A new playlist will be created and populated:    <br/>
<img src="https://i.imgur.com/HvoyvMh.png" height="30%" width="30%" alt="Playlist creation Steps"/>
<br />
<br />
<br/>
<img src="https://i.imgur.com/JfdhTwk.png" height="70%" width="70%" alt="Playlist creation Steps"/>
<br />
<br />
The original Billboard Hot 100 site:    <br/>
<img src="https://i.imgur.com/DvxsnBH.png" height="70%" width="70%" alt="Playlist creation Steps"/>
<br />
<br />



<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
