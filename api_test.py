#!/usr/bin/env python
#
# Testing script for the raspicam API
#

import io
import time
import picamera
import cv2
import numpy as np

import time
import picamera


max_pic = 4     # Max number of pics
rest_time = 3   # seconds
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(3)
    count = 0
    for i, filename in enumerate(camera.capture_continuous('image{counter:02d}.jpg')):
        print("Captured: %s"%filename)
        time.sleep(rest_time)
        if i == max_pic:
            break

# # Create the in-memory stream
# stream = io.BytesIO()
# with picamera.PiCamera() as camera:
#     camera.start_preview()
#     time.sleep(2)
#     camera.capture(stream, format='jpeg')
# # Construct a numpy array from the stream
# data = np.fromstring(stream.getvalue(), dtype=np.uint8)
# # "Decode" the image from the array, preserving colour
# image = cv2.imdecode(data, 1)
# # OpenCV returns an array with data in BGR order. If you want RGB instead
# # use the following...
# image = image[:, :, ::-1]

# camera = picamera.PiCamera()
# try:
#     camera.start_preview()
#     time.sleep(10)
#     camera.stop_preview()
# finally:
#     camera.close()

# with picamera.PiCamera() as camera:
#     camera.resolution = (640, 480)
#     camera.start_preview()
#     camera.start_recording('foo.h264', inline_headers=False)
#     camera.wait_recording(20)
#     camera.stop_recording()
#     camera.stop_preview()
