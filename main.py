import time 
import sys
from helper.helper import Helper
from helper.watcher import Watcher



if __name__ == '__main__': 
    h = Helper() 
    h.load_settings()
    w = Watcher()
    w.run()
