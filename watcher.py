import sys
import time
import os
import logging   
import re
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from controller import Controller
        
class Watcher: 
    
    '''
        cc2 Watcher
    '''

    path = "/Users/tom/Downloads/"

  
    def __init__(self): 
        self.observer = Observer() 
        
  
    def run(self): 
        event_handler = Event() 
        self.observer.schedule(event_handler, self.path, recursive = True) 
        self.observer.start() 
        try: 
            while True: 
                time.sleep(5) 
        except: 
            self.observer.stop() 
            print("Observer Stopped") 
  
        self.observer.join() 
        
        
        
class Event(LoggingEventHandler):
    
    '''
        cc2 Eventhandler
    '''

    def __init__(self): 
        # pass
        self.c = Controller() 
        self.counter= 0
    
    #basic logger
    #logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    
    #def on_modified(self, event):
                       
                
    def on_deleted(self, event):
        print("gelöscht")
        
    def on_created(self, event):       
        
        valid_argument_types = [".txt", ".mp4", ".webm", ".ogv"]
        valid_argument_compressions = ["low", "medium", "high"]
        
        file_path, original_file_name = os.path.split(event.src_path)
        extension = os.path.splitext(original_file_name)[1]
        file_name = os.path.splitext(original_file_name)[0]
                
        marker = "--"  
        
        splitted_file = re.split(marker, file_name)
        file_name_without_arguments = splitted_file[0]
        file_name_without_arguments_extension = splitted_file[0]+extension
        cropped_file_extension = extension.split(".")[1]
        
        
        if extension in valid_argument_types:
            
            print(f'is valid')
            
            for desired_argument in valid_argument_compressions:
                if desired_argument in splitted_file:
                    print (f'desired argument found')                    
                    #self.c.process(bucky,arguments,event.src_path,file_name+extension)                    
                    return 0
                else:
                    print (f'nothing to see here')
    
        else:
            print(f'No supported file extension')
         
        
    def on_moved(self, event):
        print("verschoben") #umbennen
        
        
# if __name__ == '__main__': 
#     watch = Watcher() 
#     watch.run() 