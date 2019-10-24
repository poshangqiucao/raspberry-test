from picamera import PiCamera
#import time
#import cv2

camera = PiCamera()
#camera.resolution(640,480)
#camera.vfile = True
camera.rotation = 180
camera.led = True
camera.capture('test.jpg',use_video_port=False)



