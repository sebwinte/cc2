import sys
import os
import json
from notifypy import Notify
from pathlib import Path



class Helper():

    '''
        cc2 Helper
        ----------
        This class loads the "settings.json", defines global variables 
        and manages notifications
    '''

    

    global valid_compression_arguments 
    global valid_file_formats 
    global valid_audio_arguments
    global path
    global marker
    global settings_data


    def __init__(self):
        Helper.valid_compression_arguments = ["low", "medium", "high"]
        Helper.valid_file_formats = ["mp4", "webm", "ogv", "mov", "mkv"]
        Helper.valid_audio_arguments = ["mute"]
        Helper.marker = "--"
        Helper.os = os.name
        self.notification = Notify(
            default_notification_icon = Path("doc/logo.png").absolute()
        )


    def load_settings(self):
        Helper.settings_data = []
        Helper.path = "your_folder_name"
        Helper.notification = True
        Helper.file_status = True

        try:
            file_path = Path("settings.json").absolute()
            with open(file_path) as f:
                data = json.load(f)
            
            Helper.settings_data = data
            Helper.path = Path(data['settings'][0]['cc2_folder']).absolute()
            Helper.notification = data['settings'][0]['notification']
            Helper.file_status = data['settings'][0]['file_status']

            print("Settings-Loaded")
        except:
            print("Error @load_settings")


    def notification_message(self,title,message):
        if(Helper.notification):
            self.notification.title = title
            self.notification.message = message
            self.notification.send()
