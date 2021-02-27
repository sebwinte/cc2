from convert import Converter
from directory import Directory
import time
import threading
#from cc2 import Watchdog


class Controller:

    valid_arguments_compression = ["low", "medium", "high"]
    valid_arguments_typ = ["mp4", "webm", "ogv"]

    
    #Make Global only declare once
    exportPath =  "testordner/"

    def __init__(self):
        self.dir = Directory()
        self.conv = Converter()

    

    def process(self,file_name,arguments,original_file_path,original_file_name):
        valid_arguments = self.verify_arguments(arguments)        
        directory = self.create_directory(file_name)

        
        self.dir.make_dir(self.exportPath,file_name,0o777)

        time.sleep(5)
        #def move_files(self,originalPath,path, file_name):
        self.dir.move_files(original_file_path,file_name,file_name)
        self.conv.convert_mp4_webm(self.exportPath+file_name+original_file_name,file_name,file_name,10,10)
            
        #Check Params and call the coresponding functions
        #Check Array for Params
        

    
    #To do 
    #Make Valid params an array to store multiple valid arguments

    def verify_arguments(self,arguments):
        # Only except valid arguments
        try:
            for param in arguments:
                print(param)
                if param in Controller.valid_arguments_compression:
                    print("Valid Compression Argument ")
                    self.verified_arguments.compression = param
                else:
                    print('Invalid Argument')

            # Only except valid arguments
            for param in arguments:
                if param in Controller.valid_arguments_typ:
                    print("Valid File Typ Argument")
                    self.verified_arguments.typ = param
                else:
                    print('Invalid Argument') 

            return self.valid_arguments
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
