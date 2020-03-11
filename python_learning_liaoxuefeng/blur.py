# TODO: 模糊
from PIL import Image, ImageFilter

im = Image.open('icon/test1.JPG')
im2 = im.filter(ImageFilter.BLUR)
im2.save('icon/blur.JPG', 'JPEG')
