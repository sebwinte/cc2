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
                print("EventHandlerQueue ", event_handler.queue_list)
                if event_handler.queue_list:
                    print("moin")
                    
                    for video in event_handler.queue_list:
                        self.file_path=video.get_path()
                        print("File-Path: ", self.file_path)
                        #Check if file is still there or has been removed in the meantime
                        '''
                        if file_path.exists():
                            print("File is there")
                            #video.strip_filename()
                            if(video.validate()):
                                print("valid")
                                #self.c.process(video)
                        else:
                            print("file is gone")
                        '''
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
        self.on_modified_path=""  
        self.on_created_path=""
        self.queue = Queue()
        self.queue_list = [] 


    def on_created(self, event): 
        if not event.is_directory:
            file_porcess_thread = threading.Thread(target=self.file_porcess, args=(event.src_path,))
            file_porcess_thread.start()


    def on_moved(self, event):
        print("Moved-Event ", event)


    def on_deleted(self, event):
        print("Delete ", event)
        #print("Delete-Queue ", self.queue)
        #if event.src_path in  self.queue:
        #    print("In liste vorhanden")


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
                self.queue.set_path(file_path) 
                self.queue_list.append(self.queue)

            self.last_modified = self.check_last_modified
        



class Queue: 

    '''
        cc2 compression queue
    '''


    def __init__(self): 
        self.path = '' 
        self.file_status = False
        self.compression_arguments = ''
        self.file_extension_arguments = ''

        self.extension = ''
        self.file_name = ''
        self.splitted_file = ''
        self.file_name_without_arguments = ''
        self.file_name_without_arguments_extension = ''
        self.cropped_file_extension = ''
    

    def set_path(self,path):
        self.path = path


    def set_status(self,file_status):
        self.file_status = file_status


    def get_path(self):
        return self.path


    def strip_filename(self):
        file_path, original_file_name = os.path.split(self.path)
        self.extension = os.path.splitext(original_file_name)[1]
        self.file_name = os.path.splitext(original_file_name)[0]
        self.splitted_file = re.split(Helper.marker, self.file_name.lower())
        self.file_name_without_arguments = self.splitted_file[0]
        self.file_name_without_arguments_extension = self.splitted_file[0]+extension
        self.cropped_file_extension = self.extension.split(".")[1]

    def validate(self):
        if self.cropped_file_extension.lower() in Helper.valid_arguments_typ:
            for desired_argument in Helper.valid_arguments_compression:
                if desired_argument in self.splitted_file:
                    return True                 
                else:
                    return False