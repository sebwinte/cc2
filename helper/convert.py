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
    

    #ToDo
    #Funktionsname muss geändert werden 
    def manage_videos(self,verified_arguments_compression,verified_arguments_typ,file_name_without_arguments,original_file_name,uniq_folder_id):
        for typ in verified_arguments_typ:
            method_name = 'to_' + str(typ)
            method = getattr(self, method_name)
            if method(verified_arguments_compression,file_name_without_arguments,original_file_name,uniq_folder_id): status = True
            else:
                status = False
                break
        return status


    def to_webm(self,verified_arguments_compression,file_name_without_arguments,original_file_name,uniq_folder_id):
        try:
            compression = self.convert_compression_value(str(verified_arguments_compression[0]),"webm")
            print('WEBM @' , compression)
            command = 'ffmpeg -i '+ str(Helper.path) + str(original_file_name) + '  -c:v libvpx-vp9 -crf '+ str(compression) +' ' + str(Helper.path) + str(file_name_without_arguments) + uniq_folder_id +'/'+ str(file_name_without_arguments) + '.webm -loglevel quiet'
            subprocess.run(command, shell=True)
            return True
        except:
            self.h.message("CC2","Failed to convert -> webm")
            return False


    def to_mp4(self,verified_arguments_compression,file_name_without_arguments,original_file_name,uniq_folder_id):
        try:
            compression = self.convert_compression_value(str(verified_arguments_compression[0]),"mp4")
            print('MP4 @' , compression)
            command = 'ffmpeg -i '+ str(Helper.path) + str(original_file_name) + '  -c:v libx264 -crf '+ str(compression) +' ' + str(Helper.path) + str(file_name_without_arguments) + uniq_folder_id +'/'+ str(file_name_without_arguments) + '.mp4 -loglevel quiet'
            subprocess.run(command, shell=True)
            return True
        except:
            self.h.message("CC2","Failed to convert -> mp4")
            return False


    def to_ogv(self,verified_arguments_compression,file_name_without_arguments,original_file_name,uniq_folder_id):
        try:
            compression = self.convert_compression_value(str(verified_arguments_compression[0]),"ogv")
            print('OGV @' , compression)
            command = 'ffmpeg -i '+ str(Helper.path) + str(original_file_name) + '  -c:v libtheora -q:v '+ str(compression) +' ' + str(Helper.path) + str(file_name_without_arguments) + uniq_folder_id +'/'+ str(file_name_without_arguments) + '.ogv -loglevel quiet'
            subprocess.run(command, shell=True)
            return True
        except:
            self.h.message("CC2","Failed to convert -> ogv")
            return False


    # Convert "--small,--medium,--high" into the according value based on the range of the export file_typ
    def convert_compression_value(self,compression_tag,file_typ):
        compression_value = self.h.settings_data['compression'][0][compression_tag]
        
        if(file_typ == "mp4"):
            return (int( (51 / 100) * (100 - compression_value) ) ) 

        if(file_typ == "webm"):
            return (int( (63 / 100) * (100 - compression_value) ) ) 

        if(file_typ == "ogv"):
            return (int( (10 / 100) * compression_value ) ) 
        