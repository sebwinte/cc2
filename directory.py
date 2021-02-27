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



    def move_files(self,originalPath,path, file_name):
        original = originalPath
        target = 'testordner/'+file_name
        
        try:
            print(original)
            print(target)
            shutil.move(original,target)
        except OSError:
            print (f'Error during move')
        else:
            print (f'File successfully moved')
    
