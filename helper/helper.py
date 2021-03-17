import sys
import os
import json
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

    def load_settings(self):
        try:
            file_path = Path("helper/settings.json")
            with open(file_path) as f:
                data = json.load(f)
            print("Settings-Loaded")
            self.settings_data = data
        except:
            print("Error")

    # Convert "--small,--medium,--high" into the according value based on the range of the export file_typ
    def convert_compression_value(self,compression_tag,file_typ):

        compression_value = self.settings_data['compression'][0][compression_tag]

        if(file_typ == "mp4"):
            return (int(compression_value / 9)) 

        if(file_typ == "webm"):
            return (int(compression_value / 32)*10) 

        if(file_typ == "ogv"):
            return (int(compression_value / 50)*10) 
        