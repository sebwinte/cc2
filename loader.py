#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 20:33:18 2021

@author: tom
"""

import sys
import json

class Loader:
    '''
        Loads settings.json for cc2 project
    '''
    
    def __init__(self, filename, method):
        self.filename = open(filename, method)
        
    def __enter__(self):
        return self.filename

    def __exit__(self, type, value, traceback):
        self.filename.close()


if __name__ == '__main__':
    try:
        with Loader('settings.json', 'r') as settings_file:
            data = json.load(settings_file)
            
            small = data['compression'][0]['small']
            print(small)
            
            webm = data['format'][0]['webm']
            print(webm)            

    except:
        print(sys.stderr, '\nError reading file.\n')
        sys.exit(1)
