# dict（字典）:全称dictionary，在其他语言中称为map,内部顺序和key放入的顺序无关
d = {'michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['michael'])

# 要避免key不存在的错误
print('thomas' in d)  # 判断key是否存在
print(d.get('thomas'))  # 如果key不存在，返回None
print(d.get('thomas', -1))  # 如果key不存在，返回自己定义的数字

# 删除key，对应的value也会被删除
d.pop('Bob')
print(d)

# dirt的key是不可变对象

# set,set与dirt类似，但是不存储value，在set中没有重复的key，可看作数学上无序，无重复的集合，可做交'&'并'|'等运算。
s = set([1, 2, 3, 1, 1, 2, 4])  # 传入的参数是list，重复的元素在set中被自动过滤
print(s)

# 通过remove（key）来删除元素：
s.remove(1)
print(s)  # {2, 3, 4}

# 再说不可变对象：
a = ['c', 'b', 'a']
a.sort()
print(a)  # list内容可变
a = 'abc'
a.replace('a', 'A')
print(a)  # 最后变量a仍然是abc

a = 'abc'
b = a.replace('a', 'A')
print(b)  # Abc
print(a)  # abc，要牢记，a是变量，'abc'才是字符串对象,replace方法创建了一个新的字符串
