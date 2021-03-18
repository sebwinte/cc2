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
    def manage_videos(self,verified_arguments_compression,verified_arguments_typ,file_name_without_arguments,original_file_name,uniq_id):
        for typ in verified_arguments_typ:
            method_name = 'to_' + str(typ)
            method = getattr(self, method_name)
            if method(verified_arguments_compression,file_name_without_arguments,original_file_name,uniq_id): status = True
            else:
                status = False
                break
        return status

    # ffmpeg -i "input" -c:v libx264 -crf 28 output.mp4
    def to_webm(self,verified_arguments_compression,file_name_without_arguments,original_file_name,uniq_id):
        try:
            compression = self.h.convert_compression_value(str(verified_arguments_compression[0]),"webm")
            print('WEBM @' , compression)
            command = 'ffmpeg -i '+ str(Helper.path) + str(original_file_name) + '  -c:v libvpx-vp9 -crf '+ str(compression) +' ' + str(Helper.path) + str(file_name_without_arguments) + uniq_id +'/'+ str(file_name_without_arguments) + '.webm -loglevel quiet'
            subprocess.run(command, shell=True)
            return True
        except:
            return False


    def to_mp4(self,verified_arguments_compression,file_name_without_arguments,original_file_name,uniq_id):
        try:
            compression = self.h.convert_compression_value(str(verified_arguments_compression[0]),"mp4")
            print('MP4 @' , compression)
            command = 'ffmpeg -i '+ str(Helper.path) + str(original_file_name) + '  -c:v libx264 -crf '+ str(compression) +' ' + str(Helper.path) + str(file_name_without_arguments) + uniq_id +'/'+ str(file_name_without_arguments) + '.mp4 -loglevel quiet'
            subprocess.run(command, shell=True)
            return True
        except:
            return False



    def to_ogv(self,verified_arguments_compression,file_name_without_arguments,original_file_name,uniq_id):
        try:
            compression = self.h.convert_compression_value(str(verified_arguments_compression[0]),"ogv")
            print('OGV @' , compression)
            command = 'ffmpeg -i '+ str(Helper.path) + str(original_file_name) + '  -c:v libtheora -q:v '+ str(compression) +' ' + str(Helper.path) + str(file_name_without_arguments) + uniq_id +'/'+ str(file_name_without_arguments) + '.ogv -loglevel quiet'
            subprocess.run(command, shell=True)
            return True
        except:
            return False