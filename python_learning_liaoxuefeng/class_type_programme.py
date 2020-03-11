# 函数式编程：Functional programming

# 高阶函数：
print(abs(-5))
print(abs)
x = abs
print(x)  # 变量可以指向函数
print(x(-10))  # x变量指向函数本身


# 函数名也是变量
# abs是变量，指向求绝对值的函数abs()

# abs = 10
# print(abs(10))  # 错误的

# 传入函数：一个函数接受另一个函数作为参数，这种函数就叫高阶函数：
# 最简单的高阶函数：
def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))
# 函数式变成就是说这种高阶函数这样高度抽象的编程规范
