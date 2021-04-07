import os
import shutil
import threading
import time
from utils.helper import Helper

import os.path
from os import path


class Directory:
    
    '''
        cc2 Directory
    '''
    


    def __init__(self):
        self.uniq_folder_id = ''
    

    '''
    Create a new Directory
        If the Directory already exists, add a uniq id at the end of the name
        The Directory is named after the video file
    '''
    def make_dir(self, video, access_rights):
        try:
            if os.path.exists(video.path+video.file_name):
                os.mkdir(Helper.path + video.file_name_without_arguments + video.uniq_id, access_rights)
            else:
                 os.mkdir(Helper.path+video.file_name_without_arguments, access_rights)
        except OSError:
            print ("Creation of the directory %s failed" % video.path+video.file_name)
            return 0 
        else:
            print ("Successfully created the directory %s" % video.path+video.file_name)
            return 1


    def get_folder_id(self):
        return self.uniq_folder_id


    '''
    Move the video file
        After the videos have been sucessfully converted, the original video file is moved 
        into the newly created directory
    '''
    def move_files(self,video):
        try:
            if os.path.exists(video.folder_path + video.originalPath):
                original = video.folder_path + video.originalPath
                target = video.folder_path + video.file_name + video.uniq_id
                shutil.move(original,target)
                return True
            else:
                return False
        except:
            return False

       

