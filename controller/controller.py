from utils.convert import Converter
from utils.directory import Directory
import time
import threading
from utils.helper import Helper
import os.path
from os import path
from pathlib import Path



class Controller:

    '''
        cc2 Controller
        ----------
        This class initiates the converting process.  
    '''



    def __init__(self):
        self.dir = Directory()
        self.conv = Converter()
        self.h = Helper()


    def process(self,video):
        
        if(self.dir.make_dir(video)):
            time.sleep(1)
            if(self.conv.manage_filetype_compression(video)):
                time.sleep(1)
                if(self.dir.move_files(video)):
                    self.h.notification_message("cc2","Your video has been successfully converted")
