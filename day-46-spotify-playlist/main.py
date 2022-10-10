from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

date = input("Which year do you want to go back to(YYYY-MM-DD): ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
# To view the results of the song search. used later
pp = pprint.PrettyPrinter(depth=5)

response = requests.get(URL)
content = response.text
soup = BeautifulSoup(content, "html.parser")

# Create a list that contains the correct tag elements we are after
tags = soup.find_all("h3", class_="a-no-trucate")
# Get the text and strip all the \t\n etc
song_names = [tag.getText().strip() for tag in tags]

# https://spotipy.readthedocs.io/en/2.13.0/#
# instantiate the class and create an oauth token into a text file. Note we had to create an app at
# https://developer.spotify.com/dashboard/applications and edit the settings and add in a redirect URI which was
# http://example.com and then enter the full redirect URL into the prompt at the console.
sp = spotipy.Spotify(
     auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)


song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    #pp.pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#print(song_uris)

# Create a new private playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# Add tracks to the playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)