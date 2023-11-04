import os, platform, warnings, random, string
from urllib.request import urlretrieve
from urllib import error
from PIL import Image
home = os.path.expanduser("~")
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
match platform.system():
    case 'Linux':
        cacheDir = os.path.join(home,".cache","spotify-widget")
    case 'Windows':
        cacheDir = os.path.join(home,"AppData","Local","Temp","spotify-widget")
    case 'Darwin':
        cacheDir = os.path.join(home,"Library","Caches","spotify-widget")
    case _:
        cacheDir = os.path.join(os.path.dirname(__file__),".cache")

def downloadImage(url):
    dest = os.path.join(cacheDir,os.path.basename(url))
    try:
        urlretrieve(url,)
        return dest
    except error.HTTPError:
        return None

def toTkImage(fname:str, widg):
    img = Image.open(fname).resize((64,64))
    widg.paste(img)