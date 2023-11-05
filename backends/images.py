import os, platform, warnings, random, string
from urllib.request import urlretrieve
from urllib import error
from PIL import Image
from .. import preferences
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

if not os.path.exists(cacheDir):
    os.mkdir(cacheDir)

def downloadImage(url):
    dest = os.path.join(cacheDir,os.path.basename(url))
    if not os.path.exists(dest):
        try:
            print("attempting to retrieve",url)
            urlretrieve(url,dest)
            return dest
        except error.HTTPError:
            return None
    else: return dest # Don't download the same image multiple times.
size = preferences.img_size,preferences.img_size
def toTkImage(fname:str, widg):

    img = Image.open(fname).resize(size)
    widg.paste(img)