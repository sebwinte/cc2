import os
import shutil
import threading
import time
from uuid import uuid4
import os.path
from os import path
from pathlib import Path



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
            if os.path.exists(Path(video.folder_path,video.file_name_without_arguments)) == False :
                os.mkdir(Path(video.folder_path,video.file_name_without_arguments), 0o777)
            else:
                while os.path.exists(Path(video.folder_path,video.file_name_without_arguments + "("+str(self.folder_id) + ")")):
                    self.folder_id += 1
                os.mkdir(Path(video.folder_path,video.file_name_without_arguments + "("+str(self.folder_id) + ")"), 0o777)
              

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
                original = video.path
                target = Path(video.folder_path,video.file_name_without_arguments,video.uniq_id)
                shutil.move(original,target)
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False


    def status_file(self,path,file_name,status):
        try:
            if os.path.exists(path):
                if(status == "converting"):
                    with open(Path(path,status+"_"+file_name+".txt"), 'w'): pass
                elif(status == "finished"):
                    os.rename(Path(path,"converting_"+file_name+".txt") , Path(path,"finished_"+file_name+".txt"))
                elif(status == "delete"):
                    os.remove(Path(path,"finished_"+file_name+".txt"))
       
        except:
            print("ERROR @ status_file()")

       

