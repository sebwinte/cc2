from helper.convert import Converter
from helper.directory import Directory
import time
import threading
from helper.helper import Helper
import os.path
from os import path
from pathlib import Path
from notifypy import Notify


class Controller:

    verified_arguments = []

    def __init__(self):
        self.dir = Directory()
        self.conv = Converter()
        self.notification = Notify(
            default_notification_icon = Path("doc/logo.png")
        )


    def process(self,file_name_without_arguments,arguments,original_file_path,file_name_without_arguments_extension,cropped_file_extension,original_file_name):

        verified_arguments_compression = self.verify_arguments_compression(arguments)
        verified_arguments_typ = self.verify_arguments_typ(arguments)

        if self.dir.make_dir(Helper.path,file_name_without_arguments,0o777):

            self.conv.manage_videos(verified_arguments_compression,verified_arguments_typ,file_name_without_arguments,original_file_name)
           
            self.dir.move_files(original_file_name,Helper.path,file_name_without_arguments)


            self.notification.title = "cc2-Finished"
            self.notification.message = file_name_without_arguments + " is ready."
            self.notification.send()


            

    #To do
    # Zusammenfassen zu einer Funktion mit _typ
    def verify_arguments_compression(self,arguments):
        # Only except valid arguments
        valid_arguments = []
        try:
            # Check Compression Arguments
            for param in arguments:
                if param in Helper.valid_arguments_compression:
                    valid_arguments.append(param)
            return valid_arguments
        except:
            return 0    



    def verify_arguments_typ(self,arguments):
        # Only except valid arguments
        valid_arguments = []
        try:
            # Check Compression Arguments
            for param in arguments:
                if param in Helper.valid_arguments_typ:
                    valid_arguments.append(param)
            return valid_arguments
        except:
            return 0    




