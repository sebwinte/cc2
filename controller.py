from convert import Converter
#from cc2 import Watchdog


class Controller:

    valid_arguments_compression = ["low", "medium", "high"]
    valid_arguments_typ = ["mp4", "webm", "ogv"]

    


    def run(self):
        #Start Watchdog Eventhandler
        return 0
    


    def process(self,file_name,arguments):
        v_arguments = self.verify_arguments(arguments)        
        directory = self.create_directory(file_name)


        #Check Params and call the coresponding functions
        #Check Array for Params
        pass


    def verify_arguments(self,arguments):
        # Only except valid arguments
        try:
            for param in self.arguments:
                if param in Controller.valid_arguments_compression:
                    print("Valid Compression Argument ")
                    self.verified_arguments.compression = param
                else:
                    print('Invalid Argument')
                    return 0

            # Only except valid arguments
            for param in self.arguments:
                if param in Controller.valid_arguments_typ:
                    print("Valid File Typ Argument")
                    self.verified_arguments.typ  = param
                else:
                    print('Invalid Argument')
                    return 0

            return self.v_arguments
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
