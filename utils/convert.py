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

    def manage_filetype_compression(self,video):
        status = None
        for file_type in video.get_file_format_arguments():
            if(video.get_compression_arguments()):
                for compression_type in video.get_compression_arguments():
                    method_name = 'to_' + str(file_type)
                    method = getattr(self, method_name)
                    if method(compression_type,video.path,video.folder_path, video.verified_compression_arguments,video.file_name_without_arguments,video.uniq_id): status = True
                    else:
                        status = False
                        break
            else: 
                print("COBY PASTA")
                method_name = 'to_' + str(file_type)
                method = getattr(self, method_name)
                if method("copy",video.path,video.folder_path, video.verified_compression_arguments,video.file_name_without_arguments,video.uniq_id): status = True
                else:
                    status = False
                    break
        return status


    def to_webm(self,compression_type,path,folder_path, verified_arguments_compression,file_name_without_arguments,unique_folder_id):
        try:
            ffmpeg_input = ffmpeg.input(path)
            ffmpeg_output = folder_path + str(file_name_without_arguments) + unique_folder_id +'\\'+ str(file_name_without_arguments) + ('-' + str(compression_type) if len(verified_arguments_compression) > 1 else '') + '.webm' 
            compression = self.convert_compression_value(str(compression_type),"webm")
            print("COMPRESSION", compression)
            ffmpeg.output(ffmpeg_input,ffmpeg_output,
                **{'c:v': 'libvpx-vp9','crf': compression, 'f': 'webm'}
                ).overwrite_output().run()

            print('WEBM @' , compression)

            return True
        except Exception as e:
            self.h.notification_message("cc2","Failed to convert -> webm")
            return False


    def to_mp4(self,compression_type,path,folder_path, verified_arguments_compression,file_name_without_arguments,unique_folder_id):
        try:
            ffmpeg_input = ffmpeg.input(path)
            ffmpeg_output = folder_path + str(file_name_without_arguments) + unique_folder_id +'\\'+ str(file_name_without_arguments) + ('-' + str(compression_type) if len(verified_arguments_compression) > 1 else '') + '.mp4' 
            compression = self.convert_compression_value(str(compression_type),"mp4")

            ffmpeg.output(ffmpeg_input,ffmpeg_output,
                **{'c:v': 'libx264','crf': compression, 'f': 'mp4'}
                ).overwrite_output().run()

            print('MP4 @' , compression)
            return True
        except:
            self.h.notification_message("cc2","Failed to convert -> mp4")
            return False

    
    def to_ogv(self,compression_type,path,folder_path, verified_arguments_compression,file_name_without_arguments,unique_folder_id):
        try:
            ffmpeg_input = ffmpeg.input(path)
            ffmpeg_output = folder_path + str(file_name_without_arguments) + unique_folder_id +'\\'+ str(file_name_without_arguments) + ('-' + str(compression_type) if len(verified_arguments_compression) > 1 else '') + '.ogv' 
            compression = self.convert_compression_value(str(compression_type),"ogv")
    
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
        if(compression_tag=="copy"):
            return "copy"
        else:
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
