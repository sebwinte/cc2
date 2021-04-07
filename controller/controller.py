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
    '''



    def __init__(self):
        self.dir = Directory()
        self.conv = Converter()
        self.h = Helper()


    '''
    Process
        
    '''
    #def process(self,file_name_without_arguments,arguments,original_file_path,file_name_without_arguments_extension,cropped_file_extension,original_file_name):
    def process(self,video):
        print("process")
        print(video)

        
        self.dir.make_dir(video,0o777)

        if self.conv.manage_video_compression(video):
            if self.dir.move_files(video):
                self.h.message("CC2","Your video has been successfully converted")
            else: return   
        else: return   

        

    

