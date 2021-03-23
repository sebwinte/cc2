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
    '''
    


    def __init__(self):
        self.uniq_folder_id = ''
    

    '''
    Create a new Directory
        If the Directory already exists, add a uniq id at the end of the name
        The Directory is named after the video file
    '''
    def make_dir(self, path, file_name, access_rights):
        uniq_folder_id = '' #Uniq Folder-ID if Folder already exists
        try:
            if os.path.exists(path+file_name):
                uniq_folder_id = str(uuid4())
                os.mkdir(path + file_name + uniq_folder_id, access_rights)
            else:
                 os.mkdir(path+file_name, access_rights)
        except OSError:
            print ("Creation of the directory %s failed" % path+file_name)
            return 0 
        else:
            print ("Successfully created the directory %s" % path+file_name)
            return self.uniq_folder_id


    def get_folder_id(self):
        return self.uniq_folder_id


    '''
    Move the video file
        After the videos have been sucessfully converted, the original video file is moved 
        into the newly created directory
    '''
    def move_files(self,originalPath,folder_path, file_name ,uniq_folder_id):
        try:
            if os.path.exists(folder_path + originalPath):
                original = folder_path + originalPath
                target = folder_path + file_name + uniq_folder_id
                shutil.move(original,target)
                return True
            else:
                return False
        except:
            return False

       

