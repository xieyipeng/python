# ************数据类型************

# 科学记数法
print(1.23e8)

# 字符串：""或''本身只是一种表示，如果字符串中有'，那就用""括起来。
print("I'm OK")
# 既包含',又包含"，用转义字符\
print('I\'m \"OK\"')
# 用r''表示''里面的字符不允许转义
print(r'\\\t\\')
# 用'''...'''格式表示多行内容
print('''line1
line2
line3''')

# 布尔值
print(3 > 2)
print(True and True)

# 空值None

# 变量：
a = 123
print(a)
a = '456'
print(a)

x = 10
x = x + 2
print(x)

# 除法 1、/  2、//
print(10 / 3)
print(10 // 3)  # 整数的地板除，只取整数

# 取余
print(10 % 3)
