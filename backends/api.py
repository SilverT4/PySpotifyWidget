from spotipy import Spotify, SpotifyStateError, SpotifyOauthError, SpotifyException, SpotifyOAuth
from os import getenv
from dotenv import load_dotenv
from ..spotify import Objects
import warnings
load_dotenv()

class Client:
    client_id = getenv('SPOTIPY_CLIENT_ID')
    "The Spotify client ID."
    client_secret = getenv('SPOTIPY_CLIENT_SECRET')
    redirect = getenv('SPOTIPY_REDIRECT_URI','https://silvert4.github.io/spotify.html')
    auth_scope = getenv("SPOTIPY_AUTH_SCOPE","user-read-currently-playing user-read-playback-state playlist-read-private playlist-read-collaborative") # If you don't set the auth scope in a .env file, this'll be used.
    def __init__(self):
        self.auth = SpotifyOAuth(self.client_id, self.client_secret, self.redirect, scope=self.auth_scope, show_dialog=True, open_browser=True)
        self.client = Spotify(oauth_manager=self.auth)
        
    def get_playback(self):
        try:
            cplay = self.client.current_playback('US','episode')
            if cplay:
                return Objects.Player(**cplay)
            return None
        except SpotifyException as s:
            warnings.warn("Could not get current playback information! Details:\n%s (HTTP %d)" % (s.msg,s.code))