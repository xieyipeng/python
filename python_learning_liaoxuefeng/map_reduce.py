# map和reduce函数：
# map：接收两个参数，一个函数，一个Iterable，map将传入的函数作用于每一个元素，并返回新的Iterable


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 高阶函数
print(r)
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))  # 变为字符串

from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))  # reduce把结果继续和序列的下一个元素做累积运算


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


# str->int的函数：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print(list(map(char2num, '13579')))  # [1, 3, 5, 7, 9]
print(reduce(fn, map(char2num, '13579')))  # 13579


# 整理：
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#
#     def char2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
#     return reduce(fn, map(char2num, s))

# print(str2int('123456'))

# 用lambda函数化简：
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# filter过滤：高阶函数
# 删掉偶数，只保留奇数：

def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# 求素数：
def _odd_iter():  # 这是一个生成器:从3开始的奇数序列
    n = 1
    while True:
        n = n + 2
        yield n


# Python中的lambda关键字可以理解为：其功能类似于函数指针。
# lambda的官方翻译是匿名函数，这是相对与正常的函数来说的，举例说明：
# 定义一个正常的函数，实现增1运算：

# def plus1(x):
#     return x + 1

# 上面的语句实现了：
# 1.
# 定义了一个函数，函数名叫：plus1
# 2.
# 此函数有一个参数
# 对应的匿名函数语句写作：

# lambda x: x + 1

# 注意，这是一个表达式，所以他实际上是做不了任何事情的。。。
# 那么我们如果想调用函数来实现增1运算，分别用正常函数和匿名函数的实现举例如下：
# 实名函数实现：

# def plus1(x):
#     return x + 1
# a = 0
# a = plus1(a)
# print(a)

# 匿名函数实现：

# func = lambda x: x + 1
# a = 0
# a = func(a)
# print(a)

# 结论，匿名函数的用法，既像C语言中的宏定义，又像C语言中的函数指针。
# 将匿名函数和实名函数结合起来使用就更加好玩了，比如：

# def plus1(x):
#     return x + 1

# func = lambda x: plus1(x)
# a = 0
# a = func(a)
# print(a)
# 你看，这不就是函数指针的用法了吗？
# C语言有了函数指针就变得灵活无比，同样，将lambda用上之后，python也可以变得同样的灵活。

# 设置断点理解他
def _not_divisible(n):  # 筛选函数
    return lambda x: x % n > 0


# 如何理解yield关键字：https://www.jianshu.com/p/fb67382a0455
def primes():
    yield 2  # 到这里返回一次，之后从这里开始
    it = _odd_iter()  # 初始化话序列
    # print(it)
    # print(next(it))
    # print('while:')
    # x = 0
    while True:
        n = next(it)  # 返回序列第一个数
        yield n
        # print(n)
        # it1 = filter(_not_divisible(n), it)
        it = filter(_not_divisible(n), it)  # 构造新序列
        # num = 0
        # for i in it1:
        #     print(i)
        #     num += 1
        #     if num == 10:
        #         break
        # print("------------")
        # x += 1
        # if x == 5:
        #     break

        # # print(it)
        # # print(next(it))
        # num = 0
        # print(it==it1)
        # print('while:')
        # while num < 10:
        #     print(next(it1),)
        #     num = num + 1


for n in primes():
    if n < 100:
        print(n)
    else:
        break
