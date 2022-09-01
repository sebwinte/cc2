import time 
import sys
from utils.helper import Helper
from utils.watcher import Watcher
from utils.tray import Tray


if __name__ == '__main__': 
    h = Helper() 
    h.load_settings()
    t = Tray()
    t.run()
    w = Watcher()
    w.run()