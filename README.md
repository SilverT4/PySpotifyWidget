# Custom Spotify Playback Widget

This is a widget created in Python to display your current Spotify playback in a little window in the corner of your screen.

# Setup

## Installation requirements

This script requires Python 3.8+, as well as the following libraries. A full list of required libraries can be found in [requirements.txt](requirements.txt)

```
Pillow>=10.0
spotipy
requests
certifi
urllib3
charset-normalizer
idna
six
redis
```

## Setting up a Spotify application for API access

To get started, you'll need to create an application with Spotify. To do this, follow these steps:

1. Navigate to the [Spotify for Developers Dashboard](https://developer.spotify.com/dashboard)
2. Sign in with your Spotify account, if necessary.
3. Click on "Create app"
4. Give your app any name and description. Under "Redirect URI", spotipy recommends using `https://localhost:3008`. If you have a web server you can use, enter that.
5. Check the **Web API** box under "Which API/SDKs are you planning to use?". This will help ensure your application has API access.

## Setting up the widget to authenticate

After cloning the repository, you'll need to create a `.env` file, preferrably in the root of the cloned repository.

Your .env file should contain the following:

```env
SPOTIPY_CLIENT_ID=<your spotify client ID here>
SPOTIPY_CLIENT_SECRET=<your spotify client secret here>
SPOTIPY_REDIRECT_URI=<whatever URI is set up in your spotify application.>
SPOTIPY_AUTH_SCOPE=user-read-currently-playing user-read-playback-state
```

To get your client ID and secret, go back to the [dashboard](https://developer.spotify.com/dashboard), open the page for your application, and click the Settings button.

Under the "Basic Information" tab, copy the Client ID. Also click on the "View client secret" hyperlink, and copy that into your .env file.

# Configuration

### Cache directory

As it is right now, the cache directory used by the app is hardcoded in `backends/images.py` to one of four directories, depending on your system:

1. Windows: `%LocalAppData%\Temp\spotify-widget`
2. Linux: `~/.cache/spotify-widget`
3. macOS: `~/Library/Caches`
4. Fallback: `<repository path>/backends/.cache`

The fallback is for in case this application is being run on an unrecognised platform.

If you want to change this, replace lines 4-12 in [images.py](backends/images.py) with a custom cache directory.

Example:

```python
cacheDir = "~/.cache/spoti"
```

# API functions used by this application

This application relies primarily on the [Spotify Web API](https://developer.spotify.com/documentation/web-api), using the [spotipy](https://pypi.org/project/spotipy) library as a wrapper.

To be more specific on the API calls made, here's a list of endpoints and why they're called by this application.

1. `/me/player` - Get Playback State
    * Required permissions: `user-read-playback-state`
2. `/me/player/currently-playing` - Get Currently Playing Track
    * Required permissions: `user-read-currently-playing`
    * Call reason: This call is made to retrieve information about the currently playing track, if any, from the Spotify API. This is then used to display information about the current track's name, artists, and album, as well as its duration.