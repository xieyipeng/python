# 排序算法：
# python内置的函数：高级函数
print(sorted([12, -5, -62, 124, 65, 30]))

# 接收一个key来实现自定义排序：按绝对值排序
print(sorted([12, -5, -62, 124, 65, 30], key=abs))

# 对字符串排序是对其ascii值来排序

# 反向排序，只需制定reverse为True就好：
print(sorted([12, -5, -62, 124, 65, 30], reverse=True))
