# 迭代：给定一个list或者tuple，用for循环来遍历整个list或者tuple，就是迭代
d = {'a': 1, 'b': 2, 'c': 3}  # 迭代key-value对，也可以迭代字符串只要作用于可迭代对象就行
for k, v in d.items():
    print(k, v)

for k, value in enumerate(['a', 'b', 'c']):  # 用enumerate(列举)方法可以将list变成索引-元素对
    print(k, value)
