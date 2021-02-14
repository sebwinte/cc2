import sys
import time
import os
import logging   
import re
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
        
class Watchdog: 
    
    '''
        cc2 Watchdog .
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
    
    #basic logger
    #logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    
    # def on_modified(self, event):
                       
                
    def on_deleted(self, event):
        print("gelöscht")
        
    def on_created(self, event):        
        # print(event.src_path)
        head, tail = os.path.split(event.src_path)
        extension = os.path.splitext(tail)[1]
        file_name = os.path.splitext(tail)[0]
        
        marker = "--"
        
        data = re.split(marker, file_name)
        print(data)
       
        # controller.file_added(data)
        
    def on_moved(self, event):
        print("verschoben") #umbennen
        
        
        
if __name__ == '__main__': 
    watch = Watchdog() 
    watch.run() 