import time 
import sys
from helper.helper import Helper
from helper.watcher import Watcher


if __name__ == '__main__': 
    h = Helper() 
    #h.load_settings()

    #print(h.convert_compression_value("low","webm"))
    #print("-----------------------------------------")
    w = Watcher()
    w.run()
