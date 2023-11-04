from tkinter import ttk
import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import Image
from ..backends import images
class InfoScreen(tk.Frame):
    def __init__(self, master:tk.Misc|None = None, **cnf):
        super().__init__(master, cnf)
        self.img = PhotoImage(Image.new('RGBA',(64,64),0x899FB5),master=self)
        self.aCover = tk.Label(self, image=self.img)
        self.aCover.image = self.img
        self.aCover.grid(row=0,column=0)
        self.infoText = tk.StringVar(self,"""Never Gonna Give You Up\nRick Astley\nWhen You Need Somebody\n1:11/3:33""")
        self.infoLbl = tk.Label(self, textvariable=self.infoText, justify='left')
        self.infoLbl.grid(row=0,column=1,sticky='w')
        self.pvar = tk.DoubleVar(self,0.33)
        self.pbar = ttk.Progressbar(self,maximum=1,variable=self.pvar)
        self.pbar.grid(row=1,column=0,sticky='ew',columnspan=2)