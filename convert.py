import sys
import time
import subprocess


class Converter:

    
    def __init__(self):
        pass

    def convert_mp4_webm(self,path,input_filename, output_filename,videoCompression,audioCompression):
        try:
            print('Start convert')
            command = 'ffmpeg -i testordner/Bucky/Bucky--low.mp4 -lossless 1  testordner/Bucky/output.webm' 
            #command = 'ffmpeg -i '+ path + input_file +' -c:v libvpx-vp9 -crf '+ videoCompression + ' -b:v 0 -b:a 128k -c:a libopus '+ path + 'tester.webm'
            subprocess.run(command)
            print('WINISH convert')
        except:
            print('Error')

