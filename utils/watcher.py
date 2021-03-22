import sys
import time
import os
import logging   
import threading
import re
from pathlib import Path
from utils.helper import Helper
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from controller.controller import Controller
        
class Watcher: 
    
    '''
        cc2 Watcher
    '''


  
    def __init__(self): 
        self.observer = Observer() 
        self.h = Helper() 

  
    def run(self): 
        try:
            event_handler = Event() 
            self.observer.schedule(event_handler, Helper.path, recursive = False) 
            self.observer.start() 
            self.c = Controller() 
        except:
            self.h.message("CC2","Error directory: "+ Helper.path + " not found" )
            self.h.message("CC2","Stopping cc2")
            sys.exit(1)


        try: 
            while True: 
                time.sleep(5)
                if event_handler.queue:
                    print(event_handler.queue)
                    #Get the last file-path from the queue and remove it
                    file_path = Path(event_handler.queue.pop())
                    #Check if file is still there or has been removed in the meantime
                    if file_path.exists():
                        self.own_observer(file_path)
        except: 
            self.observer.stop() 
            print("Observer Stopped") 
  
        self.observer.join() 

 

    def own_observer(self,src):
        try:
            file_path, original_file_name = os.path.split(src)
            extension = os.path.splitext(original_file_name)[1]
            file_name = os.path.splitext(original_file_name)[0]
            splitted_file = re.split(Helper.marker, file_name)
            file_name_without_arguments = splitted_file[0]
            file_name_without_arguments_extension = splitted_file[0]+extension
            cropped_file_extension = extension.split(".")[1]
        except:
            return 0  
        
        if cropped_file_extension in Helper.valid_arguments_typ:
            for desired_argument in Helper.valid_arguments_compression:
                if desired_argument in splitted_file:
                    self.c.process(file_name_without_arguments,splitted_file,file_path,file_name_without_arguments_extension,cropped_file_extension,original_file_name)                  
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
        if not event.is_directory:
            file_porcess_thread = threading.Thread(target=self.file_porcess, args=(event.src_path,))
            file_porcess_thread.start()


    def file_porcess(self,file_path):
        self.last_modified = os.stat(file_path).st_mtime
        self.file_open = True

        while self.file_open:
            time.sleep(1)
            self.check_last_modified = os.stat(file_path).st_mtime
            self.check_mark =  self.check_last_modified - self.last_modified

            if self.check_mark == 0.0:
                time.sleep(1)
                self.file_open = False
                print("finished copying")
                self.queue.append(file_path) 

            self.last_modified = self.check_last_modified
        