"""Class for managing Spotify API."""
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL_REDIRECT = "http://example.com/"


class MySpotify:
    """Manage the functions on Spotipy Library"""
    def __init__(self):
        self.client_id = os.environ.get('SPOTIFY_CLIENT_ID')
        self.client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')
        self.spotify = self.create_user()
        self.current_user = self.spotify.current_user()['id']

    def create_user(self):
        spotify = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                        client_id=self.client_id,
                        client_secret=self.client_secret,
                        redirect_uri=URL_REDIRECT,
                        scope='playlist-modify-private',
                        show_dialog=True,
                        cache_path="token.txt"))
        return spotify

    def get_list_of_songs_uri(self, a_list: list) -> list:
        uri_list = []
        for song in a_list:
            song_name = song[0]
            artist_name = song[1]
            uri = self.spotify.search(q=f"track:{song_name} \
                artist:{artist_name}", type='track', limit=1)
            try:
                uri_list.append(uri['tracks']['items'][0]['uri'])
            except IndexError:
                pass
        return uri_list

    def create_playlist(self, year) -> str:
        playlist = self.spotify.user_playlist_create(
            self.current_user, f'Billboard top 100 - {year}', public=False)
        return playlist['id']

    def populate_playlist(self, playlist_id: str, uri_list: list):
        self.spotify.user_playlist_add_tracks(
            self.current_user, playlist_id, uri_list)
        print('Playlist created and populated!')
