import os
import re
import time
from pathlib import Path
from utils.helper import Helper
from utils.directory import Directory



class Video: 
    
    '''
        cc2 Video
        ----------
        This class ....
    '''


  
    def __init__(self,path): 
        self.h = Helper() 
        self.dir = Directory()
        self.uniq_id = ""
        self.converted = False                      # compressed or not
        self.valid_file = False                     # valid filetype
        self.state = ""                             # converting,finished,error
                        
        self.path = path                            # C:\USER\Videos\myvideo--medium--mp4.mp4
        self.folder_path = ''                       # C:\USER\Videos\
        self.file_name = ''                         # myvideo--medium--mp4
        self.compression_arguments = ''             # low,medium,high
        self.file_format = ''                       # mp4
        
        self.splitted_file_name = []                # ['myvideo', 'medium', 'mp4']
        self.arguments = []
        self.file_name_without_arguments = ''       # myvideo

        self.verified_compression_arguments = []    # ["low", ...]
        self.verified_file_formats = []             # ["mp4", ...]
        self.verified_audio_arguments = ""          # mute

        self.strip_filename(path)

    
    def strip_filename(self,path):
        try:
            self.folder_path, self.file_name = os.path.split(path)
            self.file_format = os.path.splitext(self.file_name)[1].split(".")[1].lower()
            self.file_name = os.path.splitext(self.file_name)[0].lower()
            self.splitted_file_name = re.split(Helper.marker, self.file_name)
            self.file_name_without_arguments = self.splitted_file_name[0]

            self.validate()
        except Exception as e:
            print(e)


    def validate(self):
        if self.file_format in Helper.valid_file_formats:

            # call here so the both verify functions get called once otherwise "or" might only call first
            valid_file_format = self.verify_file_formats()
            valid_compression_arguments = self.verify_compression_arguments()

            # need at least one to be true -> no ca = "copy", no ff = same filetype as original
            if(valid_file_format or valid_compression_arguments):
                self.valid_file = True
                self.verify_audio_arguments()
            else:
                self.valid_file = False
            
        else:
            self.valid_file = False


    # verify_compression_arguments return only valid arguments according to the Helper.valid_arguments_compression

    def verify_compression_arguments(self):
        try:
            valid = False
            for param in self.splitted_file_name:
                if param.lower() in Helper.valid_compression_arguments:
                    self.verified_compression_arguments.append(param.lower())
                    valid = True
            return valid
        except Exception as e:
            print(e)


    # verify_file_formats return only valid arguments according to the Helper.valid_arguments_type 

    def verify_file_formats(self):
        try:
            valid = False
            for param in self.splitted_file_name:
                if param.lower() in Helper.valid_file_formats:
                    self.verified_file_formats.append(param.lower())
                    valid = True

            # no argument => file_format of video is set as default
            if(valid==False): self.verified_file_formats.append(self.file_format.lower())
            return valid
        except Exception as e:
            print(e)


    def verify_audio_arguments(self):
        try:
            valid = False
            for param in self.splitted_file_name:
                if param.lower() in Helper.valid_audio_arguments:
                    self.verified_audio_arguments = param.lower()
                    valid = True
            return valid
        except Exception as e:
            print(e)


    def get_compression_arguments(self):
        return self.verified_compression_arguments

    
    def get_file_format_arguments(self):
        return self.verified_file_formats


    def set_uniq_id(self, id):
        self.uniq_id= "("+ str(id) + ")"

    def get_uniq_id(self):
        return self.uniq_id

    def get_validation(self):
        return self.valid_file


    def update_status(self,status):
        if(Helper.file_status):
            self.state=status
            file_name = self.file_name_without_arguments+self.uniq_id
            self.dir.status_file(self.folder_path,file_name,status)
            if(status=="finished"):
                time.sleep(5)
                self.dir.status_file(self.folder_path,file_name,"delete")
        
