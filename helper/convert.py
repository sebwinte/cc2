import sys
import time
import subprocess


class Converter:

    
    def __init__(self):
        pass

    def convert_mp4_webm(self,file_path,path,videoCompression):
        try:
            print('Start converting Video')
            command = 'ffmpeg -i '+ str(file_path) +' -c:v libvpx-vp9 -crf '+ str(videoCompression) + ' -b:v 0 -b:a 128k -c:a libopus '+ str(path) + '/tester.webm'
            subprocess.run(command)
        except:
            print('Error')


