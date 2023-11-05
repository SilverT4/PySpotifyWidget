# Basic spotify object stuff
from typing import Literal, Any, TypeAlias
__doc__ = """This class simply contains some Pythonic classes that make it a little bit easier to handle returned objects."""
SimpleArtistList:TypeAlias = list[dict[str,str|int|dict]]
CopyrightObject:TypeAlias = list[dict[str,str]]
class Image:
    def __init__(self, url:str, height:int, width:int):
        self.url = url
        self.height = height
        self.width = width

class SimplifiedArtistObject:
    def __init__(self, external_urls:dict[str,str], href:str, id:str, name:str, type:Literal['artist'], uri:str, images:list[dict[str,str|int]] = None, popularity:int = None, followers:dict[str,str|None|int] = None, genres:list[str] = None):
        self.external_urls = external_urls
        self.followers = followers
        self.genres = genres
        self.href = href
        self.id = id
        if images:
            self.images = [Image(**i) for i in images]
        else:
            self.images = [None]
        self.name = name
        self.popularity = popularity
        self.type = type
        self.uri = uri

class Track:
    def __init__(self, album:dict[str,str|int|bool|list[str]], artists:SimpleArtistList, disc_number:int, duration_ms:int, explicit:bool, external_ids:dict[str,str], external_urls:dict[str,str], href:str, id:str, name:str, popularity:int, preview_url:str|None, type:Literal['track'], uri:str, is_local:bool, track_number:int, is_playable:bool = None, linked_from:dict|None = None, restrictions:dict[str,str] | None = None, available_markets:list[str] |None= None):
        self.album = Album(**album)
        self.artists = [SimplifiedArtistObject(**a) for a in artists]
        self.available_markets = available_markets
        self.disc_number = disc_number
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.external_ids = external_ids
        self.external_urls = external_urls
        self.id = id
        self.href = href
        self.name = name
        self.popularity = popularity
        self.preview_url = preview_url
        self.type = type
        self.uri = uri
        self.is_local = is_local
        self.is_playable = is_playable
        self.linked_from = linked_from
        self.restrictions = restrictions
        self.track_number = track_number

class Show:
    def __init__(self, available_markets:list[str], copyrights:CopyrightObject, description:str, html_description:str, explicit:bool, external_urls:dict[str,str], href:str, id:str, images:list[dict[str,str|int]], is_externally_hosted:bool, languages:list[str], media_type:str, name:str, publisher:str, type:Literal['show'], uri:str, total_episodes:int):
        self.available_markets = available_markets
        self.copyrights = copyrights
        self.description = description
        self.html_description = html_description
        self.explicit = explicit
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.images = [Image(**i) for i in images]
        self.is_externally_hosted = is_externally_hosted
        self.languages = languages
        self.media_type = media_type
        self.name = name
        self.publisher = publisher
        self.type = type
        self.uri = uri
        self.total_episodes = total_episodes
class Episode:
    def __init__(self, audio_preview_url:str|None, description:str, html_description:str, duration_ms:int, explicit:bool, external_urls:dict[str,str], href:str, id:str, images:list[dict[str,str|int]], is_externally_hosted:bool, is_playable:bool, language:str, languages:list[str], name:str, release_date:str, release_date_precision:Literal['year','month','day'], type:Literal['episode'], uri:str, show:dict, restrictions:dict[str,str]|None = None, resume_point:dict[str,bool|int] | None = None):
        self.audio_preview_url = audio_preview_url
        self.description = description
        self.html_description = html_description
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.images = [Image(**i) for i in images]
        self.is_externally_hosted = is_externally_hosted
        self.is_playable = is_playable
        self.language = language
        self.languages = languages
        self.name = name
        self.release_date = release_date
        self.release_date_precision = release_date_precision
        self.resume_point = resume_point
        self.type = type
        self.uri = uri
        self.show = Show(**show)
        self.restrictions = restrictions

