# 列表生成式，list comprehensions：可以用来生成list
print([x * x for x in range(1, 11)])  # 要把生成的元素x*x放到前面，for循环放到后面
print([m + n for m in 'ABC' for n in 'DEF'])  # 可以嵌套两层循环

import MineOs  # 导入os模块

print([d for d in MineOs.listdir('.')])  # os.listdir可以列出文件和目录
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])  # 列表生成器可以使用两个变量来生成list

# 生成器：generator<->发电机:边循环便计算的机制：
# 创建很简单，把列表生成式的[]变成()就好：
g = (x * x for x in range(10))
print(g)
# 遍历：
for n in g:
    print(n)


# 著名的斐波拉契数列：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 把fib函数改成generator，注意yield的特殊性
        # print(b)
        temp = a
        a = b
        b = temp + b
        # a, b = b, a + b
        n = n + 1
    return 'done'


print(fib(6))
# 遍历generator：
for n in fib(6):  # 发现拿不到return语句
    print(n)

# 要拿到返回值：
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return values:', e.value)
        break

# 迭代器：可以被next函数调用并不断反回下一个值的对象称为迭代器Iterator
# 可用作for循环的对象的称为可迭代对象
# 使用isinstance()函数判断一个对象是不是可迭代(Iterable)对象
# 使用isinstance()函数判断一个对象是不是可迭代(Iterator)对象
from collections import Iterable
from collections import Iterator

print(isinstance([], Iterable))
print(isinstance([], Iterator))
# 生成器（generator）都是iterator对象，但是list，dict，str虽然是Iterable，但不是Iterator
# 把list，dict，str等Iterable变成Iterator可以使用iter函数：
print(isinstance(iter([]), Iterator))
