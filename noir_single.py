# imports

import picamera
from time import sleep
import subprocess
import time

# configuration

camera = picamera.PiCamera()

timestr = time.strftime("%Y%m%d-%H%M")
filename = 'image_single_' + timestr + '.jpg'
camera.capture(filename)
cmd_str='/usr/local/bin/infrapix_single -i '+filename+' --vmin -1.0 --vmax 1.0 --show_histogram -o ndvi_'+filename
print(cmd_str)
return_code = subprocess.call(["/usr/local/bin/infrapix_single","-i",filename,"--show_histogram","-o","ndvi_"+filename])




