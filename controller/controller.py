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
        ----------
        This class initiates the converting process.  
    '''



    def __init__(self):
        self.dir = Directory()
        self.conv = Converter()
        self.h = Helper()


    # process 

    def process(self,file_name_without_arguments,arguments,original_file_path,file_name_without_arguments_extension,cropped_file_extension,original_file_name):

        verified_arguments_compression = self.verify_arguments_compression(arguments)
        verified_arguments_type = self.verify_arguments_type(arguments)
        
        unique_folder_id = self.dir.make_dir(Helper.path,file_name_without_arguments,0o777)
        print(unique_folder_id)
        if self.conv.manage_filetype_compression(verified_arguments_compression,verified_arguments_type,file_name_without_arguments,original_file_name,unique_folder_id):
            if self.dir.move_files(original_file_name,Helper.path,file_name_without_arguments,unique_folder_id):
                self.h.notification_message("cc2","Your video has been successfully converted")
            else: return   
        else: return   


    # verify_arguments_compression return only valid arguments according to the Helper.valid_arguments_ list 

    def verify_arguments_compression(self,arguments):
        valid_arguments = []
        try:
            for param in arguments:
                if param.lower() in Helper.valid_arguments_compression:
                    valid_arguments.append(param.lower())
            # Default if no compression argument found 
            if not valid_arguments:
                valid_arguments =  ["medium"]
            return valid_arguments
        except:
            return False   


    # verify_arguments_type return only valid arguments according to the Helper.valid_arguments_ list 

    def verify_arguments_type(self,arguments):
        valid_arguments = []
        try:
            for param in arguments:
                if param.lower() in Helper.valid_arguments_type:
                    valid_arguments.append(param.lower())
            return valid_arguments
        except:
            return False    


    

