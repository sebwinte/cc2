import sys
import time
import subprocess
from helper.helper import Helper


class Converter:

    '''
        cc2 Converter
    '''

    
    def __init__(self):
        self.h = Helper()
        self.h.load_settings()
    
    #ToDo
    #Funktionsname muss geändert werden 
    def manage_videos(self,verified_arguments_compression,verified_arguments_typ,file_name_without_arguments,original_file_name):
        for typ in verified_arguments_typ:
            method_name = 'to_' + str(typ)
            method = getattr(self, method_name)
            return method(verified_arguments_compression,file_name_without_arguments,original_file_name)


    def to_webm(self,verified_arguments_compression,file_name_without_arguments,original_file_name):
        try:
            compression = self.h.convert_compression_value(str(verified_arguments_compression[0]),"webm")
            command = 'ffmpeg -i '+ str(Helper.path) + str(original_file_name) + ' '+ str(Helper.path) + str(file_name_without_arguments) +'/'+ str(file_name_without_arguments) + '.webm -loglevel quiet'
            subprocess.run(command, shell=True)
            return True
        except:
            return False


    def to_mp4(self,verified_arguments_compression,file_name_without_arguments,original_file_name):
        try:
            compression = self.h.convert_compression_value(str(verified_arguments_compression[0]),"mp4")
            command = 'ffmpeg -i '+ str(Helper.path) + str(original_file_name) + ' '+ str(Helper.path) + str(file_name_without_arguments) +'/'+ str(file_name_without_arguments) + '.mp4 -loglevel quiet'
            subprocess.run(command, shell=True)
            return True
        except:
            return False



    def to_ogv(self,verified_arguments_compression,file_name_without_arguments,original_file_name):
        try:
            compression = self.h.convert_compression_value(str(verified_arguments_compression[0]),"ogv")
            command = 'ffmpeg -i '+ str(Helper.path) + str(original_file_name) + ' '+ str(Helper.path) + str(file_name_without_arguments) +'/'+ str(file_name_without_arguments) + '.ogv -loglevel quiet'
            subprocess.run(command, shell=True)
            return True
        except:
            return False