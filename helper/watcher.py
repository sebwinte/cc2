import sys
import time
import os
import logging   
import threading
import re
import helper.settings as settings
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from controller.controller import Controller
        
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
        self.c = Controller() 


        try: 
            while True: 
                time.sleep(5)
                if len(event_handler.moved_files) != 0:
                    self.own_observer(event_handler.queue.pop(0))
                print(event_handler.moved_files)
        except: 
            self.observer.stop() 
            print("Observer Stopped") 
  
        self.observer.join() 
    

    def own_observer(self,src):

        try:
            file_path, original_file_name = os.path.split(src)
            extension = os.path.splitext(original_file_name)[1]
            file_name = os.path.splitext(original_file_name)[0]

            splitted_file = re.split(settings.marker, file_name)
            file_name_without_arguments = splitted_file[0]
            file_name_without_arguments_extension = splitted_file[0]+extension
            cropped_file_extension = extension.split(".")[1]

        except:
            return 0  
        
        if cropped_file_extension in settings.valid_arguments_typ:
            for desired_argument in settings.valid_arguments_compression:
                if desired_argument in splitted_file:
                    self.c.process(file_name_without_arguments,splitted_file,file_path,file_name_without_arguments_extension,cropped_file_extension,original_file_name)                  
                else:
                    return 0
        else:
            print(f'No supported file extension')

        
        
class Event(LoggingEventHandler):
    
    '''
        cc2 Eventhandler
    '''


    def __init__(self): 
        super().__init__()
        self.on_modified_path=""  
        self.on_created_path=""
        self.queue=[]      


    def on_created(self, event): 
        self.on_created_path=event.src_path


    def on_modified(self, event):

        if self.on_modified_path == event.src_path and  self.on_created_path == self.on_modified_path:
            self.queue.append(self.on_modified_path)
        else:
            self.on_modified_path = event.src_path