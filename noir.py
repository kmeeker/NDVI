# imports

import picamera
from time import sleep
import subprocess
import time 

# configuration

camera = picamera.PiCamera()
delay = 3599
from subprocess import call

for i in range(1,24):
    timestr = time.strftime("%Y%m%d-%H%M")
    filename = 'image' + timestr + '.jpg'
    camera.capture(filename)

    cmd_str='/usr/local/bin/infrapix_single -i '+filename+' --show_histogram -o ndvi_'+filename
    print(cmd_str)
    return_code = subprocess.call(cmd_str, shell=True)

    cmd_str='/usr/local/bin/infrapix_single -i '+filename+' --vmin -1.0 --vmax 1.0 --show_histogram -o ndvi_'+filename
    print(cmd_str)
    return_code = subprocess.call(cmd_str, shell=True)

    cmd_str='/usr/local/bin/infrapix_single -i '+filename+' --vmin -1.0 --vmax 1.0 -o ndvi_nh_'+filename
    print(cmd_str)
    return_code = subprocess.call(cmd_str, shell=True)

    cmd_str='~/NoIR $ ~/Dropbox-Uploader/dropbox_uploader.sh upload *.jpg *.jpg'
    print(cmd_str)
    return_code = subprocess.call(cmd_str, shell=True)

    sleep(delay)




