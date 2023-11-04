from tkinter import ttk
import tkinter as tk
from requests.exceptions import ReadTimeout
from PIL.ImageTk import PhotoImage
from PIL import Image
from ..backends import images, api
from ..spotify import Objects
from os.path import basename, dirname, join
from getpass import getuser
from .. import preferences
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
        self.img = PhotoImage(Image.open(self.ifname).resize(images.size),master=self)
        self.aCover = tk.Label(self, image=self.img)
        self.aCover.image = self.img
        self.aCover.grid(row=0,column=0)
        self.infoText = tk.StringVar(self,"""Never Gonna Give You Up\nRick Astley\nWhen You Need Somebody\n1:11/3:33""")
        self.placeholder_txt = "Never Gonna Give You Up\nRick Astley\nWhen You Need Somebody\n1:11/3:33"
        self.infoLbl = tk.Label(self, textvariable=self.infoText, justify='left')
        self.infoLbl.grid(row=0,column=1,sticky='w')
        self.pvar = tk.DoubleVar(self,0.33)
        self.pbar = ttk.Progressbar(self,maximum=1,variable=self.pvar)
        self.pbar.grid(row=1,column=0,sticky='ew',columnspan=2)
        self.bind("<<RedownloadImage>>", self.redownload_image)
        self.retries = 0
        self.refresh()

    def redownload_image(self, e:tk.Event=None): # e is default to None for manual calls
        fname = images.downloadImage(self.imageUrl)
        images.toTkImage(fname, self.img)
    def refresh(self):
        try:
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
                match preferences.window_title_mode:
                    case 'context':
                        if cplay.context != None:
                            ctx = self.client.get_context_by_uri(cplay.context.uri,cplay.context.type)
                            self.tk.call("wm","title",".",ctx.name)
                        else:
                            self.tk.call("wm","title",".","Custom Spotify Playback Widget")
                    case 'item':
                        if cplay.item != None:
                            self.tk.call("wm","title",".",cplay.item.name)
                        else:
                            self.tk.call("wm","title",".","Custom Spotify Playback Widget")
                    case 'custom':
                        if preferences.custom_title:
                            self.tk.call("wm","title",".",preferences.custom_title)
                        else:
                            self.tk.call("wm","title",".",getuser())
                    case 'none':
                        self.tk.call("wm","title",".","Custom Spotify Playback Widget")
            else:
                self.ifname = self.placeholder_img
                self.img.paste(Image.open(self.ifname).resize(images.size))
                self.infoText.set(self.placeholder_txt)
                self.pbar.configure(maximum=213000,value=71000)
                if preferences.window_title_mode == 'custom':
                    self.tk.call("wm","title",".",getuser())
                else:
                    self.tk.call("wm","title",".","Custom Spotify Playback Widget")
            self.retries = 0 # reset the counter
            self.after(150, self.refresh)
        except ReadTimeout:
            self._readTimeout()
    
    def _readTimeout(self):
        self.retries += 1
        self.infoText.set("Could not connect to Spotify,\nread timed out.\nAttempt %d\nRetrying in 5..." % self.retries)
        _4 = "Could not connect to Spotify,\nread timed out.\nAttempt %d\nRetrying in 4..." % self.retries
        _3 = "Could not connect to Spotify,\nread timed out.\nAttempt %d\nRetrying in 3..." % self.retries
        _2 = "Could not connect to Spotify,\nread timed out.\nAttempt %d\nRetrying in 2..." % self.retries
        _1 = "Could not connect to Spotify,\nread timed out.\nAttempt %d\nRetrying in 1..." % self.retries
        _0 = "Could not connect to Spotify,\nread timed out.\nAttempt %d\nRetrying..." % self.retries
        self.pbar.configure(maximum=5)
        self.pvar.set(5)
        self.after(1000,self.pvar.set,4)
        self.after(2000,self.pvar.set,3)
        self.after(3000,self.pvar.set,2)
        self.after(4000,self.pvar.set,1)
        self.after(5000,self.pvar.set,0)
        self.after(1000,self.infoText.set,_4)
        self.after(2000,self.infoText.set,_3)
        self.after(3000,self.infoText.set,_2)
        self.after(4000,self.infoText.set,_1)
        self.after(5000,self.infoText.set,_0)
        self.after(5000,self.refresh)