import tkinter as tk
from tkinter import ttk, colorchooser
try:
    from .infoScreen import InfoScreen
except ImportError:
    try:
        from infoScreen import InfoScreen
    finally:
        print("a")
from .. import preferences
class PbarCustom(tk.Toplevel):
    def __init__(self, master=None, **cnf):
        super().__init__(master,cnf)
        self.style = master.style
        self.exampleBar = ttk.Progressbar(self,value=50)
        self.exampleBar.grid(row=0,columnspan=999)
        tk.Label(self,text="filled bar colour:").grid(row=1,column=0)
        tk.Label(self,text="unfilled bar colour:").grid(row=1,column=1)
        self.fb = tk.StringVar(self,self.style.lookup("Horizontal.TProgressbar","background"))
        self.ub = tk.StringVar(self,self.style.lookup("Horizontal.TProgressbar","troughcolor"))
        tk.Button(self,textvariable=self.ub,command=self.show_unfill).grid(row=2,column=1)
        tk.Button(self,textvariable=self.fb,command=self.show_fill).grid(row=2,column=0)
        tk.Button(self,text="Done",command=self.destroy).grid(row=999,columnspan=999,sticky='ew')
    def show_fill(self):
        color = colorchooser.askcolor(initialcolor=self.fb.get())
        if color:
            self.fb.set(color[1])
            self.style.configure('Horizontal.TProgressbar',background=color[1])
    def show_unfill(self):
        color = colorchooser.askcolor(initialcolor=self.ub.get())
        if color:
            self.ub.set(color[1])
            self.style.configure('Horizontal.TProgressbar',troughcolor=color[1])
