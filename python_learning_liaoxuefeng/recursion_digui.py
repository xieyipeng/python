# 递归：
# 阶乘：

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(1))
# print(fact(3))
# print(fact(1000))

# 尾递归优化 主要是把每一步的乘积传入到递归函数中：

# 如果一个函数中所有递归形式的调用都出现在函数的末尾，我们称这个递归函数
# 是尾递归的。当递归调用是整个函数体中最后执行的语句且它的返回值不属于表
# 达式的一部分时，这个递归调用就是尾递归。尾递归函数的特点是在回归过程中
# 不用做任何操作，这个特性很重要，因为大多数现代的编译器会利用这种特点自
# 动生成优化的代码。


def fact(n):  # 尾递归和循环是等价的
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    a = num - 1
    b = num * product
    return fact_iter(a, b)


print(fact(1000))
