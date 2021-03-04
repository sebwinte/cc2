import os
import shutil

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
        try:
            os.mkdir(path+file_name, access_rights)
        except OSError:
            print ("Creation of the directory %s failed" % path+file_name)
        else:
            print ("Successfully created the directory %s" % path+file_name)



    def move_files(self,originalPath,folder_path, file_name):
        original = folder_path + originalPath
        target = folder_path + file_name

        try:
            shutil.move(original,target)
        except OSError:
            print (f'Error during move')
        else:
            print (f'File successfully moved')
    
