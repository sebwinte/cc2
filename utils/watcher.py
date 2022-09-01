import sys
import time
import os
import threading
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
                    #Get the last file-path from the queue and remove it
                    file_path = Path(event_handler.queue.pop())
                    #Check if file is still there or has been removed in the meantime (e.g. during the copying process)
                    if file_path.exists():
                        video = Video(file_path)
                        # Only start if File is valid 
                        if video.get_validation():
                            self.c.process(video)

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


    # on_created is triggerd if an new file/directory is created/copied

    def on_created(self, event): 
        if not event.is_directory:
            file_porcess_thread = threading.Thread(target=self.file_status, args=(event.src_path,))
            file_porcess_thread.start()

    
    def on_moved(self, event): 
        if not event.is_directory:
            # If file is renamed inside the folder the path is the same 
            if( os.path.split(event.src_path)[0] == os.path.split(event.dest_path)[0] ):
                file_porcess_thread = threading.Thread(target=self.file_status, args=(event.dest_path,))
                file_porcess_thread.start()



    # file_status monitors the file copying process and appends 
    # it to the queue after it is completed 

    def file_status(self,file_path):
        last_modified = os.stat(file_path).st_mtime
        file_open = True
        while file_open:
            time.sleep(1)
            check_last_modified = os.stat(file_path).st_mtime
            check_mark =  abs(check_last_modified) - abs(last_modified)

            if check_mark == 0.0:
                time.sleep(1)
                file_open = False
                self.queue.append(file_path) 

            last_modified = check_last_modified