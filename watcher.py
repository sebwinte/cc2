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
        cc2 Watchdog .
    '''

    path = "testordner/"

  
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
        self.c = Controller() 
        self.counter= 0
    
    #basic logger
    #logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    
    # def on_modified(self, event):
                       
                
    def on_deleted(self, event):
        print("gelöscht")
        
    def on_created(self, event):        
        # print(event.src_path)
        marker = "--"
        

        head, tail = os.path.split(event.src_path)
        extension = os.path.splitext(tail)[1]
        file_name = os.path.splitext(tail)[0]
        arguments = re.split(marker, file_name)

        if(self.counter==0):
            self.c.process(arguments[0],arguments,event.src_path,file_name+extension,file_name)
            self.counter=1

        print("on_created")
       
        
        
    def on_moved(self, event):
        print("verschoben") #umbennen
        
        
        
#if __name__ == '__main__': 
    #watch = Watchdog() 
    #watch.run() 