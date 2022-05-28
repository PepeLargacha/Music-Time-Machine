"""
To make it work, you have to have an account on Spotify, and create
a new app on: "https://developer.spotify.com/"
After that you need to edit settings on the app and add the following
Redirect URIs: "http://example.com/"
Then you'll need to set the environment variables:

SPOTIFY_CLIENT_ID: "your client id"
SPOTIFY_CLIENT_SECRET: "your client secret"

Then the first time you run the program it will ask you to input on
the console, the page address that show on browser address bar after you
autorize your app.
After that you can run the program again and it will work as planned.
"""
from ui import get_year_from_user
from spotify_api import MySpotify
from billboardsouper import BillboardScraper

my_scraper = BillboardScraper(get_year_from_user())
my_spotify = MySpotify()
my_spotify.get_list_of_songs_uri(my_scraper.song_list)
my_spotify.create_playlist(my_scraper.target_date)
my_spotify.populate_playlist()
