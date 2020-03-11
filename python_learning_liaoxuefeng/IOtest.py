# IO
from io import StringIO

try:
    f = open('F:\github\python\IOtest.txt', 'r')
    # print(f.read())
finally:
    if f:
        f.close()

# 不必调用close方法

with open('F:\github\python\IOtest.txt', 'r') as f2:
    # print(f2.read())
    print('hello')

try:
    f = open('F:\github\python\IOtest.txt', 'r')
    # for line in f.readlines():
    #     print(line.split())  # 删除掉末尾的\n
finally:
    if f:
        f.close()

try:
    f = open('F:\github\python\dajia.jpg', 'rb')  # 二进制文件
    # print(f.read())
    # for line in f.readlines():
    #     print(line.split())  # 删除掉末尾的\n
finally:
    if f:
        f.close()

# f = open('F:\github\python\dajia.jpg', 'rb',encoding='gbk')

try:
    f = open('F:\github\python\IOtest.txt', 'a')
    # f.write('hello world!\n')
    print('success!')
finally:
    if f:
        f.close()

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# byteIO
