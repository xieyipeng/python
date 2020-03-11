# 切片：
classmates = ['michael', 'bob', 'tracy']
print(classmates[0:3])  # 切片，从索引0开始，直到索引3为止，不包括3
print(classmates[:3])  # 如果第一个索引是0，也可以省略
print(classmates[-2:])  # python支持从-1取元素，倒是第一个元素的索引是-1

# 先创建0到99的数列：
L = list(range(100))
print(L)
print(L[:10:2])  # 取前十个数字，每两个取一下
print((0, 1, 2, 3, 4, 5, 6, 7)[:3])  # tuple也是一种list，只是tuple不可变而已，也可以用切片操作
print(('ABCDE')[:3])
