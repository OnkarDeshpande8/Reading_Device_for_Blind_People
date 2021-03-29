from gtts import gTTS
import os
from PIL import Image
from pytesseract import image_to_string

          
image = Image.open('demo.jpg', mode='r')
print(image_to_string(image))


tts=gTTS(image_to_string(image),lang='en',slow=False)

tts.save("output.mp3")

os.system("start output.mp3")

print('process complited')



