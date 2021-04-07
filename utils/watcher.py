import sys
import time
import os
import logging   
import threading
import re
from uuid import uuid4
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
            self.h.message("CC2","Maybe the directory: "+ Helper.path + " is not correct" )
            self.h.message("CC2","Stopping cc2")
            sys.exit(1)


        try: 
            while True: 
                time.sleep(5)
                print("EventHandlerQueue ", event_handler.queue_list)

                if event_handler.queue_list:
                    for video in event_handler.queue_list:
                        
                        if os.path.exists(video.get_path()):
                            video.strip_filename()
                            if(video.validate()):
                                self.c.process(video)
                                event_handler.queue_list.remove(video)
                        else:
                            event_handler.queue_list.remove(video)

                        
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
        self.queue_list = [] 


    def on_created(self, event): 
        if not event.is_directory:
            file_porcess_thread = threading.Thread(target=self.file_porcess, args=(event.src_path,))
            file_porcess_thread.start()
            #file_porcess_thread.join()


    def on_moved(self, event):
        print("Moved-Event ", event)


    def on_deleted(self, event):
        print("Delete ", event)
        #print("Delete-Queue ", self.queue)
        #if event.src_path in  self.queue:
        #    print("In liste vorhanden")


    def file_porcess(self,file_path):
        print("############################################",file_path)
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

                #Create new object and add video to queue_list
                self.video = Video()
                self.video.set_path(file_path) 
                self.video.set_status(True)
                self.queue_list.append(self.video)

            self.last_modified = self.check_last_modified
        



class Video: 

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
        self.splitted_file = []
        self.file_name_without_arguments = ''
        self.file_name_without_arguments_extension = ''
        self.cropped_file_extension = ''
        self.uniq_id = str(uuid4())

        self.verified_arguments_compression = []
        self.verified_arguments_typ = []

        self.state = 0

    

    def set_path(self,path):
        self.path = path


    def set_status(self,file_status):
        self.file_status = file_status


    def get_path(self):
        return self.path


    def set_state(self,state):
        self.state = state


    def get_state(self):
        return self.state


    def strip_filename(self):
        self.file_path, self.original_file_name = os.path.split(self.path)
        self.extension = os.path.splitext(self.original_file_name)[1]
        self.file_name = os.path.splitext(self.original_file_name)[0]
        self.splitted_file = re.split(Helper.marker, self.file_name)
        self.file_name_without_arguments = self.splitted_file[0]
        self.file_name_without_arguments_extension = self.splitted_file[0]+self.extension
        self.cropped_file_extension = self.extension.split(".")[1]


    def validate(self):
        if self.cropped_file_extension.lower() in Helper.valid_arguments_typ:
            for desired_argument in Helper.valid_arguments_compression:
                print(desired_argument)
                if desired_argument in self.splitted_file:
                    self.verify_arguments_compression() 
                    self.verify_arguments_typ()
                    return True
                    #break            
                else:
                    return False


    def verify_arguments_compression(self):
        try:
            for param in self.splitted_file:
                if param.lower() in Helper.valid_arguments_compression:
                    self.verified_arguments_compression.append(param.lower())
        except:
            return False    


    def verify_arguments_typ(self):
        try:
            for param in self.splitted_file:
                if param.lower() in Helper.valid_arguments_typ:
                    self.verified_arguments_typ.append(param.lower())
        except:
            return False   