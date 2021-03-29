import time
import picamera

with picamera.PiCamera() as camera:
          camera.start_preview()
          time.sleep(5)
          camera.capture('/home/pi/camera data/img.jpg')
          camera.stop_preview()
