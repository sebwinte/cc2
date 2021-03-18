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

    '''
    H.264 (libx264) The range of the CRF scale is 0–51, where 0 is lossless, 23 is the default, and 51 is worst quality possible

    VP9 (libvpx-vp9) No default value. The CRF value can be from 0–63. Lower values mean better quality. Recommended values range from 15–35, with 31 being recommended for 1080p HD video.
    
    Libtheora (libtheora) For libtheora, it's the opposite - higher values are better. Range is 0-10.'''

    # Convert "--small,--medium,--high" into the according value based on the range of the export file_typ
    def convert_compression_value(self,compression_tag,file_typ):

        compression_value = self.settings_data['compression'][0][compression_tag]

        if(file_typ == "mp4"):
            return (int( (51 / 100) * (100 - compression_value) ) ) 

        if(file_typ == "webm"):
            return (int( (63 / 100) * (100 - compression_value) ) ) 

        if(file_typ == "ogv"):
            return (int( (10 / 100) * compression_value ) ) 
        