import sys
import time
import subprocess


class Converter:

    def convert_mp4_webm(self,path,input_filename, output_filename,videoCompression,audioCompression):
        try:
            command = 'ffmpeg -i '+ path + input_file +' -c:v libvpx-vp9 -crf '+ videoCompression + ' -b:v 0 -b:a 128k -c:a libopus '+ path + output_file
            subprocess.run(command)
        except:
            print('Error')


