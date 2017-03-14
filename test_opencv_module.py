from opencvsample import openImage
from PIL import Image

impath = '/home/hal9000/15.png'

openImage(Image.open(impath))

print('Done.')