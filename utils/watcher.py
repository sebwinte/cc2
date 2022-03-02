import sys
import time
import os
import logging   
import threading
import platform
import re
from pathlib import Path
from utils.helper import Helper
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from controller.controller import Controller
from utils.video import Video



class Watcher: 
    
    '''
        cc2 Watcher
        ----------
        This class monitors all activities in the defined directory.
    '''


  
    def __init__(self): 
        self.observer = Observer() 
        self.h = Helper() 


    # run starts the observer

    def run(self): 
        if os.path.exists(Helper.path):
            event_handler = Event() 
            self.observer.schedule(event_handler, Helper.path, recursive = False) 
            self.observer.start() 
            self.c = Controller()
        else:
            self.h.notification_message("cc2","Error directory: "+ Helper.path + " not found" )
            self.h.notification_message("cc2","Check cc2_folder in settings.json")
            print(sys.stderr, '\nStopping cc2.\n')
            sys.exit(1)


        try: 
            while True: 
                time.sleep(2)
                if event_handler.queue:
                    #print('Queue: ', event_handler.queue)
                    #Get the last file-path from the queue and remove it
                    file_path = Path(event_handler.queue.pop())
                    #Check if file is still there or has been removed in the meantime (e.g. during the copying process)
                    if file_path.exists():
                        video = Video(file_path)
                        #print("NEW FILE@",file_path)
                        #print("VID: ", vid.get_verified_arguments_compression())
                        #print(video.valid_file())
                        # if(video.valid_file()):
                        #     print("VALID FILE")
                        #     self.c.process(video)
                        # else:
                        #     print("NO VALID FILE")
                        # self.strip_filename(file_path)


        except Exception as e:
            self.observer.stop() 
            print("Observer Stopped") 
            print(e)
  
        self.observer.join() 

           
    
class Event(LoggingEventHandler):
    
    '''
        cc2 Eventhandler
        ----------
        See Watcher() for more details
    '''


    def __init__(self): 
        super().__init__()
        self.on_modified_path=""  
        self.on_created_path=""
        self.queue=[]    
        self.h = Helper()   

    #DEBUG DELETE 
    def on_any_event(self, event):
        #pass
        print(event)


    # on_created is triggerd if an new file/directory is created/copied

    def on_created(self, event): 
        if not event.is_directory:
            file_porcess_thread = threading.Thread(target=self.file_status, args=(event.src_path,))
            file_porcess_thread.start()



    # file_status monitors the file copying process and appends 
    # it to the queue after it is completed 

    def file_status(self,file_path):
        self.last_modified = os.stat(file_path).st_mtime
        self.file_open = True

        while self.file_open:
            time.sleep(1)
            self.check_last_modified = os.stat(file_path).st_mtime
            self.check_mark =  self.check_last_modified - self.last_modified

            if self.check_mark == 0.0:
                time.sleep(1)
                self.file_open = False
                #print("finished copying", file_path)

                # MacOS specific recursive fallback mechanism. Error caused by Watchdog API
                # only works with an absolute path
                replaced_path = file_path.replace(self.h.path, '')
                if platform.system() == "Darwin" and "/" in replaced_path:
                    print("I am on MacOS")
                    print("---->", replaced_path)
                    print("recursive fallback mechanism")
                else:
                    self.queue.append(file_path) 

            self.last_modified = self.check_last_modified