class Album:
    """
    Represents a Spotify album. This object's fields are based off of the Spotify API documentation."""
    def __init__(self, album_type:Literal['album','single','compilation'], total_tracks:int, href:str, id:str, images:list[dict[str,str|int]], name:str, release_date:str, release_date_precision:Literal['year','month','day'], type:Literal['album'], uri:str, external_urls:dict[str,str], artists:SimpleArtistList, copyrights:CopyrightObject = None, tracks:dict[str,str|dict|int] = None, is_playable = True, label:str = None, popularity:int=None,genres:list[str]=None,available_markets:list[str]=None, restrictions=None):
        self.name = name
        self.external_urls = external_urls
        self.album_type = album_type
        self.type = type
        self.total_tracks = total_tracks
        self.available_markets = available_markets
        self.href = href
        self.id = id
        self.uri = uri
        self.images = [Image(**i) for i in images]
        self.release_date = release_date
        self.release_date_precision = release_date_precision
        self.genres = genres
        self.label = label
        self.popularity = popularity
        self.copyrights = copyrights
        self.artists = [SimplifiedArtistObject(**a) for a in artists]
        self.restrictions = restrictions
class Artist:
    def __init__(self, external_urls:dict[str,str], followers:dict[str,str|int], genres:list[str], href:str, id:str, images:list[dict[str,str|int]], name:str, popularity:int, type:Literal['artist'], uri:str):
        self.external_urls = external_urls
        self.followers = followers
        self.genres = genres
        self.href = href
        self.id = id
        self.images = [Image(**i) for i in images]
        self.name = name
        self.popularity = popularity
        self.type = type
        self.uri = uri

class Playlist:
    def __init__(self, collaborative:bool=None, description:str = None, external_urls = None, followers = None, href:str = None, id:str = None, images = None, name:str = None, owner = None, public:bool = None, snapshot_id:str = None, tracks = None, type:Literal['playlist'] = 'playlist', uri:str = None) -> None:
        "since you can select fields with this one, all fields are optional.s"
        self.collaborative = collaborative
        self.description = description
        self.external_urls = external_urls
        self.followers = followers
        self.href = href
        self.id = id
        if images:
            self.images = [Image(**i) for i in images]
        else:
            self.images = [None]
        self.name = name
        self.owner = owner
        self.public = public
        self.snapshot_id = snapshot_id
        self.tracks = tracks
        self.type = type
        self.uri = uri
class Device:
    def __init__(self, id:str, is_active:bool, is_private_session:bool, is_restricted:bool, name:str, supports_volume:bool, type:Literal['Computer','Smartphone','Speaker'], volume_percent:int):
        self.id = id
        self.is_active = is_active
        self.is_private_session = is_private_session
        self.is_restricted = is_restricted
        self.name = name
        self.type = type
        self.supports_volume = supports_volume
        self.volume_percent = volume_percent

class Actions:
    def __init__(self, interrupting_playback:bool = False, pausing:bool = False, resuming:bool = False, seeking:bool = False, skipping_next:bool = False, skipping_prev:bool = False, toggling_repeat_context:bool = False, toggling_shuffle:bool = False, toggling_repeat_track:bool = False, transferring_playback:bool = False):
        self.interrupting_playback = interrupting_playback
        self.pausing = pausing
        self.resuming = resuming
        self.seeking = seeking
        self.skipping_next = skipping_next
        self.skipping_prev = skipping_prev
        self.toggling_repeat_context = toggling_repeat_context
        self.toggling_repeat_track = toggling_repeat_track
        self.toggling_shuffle = toggling_shuffle
        self.transferring_playback = transferring_playback

class Context:
    def __init__(self, type:Literal['album','artist','playlist','show'], href:str, external_urls:dict[str,str], uri:str):
        self.type = type
        self.href = href
        self.external_urls = external_urls
        self.uri = uri
class Player:
    def __init__(self, device:dict[str,str|bool|int], repeat_state:Literal['context','track','off'], shuffle_state:bool, timestamp:int, progress_ms:int | None, is_playing:bool, currently_playing_type:Literal['track','episode','ad','unknown'], actions:dict[str,dict[str,bool]], context:dict[str,str|dict[str,str]] = None, item:dict[str,str|dict|int|bool] = None) -> None:
        self.device = Device(**device)
        self.repeat_state = repeat_state
        self.shuffle_state = shuffle_state
        self.timestamp = timestamp
        self.progress_ms = progress_ms
        self.is_playing = is_playing
        self.currently_playing_type = currently_playing_type
        if 'disallows' in actions:
            self.actions = Actions(**actions['disallows'])
        else:
            self.actions = Actions() # Blank if the actions are not applicable.
        if context:
            self.context = Context(**context)
        else:
            self.context = None
        if item:
            if item['type'] == 'episode':
                self.item = Episode(**item)
            elif item['type'] == 'track':
                self.item = Track(**item)
        else:
            self.item = None
        