class PaletteWindow(tk.Toplevel):
    def __init__(self, master=None, **cnf):
        super().__init__(master, cnf)
        self.title("Choose a colour scheme")
        cats = ['gray','white','blue','blue_gray','green','orange','pink','purple']
        cmds = [self.show_gra,self.show_whi,self.show_blu,self.show_bgr,self.show_gre,self.show_ora,self.show_pin,self.show_pur]
        self.lv = tk.StringVar()
        self.listbox = tk.Listbox(self,listvariable=self.lv)
        for i,c in enumerate(cats):
            btn = tk.Button(self, text=c, command=cmds[i])
            btn.grid(row=0,column=i,sticky='ew')
        cbtn = tk.Button(self,text='custom',command=self.ask_cus)
        cbtn.grid(row=0,column=8,sticky='ew')
        self.listbox.grid(row=1,columnspan=9)
        self.sb = tk.Scrollbar(self,orient='vertical',command=self.listbox.yview)
        self.listbox['yscrollcommand'] = self.sb.set
        self.sb.grid(row=1,column=8,sticky='nsw')
        okbtn = tk.Button(self,text='ok',command=self.confirm)
        okbtn.grid(row=2,columnspan=5,sticky='ew')
        can = tk.Button(self, text='cancel', command=self.destroy)
        can.grid(row=2,column=5,columnspan=5,sticky='ew')

    def ask_cus(self):
        color = colorchooser.askcolor(initialcolor=self.cget('bg'))
        if color[1]:
            self.master.tk_setPalette(color[1])
            self.destroy()
    def show_gra(self):
        options = ['gray60', 'gray70', 'gray80', 'gray85', 'gray90', 'gray95']
        self.listbox.delete(0,'end')
        self.listbox.insert(0,*options)
    def show_whi(self):
        options = ['snow1', 'snow2', 'snow3', 'snow4', 'seashell1', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'bisque1', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff1', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'NavajoWhite1', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'LemonChiffon1', 'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk1', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'ivory1', 'ivory2', 'ivory3', 'ivory4', 'honeydew1', 'honeydew2', 'honeydew3', 'honeydew4', 'LavenderBlush1', 'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose1', 'MistyRose2', 'MistyRose3', 'MistyRose4', 'azure1', 'azure2', 'azure3', 'azure4']
        self.listbox.delete(0,'end')
        self.listbox.insert(0,*options)
    def show_blu(self):
        options = ['SlateBlue1', 'RoyalBlue1', 'blue1', 'DodgerBlue1', 'SlateBlue2', 'RoyalBlue2', 'blue2', 'DodgerBlue2', 'SlateBlue3', 'RoyalBlue3', 'blue3', 'DodgerBlue3', 'SlateBlue4', 'RoyalBlue4', 'blue4', 'DodgerBlue4']
        self.listbox.delete(0,'end')
        self.listbox.insert(0,*options)
    def show_bgr(self):
        options = ['SlateGray1', 'LightSteelBlue1', 'LightBlue1', 'LightCyan1', 'SlateGray2', 'LightSteelBlue2', 'LightBlue2', 'LightCyan2', 'SlateGray3', 'LightSteelBlue3', 'LightBlue3', 'LightCyan3', 'SlateGray4', 'LightSteelBlue4', 'LightBlue4', 'LightCyan4']
        self.listbox.delete(0,'end')
        self.listbox.insert(0,*options)
    def show_gre(self):
        options = ['DarkSlateGray1', 'aquamarine1', 'DarkSeaGreen1', 'SeaGreen1', 'PaleGreen1', 'SpringGreen1', 'green1', 'chartreuse1', 'OliveDrab1', 'DarkOliveGreen1', 'khaki1', 'LightGoldenrod1', 'LightYellow1', 'yellow1', 'gold1', 'DarkSlateGray2', 'aquamarine2', 'DarkSeaGreen2', 'SeaGreen2', 'PaleGreen2', 'SpringGreen2', 'green2', 'chartreuse2', 'OliveDrab2', 'DarkOliveGreen2', 'khaki2', 'LightGoldenrod2', 'LightYellow2', 'yellow2', 'gold2', 'DarkSlateGray3', 'aquamarine3', 'DarkSeaGreen3', 'SeaGreen3', 'PaleGreen3', 'SpringGreen3', 'green3', 'chartreuse3', 'OliveDrab3', 'DarkOliveGreen3', 'khaki3', 'LightGoldenrod3', 'LightYellow3', 'yellow3', 'gold3', 'DarkSlateGray4', 'aquamarine4', 'DarkSeaGreen4', 'SeaGreen4', 'PaleGreen4', 'SpringGreen4', 'green4', 'chartreuse4', 'OliveDrab4', 'DarkOliveGreen4', 'khaki4', 'LightGoldenrod4', 'LightYellow4', 'yellow4', 'gold4']
        self.listbox.delete(0,'end')
        self.listbox.insert(0,*options)
    def show_ora(self):
        options = ['goldenrod1', 'DarkGoldenrod1', 'RosyBrown1', 'IndianRed1', 'sienna1', 'burlywood1', 'wheat1', 'tan1', 'chocolate1', 'firebrick1', 'brown1', 'salmon1', 'LightSalmon1', 'orange1', 'DarkOrange1', 'coral1', 'tomato1', 'OrangeRed1', 'red1', 'goldenrod2', 'DarkGoldenrod2', 'RosyBrown2', 'IndianRed2', 'sienna2', 'burlywood2', 'wheat2', 'tan2', 'chocolate2', 'firebrick2', 'brown2', 'salmon2', 'LightSalmon2', 'orange2', 'DarkOrange2', 'coral2', 'tomato2', 'OrangeRed2', 'red2', 'goldenrod3', 'DarkGoldenrod3', 'RosyBrown3', 'IndianRed3', 'sienna3', 'burlywood3', 'wheat3', 'tan3', 'chocolate3', 'firebrick3', 'brown3', 'salmon3', 'LightSalmon3', 'orange3', 'DarkOrange3', 'coral3', 'tomato3', 'OrangeRed3', 'red3', 'goldenrod4', 'DarkGoldenrod4', 'RosyBrown4', 'IndianRed4', 'sienna4', 'burlywood4', 'wheat4', 'tan4', 'chocolate4', 'firebrick4', 'brown4', 'salmon4', 'LightSalmon4', 'orange4', 'DarkOrange4', 'coral4', 'tomato4', 'OrangeRed4', 'red4']
        self.listbox.delete(0,'end')
        self.listbox.insert(0,*options)
    def show_pin(self):
        options = ['DeepPink1', 'HotPink1', 'pink1', 'LightPink1', 'PaleVioletRed1', 'VioletRed1', 'DeepPink2', 'HotPink2', 'pink2', 'LightPink2', 'PaleVioletRed2', 'VioletRed2', 'DeepPink3', 'HotPink3', 'pink3', 'LightPink3', 'PaleVioletRed3', 'VioletRed3', 'DeepPink4', 'HotPink4', 'pink4', 'LightPink4', 'PaleVioletRed4', 'VioletRed4']
        self.listbox.delete(0,'end')
        self.listbox.insert(0,*options)
    def show_pur(self):
        options = ['maroon1', 'magenta1', 'orchid1', 'plum1', 'MediumOrchid1', 'DarkOrchid1', 'purple1', 'MediumPurple1', 'thistle1', 'maroon2', 'magenta2', 'orchid2', 'plum2', 'MediumOrchid2', 'DarkOrchid2', 'purple2', 'MediumPurple2', 'thistle2', 'maroon3', 'magenta3', 'orchid3', 'plum3', 'MediumOrchid3', 'DarkOrchid3', 'purple3', 'MediumPurple3', 'thistle3', 'maroon4', 'magenta4', 'orchid4', 'plum4', 'MediumOrchid4', 'DarkOrchid4', 'purple4', 'MediumPurple4', 'thistle4']
        self.listbox.delete(0,'end')
        self.listbox.insert(0,*options)
    def confirm(self):
        self.master.tk_setPalette(self.listbox.get('active'))
        self.destroy()
        
class Window(tk.Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "spotify-widget", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.tk_setPalette(preferences.app_theme)
        self.style = ttk.Style(self)
        self.style.configure('Horizontal.TProgressbar',background=preferences.prog_fill,troughcolor=preferences.prog_trough,pbarrelief=preferences.prog_relief,troughrelief=preferences.prog_trough_relief)
        self.menubar = tk.Menu(self,type='menubar',name='system')
        self.paletteMenu = tk.Menu(self.menubar,type='normal',name='theming',tearoff=0)
        self.paletteMenu.add_command(label="overall appearance",command=self.openThemeWindow)
        self.paletteMenu.add_command(label="progressbar appearance",command=self.openPbarWindow)
        self.menubar.add_cascade(label="Change app look",menu=self.paletteMenu)
        self.configure(menu=self.menubar)
        self.iScreen = InfoScreen(self)
        self.iScreen.grid()
        self.bind("<Configure>", self.reposition, '+')
    def reposition(self,e=None):
        self.geometry("+%d+%d" % (self.winfo_screenwidth()-self.winfo_reqwidth()-8,self.winfo_screenheight()-self.winfo_reqheight()-8))
    def openThemeWindow(self):
        wind = PaletteWindow(self)
        self.wait_window(wind)
    def openPbarWindow(self):
        wind = PbarCustom(self)
        self.wait_window(wind)
if __name__ == "__main__":
    app = Window()

    app.mainloop()