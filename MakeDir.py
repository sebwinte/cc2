# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sun Feb 14 19:38:47 2021

# @author: tom
# """

import os
import shutil

class MakeDir:
    
    '''
        cc2 Create directories
        Attributes
        ----------
        path: name of the directory to be created 
        access_rights: define the access rights
    '''
    
    def __init__(self, path, file_name, access_rights):
        self.path = path
        self.file_name = file_name
        self.access_rights = access_rights
    
    def make_dir(self):
        try:
            os.mkdir(self.path+self.file_name, self.access_rights)
        except OSError:
            print ("Creation of the directory %s failed" % self.path+self.file_name)
        else:
            print ("Successfully created the directory %s" % self.path+self.file_name)
    
        
    def get_details(self):
        print(f'Your directory: {self.path}, your access rights {self.access_rights}')
        
            
class MoveFiles(MakeDir):
    
    '''
        cc2 Move files to directory
    '''
    
    def __init__(self, path, file_name, access_rights):
        super().__init__(path, file_name, access_rights)
    
    def move_files(self):
        original = r'/Users/tom/Downloads/test.txt'
        target = self.path+self.file_name
        
        try:
            shutil.move(original,target)
        except OSError:
            print (f'Error during move')
        else:
            print (f'File successfully moved')
                       
            
            
            
make = MakeDir("/Users/tom/Downloads/", "bucky_final", 0o777)
make.make_dir()
make.get_details()
move = MoveFiles("/Users/tom/Downloads/", "bucky_final", 0o777)
move.move_files()
