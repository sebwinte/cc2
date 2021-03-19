import sys
import os
import json
from notifypy import Notify
from pathlib import Path

class Helper():

    '''
        cc2 Helper
    '''

    

    global valid_arguments_compression
    global valid_arguments_typ 
    global path
    global marker
    global settings_data


    def __init__(self):
        Helper.valid_arguments_compression = ["low", "medium", "high"]
        Helper.valid_arguments_typ = ["mp4", "webm", "ogv"]
        Helper.marker = "--"
        Helper.os = os.name
        self.notification = Notify(
            default_notification_icon = Path("doc/logo.png")
        )


    def load_settings(self):
        Helper.settings_data = []
        Helper.path = ""
        Helper.notification = 0
        try:
            file_path = Path("utils/settings.json")
            with open(file_path) as f:
                data = json.load(f)
            
            Helper.settings_data = data
            Helper.path = data['settings'][0]['cc2_folder']
            Helper.notification = data['settings'][0]['notification']

            print("Settings-Loaded")
        except:
            print("Error @load_settings")


    def message(self,title,message):
        if(Helper.notification):
            self.notification.title = title
            self.notification.message = message
            self.notification.send()