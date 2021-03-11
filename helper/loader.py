#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
from pathlib import Path

class Loader:
    '''
        Loads settings.json for cc2 project
    '''
    
    def __init__(self):
        pass


    def load_settings(self):
        try:
            file_path = Path("helper/settings.json")
            with open(file_path) as f:
                data = json.load(f)
            print("Settings-Loaded")
        except:
            print("Error")


