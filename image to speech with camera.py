from gtts import gTTS
import vlc
import os
from PIL import Image
from pytesseract import image_to_string
import time
import picamera

with picamera.PiCamera() as camera:
          camera.start_preview()
          time.sleep(10)
          camera.capture('/home/pi/img.jpg')
          camera.stop_preview()
          
image = Image.open('img.jpg', mode='r')
print(image_to_string(image))


tts=gTTS(image_to_string(image),lang='en',slow=False)

tts.save("output.mp3")

p = vlc.MediaPlayer("file:///home/pi/output.mp3")
p.play()

print('process complited')






