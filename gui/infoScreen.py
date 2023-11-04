from tkinter import ttk
import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import Image
from ..backends import images, api
from ..spotify import Objects
from os.path import basename, dirname, join
def formatTime(progress:int, duration:int|None = None):
    p_s, p_ms = divmod(progress, 1000)
    p_m, p_s = divmod(p_s, 60)
    progStr = "%d:%s" % (p_m, p_s if p_s > 10 else '0%d' % p_s)
    if duration:
        d_s, d_ms = divmod(duration,1000)
        d_m, d_s = divmod(d_s, 60)
        duraStr = "%d:%s" % (d_m, d_s if d_s > 10 else '0%d' % d_s)
        return "%s / %s" % (progStr,duraStr)
    return '%s elapsed' % progStr

class InfoScreen(tk.Frame):
    def __init__(self, master:tk.Misc|None = None, **cnf):
        super().__init__(master, cnf)
        self.client = api.Client()
        self.placeholder_img = join(dirname(dirname(__file__)), "pomni_boowomp.png")
        self.ifname = join(dirname(dirname(__file__)), "pomni_boowomp.png")
        self.imageUrl = ''
        self.img = PhotoImage(Image.open(self.ifname).resize((96,96)),master=self)
        self.aCover = tk.Label(self, image=self.img)
        self.aCover.image = self.img
        self.aCover.grid(row=0,column=0)
        self.infoText = tk.StringVar(self,"""Never Gonna Give You Up\nRick Astley\nWhen You Need Somebody\n1:11/3:33""")
        self.infoLbl = tk.Label(self, textvariable=self.infoText, justify='left')
        self.infoLbl.grid(row=0,column=1,sticky='w')
        self.pvar = tk.DoubleVar(self,0.33)
        self.pbar = ttk.Progressbar(self,maximum=1,variable=self.pvar)
        self.pbar.grid(row=1,column=0,sticky='ew',columnspan=2)
        self.bind("<<RedownloadImage>>", self.redownload_image)
        self.refresh()

    def redownload_image(self, e:tk.Event=None): # e is default to None for manual calls
        fname = images.downloadImage(self.imageUrl)
        images.toTkImage(fname, self.img)
    def refresh(self):
        cplay = self.client.get_playback()
        if cplay:
            if cplay.item != None:
                self.pvar.set(cplay.progress_ms)
                self.pbar.configure(maximum=cplay.item.duration_ms)
                if isinstance(cplay.item, Objects.Episode):
                    if self.ifname != basename(cplay.item.images[0].url):
                        self.ifname = basename(cplay.item.images[0].url)
                        self.imageUrl = cplay.item.images[0].url
                        self.event_generate("<<RedownloadImage>>") # This *should* help with performance, not sure.
                else:
                    if self.ifname != basename(cplay.item.album.images[0].url):
                        self.ifname = basename(cplay.item.album.images[0].url)
                        self.imageUrl = cplay.item.album.images[0].url
                        self.event_generate("<<RedownloadImage>>") # This *should* help with performance, not sure.
                iformat = [cplay.item.name,
                           None,
                           None,
                           formatTime(cplay.progress_ms, cplay.item.duration_ms)]
                if isinstance(cplay.item, Objects.Track):
                    iformat[1] = ", ".join(artist.name for artist in cplay.item.artists)
                    iformat[2] = cplay.item.album.name
                else:
                    showName = cplay.item.show.name
                    showPublisher = cplay.item.show.publisher
                    if showName == showPublisher:
                        iformat[1] = showName
                        iformat[2] = ""
                    else:
                        iformat[1] = showName
                        iformat[2] = showPublisher
                self.infoText.set("%s\n%s\n%s\n%s" % (iformat[0],iformat[1],iformat[2],iformat[3]))
        else:
            self.ifname = self.placeholder_img
            self.img.paste(Image.open(self.ifname).resize((96,96)))
        self.after(150, self.refresh)