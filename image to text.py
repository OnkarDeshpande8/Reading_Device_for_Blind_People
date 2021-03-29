from PIL import Image
from pytesseract import image_to_string

image = Image.open('demo.jpg', mode='r')
print(image_to_string(image))
