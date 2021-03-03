import time 
import sys
import settings
from watcher import Watcher


if __name__ == '__main__': 
    settings.init()     
    w = Watcher()
    w.run()
