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


    def __init__(self):
        Helper.valid_arguments_compression = ["low", "medium", "high"]
        Helper.valid_arguments_typ = ["mp4", "webm", "ogv"]
        Helper.path = "testordner/"
        Helper.marker = "--"
        Helper.os = os.name
        self.settings_data = []
        self.notification = Notify(
            default_notification_icon = Path("doc/logo.png")
        )


    def load_settings(self):
        try:
            file_path = Path("helper/settings.json")
            with open(file_path) as f:
                data = json.load(f)
            print("Settings-Loaded")
            self.settings_data = data
        except:
            print("Error")

    def message(self,title,message):
        self.notification.title = title
        self.notification.message = message
        self.notification.send()