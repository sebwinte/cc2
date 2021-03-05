import time 
import sys
import helper.settings as settings
from helper.watcher import Watcher


if __name__ == '__main__': 
    settings.init()     
    w = Watcher()
    w.run()
