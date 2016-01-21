

from PIL import Image
#http://pillow.readthedocs.org/en/3.0.x/reference/Image.html

import pytesseract

print(pytesseract.image_to_string(Image.open('sample4.jpg')))
