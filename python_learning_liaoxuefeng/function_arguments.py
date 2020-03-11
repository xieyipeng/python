# 函数参数：
# 位置参数：

# def power(x):
#     return x * x
# print(power(5))


def power(x, n=2):  # 上面的power函数就没用了，修改为带有默认参数的函数
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5, 4))
# 默认参数：
print(power(5))  # 必选参数在前，默认参数在后


def enroll(name, gender, age=6, city='beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Sarach', 'F')
enroll('Sarach', 'F', city='Tianjin')  # 默认参数的调用


# def add_end(L=[]):  # 默认参数的坑
#     L.append('end')
#     return L
#
#
# print(add_end())
# print(add_end())
# print(add_end())  # 所以默认参数的定义必须是只想不可变对象

def add_end(L=None):  # 修改的
    if L is None:
        L = []
    L.append('end')
    return L


print(add_end())
print(add_end())
print(add_end())


# 可变参数：参数个数可变
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3, 4))
nums = [1, 2, 3]
print(calc(*nums))


# 关键字参数：扩展函数的功能
# def person(name, age, **kw):  # 命名关键字参数：
#     if 'city' in kw:
#         pass
#     if 'job' in kw:
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)
#
#
# print(person('Michael', 30))
# print(person('Bob', 35, city='Beijing'))  # 可以组装一个dict，person('Jack',24,**extra)

# 命名关键字参数：
# def person(name, age, *, city, job):  # 命名关键字参数：在*之后的参数都是命名关键字参数
#     print(name, age, city, job)
#
#
# print(person('Jack', 24, city='Beijing', job='English'))  # 参数必须传入参数名

def person(name, age, *, city='Beijing', job):  # 有默认参数
    print(name, age, city, job)


print(person('Jack', 24, job='English'))

# 参数组合-顺序：必选参数->默认参数->可变参数->命名参数/命名关键字参数->关键字参数
