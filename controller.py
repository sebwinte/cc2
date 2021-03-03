from convert import Converter
from directory import Directory
import time
import threading
import settings
#from cc2 import Watchdog


class Controller:

    verified_arguments = []

    
    #Make Global only declare once
    exportPath =  "testordner/"

    def __init__(self):
        self.dir = Directory()
        self.conv = Converter()

    

    def process(self,file_name,arguments,original_file_path,original_file_name,original_filetyp):
        verified_arguments_compression = self.verify_arguments_compression(arguments)
        verified_arguments_typ = self.verify_arguments_typ(arguments)

        
        self.dir.make_dir(self.exportPath,file_name,0o777)

        time.sleep(5)
        #self.convert_videos(verified_arguments_compression,verified_arguments_typ, original_filetyp)
        #

        self.dir.move_files(original_file_path,file_name,file_name)

        time.sleep(2)

        self.conv.convert_mp4_webm(self.exportPath+file_name+original_file_name,file_name,file_name,1,1)
            

        



    def verify_arguments_compression(self,arguments):
        # Only except valid arguments
        valid_arguments = []
        try:
            # Check Compression Arguments
            for param in arguments:
                if param in settings.valid_arguments_compression:
                    print("Valid Compression Argument")
                    valid_arguments.append(param)
                else:
                    print('Invalid Argument')
            return valid_arguments
        except:
            return 0    



    def verify_arguments_typ(self,arguments):
        # Only except valid arguments
        valid_arguments = []
        try:
            # Check Compression Arguments
            for param in arguments:
                if param in settings.valid_arguments_typ:
                    print("Valid Typ Argument")
                    valid_arguments.append(param)
                else:
                    print('Invalid Argument')
            return valid_arguments
        except:
            return 0    



    def create_directory(self,directory_name):
        #Create Directory
        #When created call next function copy video
        return directory_name




    def copy_video(self,file_name,directory):
        #Copy Original video to new location
         return 0
    

    def create_log(self,status,file_name,directory):
        #Create File in directory and write status 
         return 0


    def convert_videos(self, verified_arguments_compression , verified_arguments_typ , original_filetyp):

        try:
            for typ in verified_arguments_typ:
                self.conv.convert_+'mp4_webm'+(self.exportPath+file_name+original_file_name,file_name,file_name,10,10)

        except:
            print("ERROR")