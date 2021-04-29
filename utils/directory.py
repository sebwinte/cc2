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
        self.unique_folder_id = ''
    

    # make_dir creates a new directory based on the filename
    # If the directory already exists, a unique id is added  

    def make_dir(self,path,file_name,access_rights):
        try:
            if os.path.exists(path+file_name):
                self.unique_folder_id = str(uuid4())
                os.mkdir(path + file_name + self.unique_folder_id, access_rights)
            else:
                os.mkdir(path+file_name, access_rights)
        except OSError:
            print ("Creation of the directory %s failed" % path+file_name)
            return 0 
        else:
            print ("Successfully created the directory %s" % path+file_name)
            return self.unique_folder_id


    # move_files cuts out the original video and moves it into the according directory

    def move_files(self,original_path,folder_path,file_name,unique_folder_id):
        try:
            if os.path.exists(folder_path + original_path):
                original = folder_path + original_path
                target = folder_path + file_name + unique_folder_id
                shutil.move(original,target)
                return True
            else:
                return False
        except:
            return False

       

