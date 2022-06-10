from PIL import Image, ImageDraw
from pystray import Icon as icon, Menu as menu, MenuItem as item
from pathlib import Path
import os , sys 

from utils.helper import Helper


class Tray:
    
    '''
        cc2 Tray
        ----------
        This class creates a Tray
    '''
    
    def __init__(self):
        self.h = Helper()
        self.image = Image.open(Path("doc/logo.png"))
        


    def on_clicked(self,icon, item):
        if(str(item)=="EXIT"):
            icon.stop()
            os._exit(0)

        if(str(item)=="Reload Settings"):
            print("Reloading Settings")
            self.h.load_settings()
             

    def run(self):
        icon('cc2', self.image, 
            menu=menu(
                item(
                    'Documentation',
                    self.on_clicked
                ),
                item(
                    'Reload Settings',
                    self.on_clicked
                ),
                item(
                    'EXIT',
                    self.on_clicked,
                )
            )
        ).run_detached()

    
    
