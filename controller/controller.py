from utils.convert import Converter
from utils.directory import Directory
import time
import threading
from utils.helper import Helper
import os.path
from os import path
from pathlib import Path



class Controller:

    '''
        cc2 Controller
    '''



    def __init__(self):
        self.dir = Directory()
        self.conv = Converter()
        self.h = Helper()


    '''
    Process
        
    '''
    def process(self,file_name_without_arguments,arguments,original_file_path,file_name_without_arguments_extension,cropped_file_extension,original_file_name):

        verified_arguments_compression = self.verify_arguments_compression(arguments)
        verified_arguments_typ = self.verify_arguments_typ(arguments)
        
        uniq_folder_id = self.dir.make_dir(Helper.path,file_name_without_arguments,0o777)

        if self.conv.manage_video_compression(verified_arguments_compression,verified_arguments_typ,file_name_without_arguments,original_file_name,uniq_folder_id):
            if self.dir.move_files(original_file_name,Helper.path,file_name_without_arguments,uniq_folder_id):
                self.h.message("CC2","Your video has been successfully converted")
            else: return   
        else: return   


    '''
    Verify arguments
        Return only valid arguments according to the Helper.valid_arguments_ list 
    '''
    def verify_arguments_compression(self,arguments):
        valid_arguments = []
        try:
            for param in arguments:
                if param.lower() in Helper.valid_arguments_compression:
                    valid_arguments.append(param.lower())
            return valid_arguments
        except:
            return False    


    def verify_arguments_typ(self,arguments):
        valid_arguments = []
        try:
            for param in arguments:
                if param.lower() in Helper.valid_arguments_typ:
                    valid_arguments.append(param.lower())
            return valid_arguments
        except:
            return False    


    

