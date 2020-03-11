# 返回函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f1 = lazy_sum(1, 2, 3, 4, 5)
f2 = lazy_sum(1, 2, 3, 4, 5)
print(f1)
print(f1())  # 调用函数f时才会真正求和计算结果
print(f1 == f2)  # 每次调用都返回一个新的函数，即使参数相同


# 闭包：
#
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#
#         fs.append(f)
#     return fs
#
#
# f1, f2, f3 = count()  # 9 9 9
# print(f1(), f2(), f3())  # 返回闭包时，不要引用任何循环变量

# 如果一定要引用，在创建一个函数，用函数的参数绑定循环变量当前的值：
def count():
    def f(j):
        def g():
            return j * j

        print('g:', g)
        return g

    fs = []
    for i in range(1, 4):
        print('i:', i)
        fs.append(f(i))  # f(i)立即被执行，i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())  # 1 4 9
