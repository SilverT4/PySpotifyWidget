import os
if os.getcwd() != os.path.dirname(__file__):
    os.chdir(os.path.dirname(__file__))
from . import preferences
from .gui import window
wind = window.Window(baseName='spotify playback')
wind.mainloop()