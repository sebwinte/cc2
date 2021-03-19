import time 
import sys
from utils.helper import Helper
from utils.watcher import Watcher



if __name__ == '__main__': 
    h = Helper() 
    h.load_settings()
    w = Watcher()
    w.run()
