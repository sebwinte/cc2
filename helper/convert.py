import sys
import time
import subprocess
import helper.settings as settings



class Converter:

    
    def __init__(self):
        pass
    
    #ToDo
    #Funktionsname muss geändert werden 
    def manage_videos(self,verified_arguments_compression,verified_arguments_typ,file_name_without_arguments,original_file_name):
        for typ in verified_arguments_typ:
            method_name = 'to_' + str(typ)
            method = getattr(self, method_name)
            method(verified_arguments_compression,file_name_without_arguments,original_file_name)


    def to_webm(self,verified_arguments_compression,file_name_without_arguments,original_file_name):
        print("webm")
        command = 'ffmpeg -i '+ str(settings.path + original_file_name) + ' '+ str(settings.path + file_name_without_arguments +"/"+ file_name_without_arguments) + '.webm'
        print(command)
        subprocess.run(command)
        return 0


    def to_mp4(self,verified_arguments_compression,file_name_without_arguments,original_file_name):
        print("mp4")
        command = 'ffmpeg -i '+ str(settings.path + original_file_name) + ' '+ str(settings.path + file_name_without_arguments +"/"+ file_name_without_arguments) + '.mp4'
        print(command)
        subprocess.run(command)
        return 0


    def to_ogv(self,verified_arguments_compression,file_name_without_arguments,original_file_name):
        print("ogv")
        command = 'ffmpeg -i '+ str(settings.path + original_file_name) + ' '+ str(settings.path + file_name_without_arguments +"/"+ file_name_without_arguments) + '.ogv'
        print(command)
        subprocess.run(command)
        return 0

