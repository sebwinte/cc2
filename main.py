import time 
import sys
import helper.settings as settings
from helper.watcher import Watcher
from helper.loader import Loader


if __name__ == '__main__': 
    settings.init()   
    Loader.init()  

    w = Watcher()
    w.run()
