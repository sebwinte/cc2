import sys
import time
import subprocess


class Converter:

    
    def __init__(self):
        pass

    def convert_mp4_webm(self,path,input_filename, output_filename,videoCompression,audioCompression):
        try:
            print('Start convert')
            
            command = 'ffmpeg -i '+ str(path) +' -c:v libvpx-vp9 -crf '+ str(videoCompression) + ' -b:v 0 -b:a 128k -c:a libopus '+ str(path) + ' tester.webm'

            print(command)
            subprocess.run(command)
            print('WINISH convert')
        except:
            print('Error')


