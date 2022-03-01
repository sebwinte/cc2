import os
import shutil
import threading
import time
from uuid import uuid4
import os.path
from os import path



class Directory:
    
    '''
        cc2 Directory
        ----------
        This class creates a new directory for every video and
        moves all files into it.
    '''
    


    def __init__(self):
        self.folder_id = 1


    # make_dir creates a new directory based on the filename
    # If the directory already exists, a unique id is added  

    def make_dir(self,video):
        try:
            if os.path.exists(video.folder_path + video.file_name_without_arguments) == False :
                os.mkdir(video.folder_path + video.file_name_without_arguments, 0o777)
            else:
                while os.path.exists(video.folder_path + video.file_name_without_arguments + "("+str(self.folder_id) + ")"):
                    self.folder_id += 1
                os.mkdir(video.folder_path + video.file_name_without_arguments + "("+str(self.folder_id) + ")", 0o777)
                video.set_uniq_id(self.folder_id)
        except OSError:
            print ("Creation of the directory failed")
            return False
        else:
            print ("Successfully created the director")
            return True



    # move_files cuts out the original video and moves it into the according directory

    def move_files(self,video):
        try:
            if os.path.exists(video.path):
                original = str(video.path)
                target = str(video.folder_path + video.file_name_without_arguments + video.uniq_id)
                shutil.move(original,target)
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

       

