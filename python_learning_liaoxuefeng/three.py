# TODO:PIL 第三方模块

from PIL import Image

image = Image.open('icon/test.png')
w, h = image.size

# 1234/12/12 12:12 Tata:
# 缩放放到50%
# new_image = image.resize((int(w // 2), int(h // 2)), Image.ANTIALIAS)
# new_image.save('icon/new_test.png')
# new_image.close()

image1 = Image.open('icon/test1.JPG')
image1.thumbnail((int(w // 2), int(h // 2)))
image1.save('icon/new_test1.JPG', 'JPEG')

# plt.figure("test")
# plt.imshow(im)
# plt.show()

# TODO 搜索文件夹下所有图片格式文件并缩小
# import os
# from PIL import Image
#
# ext = ['jpg', 'jpeg', 'png']
# files = os.listdir('icon/')
#
#
# def process_image(filename, m_width=200, m_height=400):
#     image = Image.open("icon/"+filename)
#     w, h = image.size
#     if w <= m_width and h <= m_height:
#         print(filename, 'is OK.')
#         return
#     if (1.0 * w / m_width) > (1.0 * h / m_height):
#         scale = 1.0 * w / m_width
#         new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)
#
#     else:
#         scale = 1.0 * h / m_height
#         new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)
#     new_im.save('icon/new-' + filename)
#     new_im.close()
#
#
# for file in files:
#     print(file)
#     if file.split('.')[-1] in ext:
#         process_image(file)
