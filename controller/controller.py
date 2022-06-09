from utils.convert import Converter
from utils.directory import Directory
from utils.helper import Helper



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
            video.update_status("converting")
            if(self.conv.manage_filetype_compression(video)):
                if(self.dir.move_files(video)):
                    self.h.notification_message("cc2","Your video has been successfully converted")
                    video.update_status("finished")
                else:
                    video.update_status("error")
            else:
                video.update_status("error")
        else:
            video.update_status("error")
