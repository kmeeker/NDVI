#!/usr/bin/python
# imports

import picamera
from time import sleep
import subprocess
import time
import os

# configuration

return_code = subprocess.call("rm image.jpg ndvi_image.jpg", shell=True)

camera = picamera.PiCamera()

filename = 'image.jpg'
camera.capture(filename)

cmd_str="/usr/local/bin/infrapix_single -i " + filename + " --vmin -1.0 --vmax 1.0 --show_histogram -o ndvi_" + filename
    `return_code = subprocess.call(cmd_str, shell=True)

return_code = subprocess.call("gpicview --slideshow image.jpg", shell=True)



