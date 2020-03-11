# ************字符串************
print(ord('A'))
print(chr(66))
print('\u4e2d\u6587')

# bytes类型x
x = b'ABC'
print(x)

# 指定编码
print('ABCD'.encode('ascii'))

# 解码
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 长度-字符数
print(len('ABC'))

# 长度-字节数
print(len('中文'))
print(len('中文'.encode('utf-8')))

# 格式化
print('Hi,%s,you have $%d.' % ('yipeng', 1000))
# 补0
print('%2d-%02d' % (3, 1))
# 小数位数
print('%.2f' % 3.1415926)
# 转义
print('growth rate: %d %%' % 7)
