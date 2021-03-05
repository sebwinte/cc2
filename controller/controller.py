from helper.convert import Converter
from helper.directory import Directory
import time
import threading
import helper.settings as settings
import os.path
from os import path


class Controller:

    verified_arguments = []

    def __init__(self):
        self.dir = Directory()
        self.conv = Converter()

    def process(self,file_name_without_arguments,arguments,original_file_path,file_name_without_arguments_extension,cropped_file_extension,original_file_name):

        verified_arguments_compression = self.verify_arguments_compression(arguments)
        verified_arguments_typ = self.verify_arguments_typ(arguments)

        if self.dir.make_dir(settings.path,file_name_without_arguments,0o777):
            #To do
            # Aufräumen/Sauber 
            self.conv.convert_mp4_webm(settings.path+"/"+original_file_name,settings.path+file_name_without_arguments,8)
           

            self.dir.move_files(original_file_name,settings.path,file_name_without_arguments)
            

    #To do
    # Zusammenfassen zu einer Funktion mit _typ
    def verify_arguments_compression(self,arguments):
        # Only except valid arguments
        valid_arguments = []
        try:
            # Check Compression Arguments
            for param in arguments:
                if param in settings.valid_arguments_compression:
                    print("Valid Compression Argument")
                    valid_arguments.append(param)
                else:
                    print('Invalid Argument')
            return valid_arguments
        except:
            return 0    



    def verify_arguments_typ(self,arguments):
        # Only except valid arguments
        valid_arguments = []
        try:
            # Check Compression Arguments
            for param in arguments:
                if param in settings.valid_arguments_typ:
                    print("Valid Typ Argument")
                    valid_arguments.append(param)
                else:
                    print('Invalid Argument')
            return valid_arguments
        except:
            return 0    


    def convert_videos(self, verified_arguments_compression , verified_arguments_typ , original_filetyp):

        try:
            for typ in verified_arguments_typ:
                self.conv.convert_+'mp4_webm'+(settings.path+file_name+original_file_name,file_name,file_name,10,10)
        except:
            print("ERROR")