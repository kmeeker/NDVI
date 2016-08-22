# imports

import picamera
from time import sleep
import subprocess

# configuration

camera = picamera.PiCamera()
delay = 3600
from subprocess import call

for i in range(1,24):
    filename = 'image'+str(i)+'.jpg'
    camera.capture(filename)
    cmd_str='/usr/local/bin/infrapix_single -i '+filename+' --show_histogram -o ndvi_'+filename
    print(cmd_str)
    return_code = subprocess.call(["/usr/local/bin/infrapix_single","-i",filename,"--show_histogram","-o","ndvi_"+filename])
    sleep(delay)




