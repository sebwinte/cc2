import sys
import time
import os
import logging   
import re
import settings
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from controller import Controller
        
class Watcher: 
    
    '''
        cc2 Watcher
    '''

  
    def __init__(self): 
        self.observer = Observer() 
  
    def run(self): 
        event_handler = Event() 
        self.observer.schedule(event_handler, settings.path, recursive = False) 
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
        super().__init__()
        self.c = Controller() 
        self.counter= 0                       
                
    def on_deleted(self, event):
        print("gelöscht")
        
    def on_created(self, event):       
        
        marker = "--"  

        try:
            file_path, original_file_name = os.path.split(event.src_path)
            extension = os.path.splitext(original_file_name)[1]
            file_name = os.path.splitext(original_file_name)[0]

            splitted_file = re.split(marker, file_name)
            file_name_without_arguments = splitted_file[0]
            file_name_without_arguments_extension = splitted_file[0]+extension
            cropped_file_extension = extension.split(".")[1]

            
            print(file_path)
            print(original_file_name)
            print(extension)
            print(file_name)
            print(splitted_file)
            print(file_name_without_arguments)
            print(file_name_without_arguments_extension)
            print(cropped_file_extension)
        except:
            print("Error")
            return 0  
        
        if cropped_file_extension in settings.valid_arguments_typ:
            
            print(f'is valid')
            
            for desired_argument in settings.valid_arguments_compression:
                if desired_argument in splitted_file:
                    print (f'desired argument found')  
                    self.c.process(file_name_without_arguments,splitted_file,file_path,file_name_without_arguments_extension,cropped_file_extension,original_file_name)                  
                    #self.c.process(bucky,arguments,event.src_path,file_name+extension)                    
                    return 0
                else:
                    print (f'nothing to see here')
    
        else:
            print(f'No supported file extension')

        
    def on_moved(self, event):
        print("verschoben") #umbennen        