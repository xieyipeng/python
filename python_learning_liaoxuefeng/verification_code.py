# TODO: 字母验证码
from PIL import Image, ImageDraw, ImageFont, ImageFilter;
import random


# 随机字母
def randomChar():
    return chr(random.randint(65, 90))  # chr（kk） 函数，kk为整数，asc编码值，函数返回asc编码为kk 的对应的字符。


# 随机颜色1
def randomColor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def randomColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype(
    r'C:\Windows\WinSxS\amd64_microsoft-windows-font-truetype-tahoma_31bf3856ad364e35_10.0.10240.16384_none_37ccdc5b0f50c21d/tahoma.ttf',
    36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=randomColor1())

# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), randomChar(), font=font, fill=randomColor2())

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('icon/code.JPG', 'JPEG')
