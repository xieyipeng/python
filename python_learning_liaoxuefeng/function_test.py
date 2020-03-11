# 函数：
# help(abs)  # 调用帮助文档查看abs函数
print(abs(100))
print(abs(-10))

print(max(1, 2, 3, 4))  # max函数直接接受任意多个参数，并返回最大的那个

# 类型转换
print(int('123'))
print(str(123))
print(bool(1))
print(bool(''))


# 定义函数：
def my_abs(x):
    if not isinstance(x, (float, int)):  # 修改的my_abs()函数--异常处理,instance<->示例
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 空函数：
def nop():
    pass


# 返回多个值：
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step + math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x)
print(y)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)  # 返回值是一个tuple
