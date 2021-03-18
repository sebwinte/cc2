import os
import shutil
import threading
import time
from uuid import uuid4
import os.path
from os import path


class Directory:
    
    '''
        cc2 Create directories
        Attributes
        ----------
        path: name of the directory to be created 
        access_rights: define the access rights
    '''
    
    def __init__(self):
        pass
    

    
    def make_dir(self, path, file_name, access_rights):
        uniq_id = ''
        try:
            if os.path.exists(path+file_name):
                uniq_id = str(uuid4())
                os.mkdir(path + file_name + uniq_id, access_rights)
            else:
                 os.mkdir(path+file_name, access_rights)
        except OSError:
            print ("Creation of the directory %s failed" % path+file_name)
            return 0 
        else:
            print ("Successfully created the directory %s" % path+file_name)
            return uniq_id



    def move_files(self,originalPath,folder_path, file_name ,uniq_id):
        try:
            original = folder_path + originalPath
            target = folder_path + file_name + uniq_id
            shutil.move(original,target)
            return True
        except:
            return False

       

