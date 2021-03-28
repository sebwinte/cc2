import sys
import time
import subprocess
from utils.helper import Helper
import ffmpeg



class Converter:

    '''
        cc2 Converter
        ----------
        This class handels the video compression and conversion.
        Compression values are defined in the "settings.json".
    '''

    
    
    def __init__(self):
        self.h = Helper()
    

    # manage_filetype_compression calls the corresponding convert function.

    def manage_filetype_compression(self,verified_arguments_compression,verified_arguments_type,file_name_without_arguments,original_file_name,unique_folder_id):
        for file_type in verified_arguments_type:
            method_name = 'to_' + str(file_type)
            method = getattr(self, method_name)
            print("mange_filetype " ,file_type)
            if method(verified_arguments_compression,file_name_without_arguments,original_file_name,unique_folder_id): status = True
            else:
                status = False
                break
        return status


    def to_webm(self,verified_arguments_compression,file_name_without_arguments,original_file_name,unique_folder_id):
        try:
            ffmpeg_input = ffmpeg.input(str(Helper.path) + str(original_file_name))
            ffmpeg_output = str(Helper.path) + str(file_name_without_arguments) + str(unique_folder_id) +'/'+ str(file_name_without_arguments) + '.webm'
            compression = self.convert_compression_value(str(verified_arguments_compression[0]),"webm")
    
            ffmpeg.output(ffmpeg_input,ffmpeg_output,
                **{'c:v': 'libvpx-vp9','crf': compression, 'f': 'webm'}
                ).overwrite_output().run()

            print('WEBM @' , compression)
            return True
        except:
            self.h.notification_message("cc2","Failed to convert -> webm")
            return False


    def to_mp4(self,verified_arguments_compression,file_name_without_arguments,original_file_name,unique_folder_id):
        try:
            ffmpeg_input = ffmpeg.input(str(Helper.path) + str(original_file_name))
            ffmpeg_output = str(Helper.path) + str(file_name_without_arguments) + str(unique_folder_id) +'/'+ str(file_name_without_arguments) + '.mp4'
            compression = self.convert_compression_value(str(verified_arguments_compression[0]),"mp4")
    
            ffmpeg.output(ffmpeg_input,ffmpeg_output,
                **{'c:v': 'libx264','crf': compression, 'f': 'mp4'}
                ).overwrite_output().run()

            print('MP4 @' , compression)
            return True
        except:
            self.h.notification_message("cc2","Failed to convert -> mp4")
            return False


    def to_ogv(self,verified_arguments_compression,file_name_without_arguments,original_file_name,unique_folder_id):
        try:
            print("ogv")
            ffmpeg_input = ffmpeg.input(str(Helper.path) + str(original_file_name))
            ffmpeg_output = str(Helper.path) + str(file_name_without_arguments) + str(unique_folder_id) +'/'+ str(file_name_without_arguments) + '.ogv'
            compression = self.convert_compression_value(str(verified_arguments_compression[0]),"ogv")
    
            ffmpeg.output(ffmpeg_input,ffmpeg_output,
                **{'c:v': 'libtheora','q:v': compression, 'f': 'ogv'}
                ).overwrite_output().run()

            print('OGV @' , compression)
            return True
        except:
            self.h.notification_message("cc2","Failed to convert -> ogv")
            return False


    # convert_compression_value converts the "--small,--medium,--high" arguments into
    # numeric values.
    # Values are based on the crf values of each encoder 

    def convert_compression_value(self,compression_tag,file_type):
        compression_value= self.h.settings_data['compression'][0][compression_tag]

        if 0 < compression_value < 100:
            if(file_type == "mp4"):
                return (int( (51 / 100) * (100 - compression_value) ) ) 

            if(file_type == "webm"):
                return (int( (63 / 100) * (100 - compression_value) ) ) 

            if(file_type == "ogv"):
                return (int( (10 / 100) * compression_value ) ) 
        else:
            self.h.notification_message("cc2","No valid compression value")
            sys.exit(1)
