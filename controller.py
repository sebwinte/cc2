from convert import Converter
from directory import Directory
import time
import threading
import settings
#from cc2 import Watchdog


class Controller:

    verified_arguments = []

    def __init__(self):
        self.dir = Directory()
        self.conv = Converter()

    def process(self,file_name_without_arguments,arguments,original_file_path,file_name_without_arguments_extension,cropped_file_extension,original_file_name):

        verified_arguments_compression = self.verify_arguments_compression(arguments)
        verified_arguments_typ = self.verify_arguments_typ(arguments)

        print(verified_arguments_compression)
        print(verified_arguments_typ)
        self.dir.make_dir(settings.path,file_name_without_arguments,0o777)

        # Only for testing 
        # ToDo: make sure Directory is created before moving the file
        time.sleep(5)
        #self.convert_videos(verified_arguments_compression,verified_arguments_typ, original_filetyp)
        

        self.dir.move_files(original_file_name,settings.path,file_name_without_arguments)


        # Only for testing 
        # ToDo: make sure the file has finished moving before starting to convert
        time.sleep(2)

        self.conv.convert_mp4_webm(settings.path+file_name_without_arguments+"/"+original_file_name,settings.path+file_name_without_arguments,8)
            

        



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
                self.conv.convert_+'mp4_webm'+(settings.path+file_name+original_file_name,file_name,file_name,10,10)

        except:
            print("ERROR")