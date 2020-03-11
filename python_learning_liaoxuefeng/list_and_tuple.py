# ************list************

# list 可变的有序集合
classmates = ['michael', 'bob', 'tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
# 可以用-1作为索引
print(classmates[-1])

# 追加元素到末尾
classmates.append('Adam')
print(classmates)

# 追加到指定位置
classmates.insert(1, 'Jack')
print(classmates)

# 删除末尾的元素
classmates.pop()
print(classmates)

# 删除指定位置的元素
classmates.pop(1)
print(classmates)

# list 数据类型可以不一样
L = ['Apple', 123, True]
print(L)

# list元素也可以是另一个list -> 二维数组
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s[2])

# tuple 有序列表，与list类似，但是它一经初始化就不能修改，即tuple不可变
classmates = ('michael', 'bob', 'tracy')

# 定义空的tuple
t1 = ()

# 定义一个只有1个元素的tuple
# t2 = (1)  # 这样定义的是1这个数，而不是tuple，因为小括号即可以表示tuple，也可以表示数学中的小括号
t3 = (1,)  # 正确的定义方法应该是在1后面加逗号，python在显示只有一个元素的tuple时，也会在后面加一个逗号，以免误解

# ‘可变的’tuple：
t4 = ('a', 'b', ['A', 'B'])
t4[2][0] = 'X'
t4[2][1] = 'Y'
print(t4)
