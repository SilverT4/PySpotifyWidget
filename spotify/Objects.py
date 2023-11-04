# Basic spotify object stuff
from typing import Literal, Any, TypeAlias

SimpleArtistList:TypeAlias = list[dict[str,str|int|dict]]
CopyrightObject:TypeAlias = list[dict[str,str]]
class Image:
    def __init__(self, url:str, height:int, width:int):
        self.url = url
        self.height = height
        self.width = width

class Album:
    """
    Represents a Spotify album. This object's fields are based off of the Spotify API documentation."""
    def __init__(self, album_type:Literal['album','single','compilation'], total_tracks:int, available_markets:list[str], href:str, id:str, images:list[dict[str,str|int]], name:str, release_date:str, release_date_precision:Literal['year','month','day'], type:Literal['album'], uri:str, genres:list[str], label:str, popularity:int, external_urls:dict[str,str], artists:SimpleArtistList, copyrights:CopyrightObject, tracks:dict[str,str|dict|int]):
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
        #self.tracks = TracksHolder(**tracks)

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

