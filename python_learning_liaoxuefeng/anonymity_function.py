# 匿名函数
import functools

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# lambda x: x * x就相当于

# def f(x):
#     return x * x


# 关键字lambda表示匿名函数


# 装饰器：在函数调用期间动态添加功能的方式--Decorator

def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        print('arguments: ', args, '', kwargs)
        return func(*args, **kwargs)

    return wrapper


@log
def now():
    print('1973-03-25')


f = now
f()

# 函数的__name__属性，获取函数名称

print(now.__name__)
print(f.__name__)


# 带参数的decorator

def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log('execute')
def last():
    print('1971-01-20')


last()
print(last.__name__)

# 偏函数：把一个函数的某些参数固定住，返回一个新的函数

print(int('12345', base=8))


def int2(x, base=2):
    return int(x, base)


print(int2('100000'))

intO2 = functools.partial(int, base=2)
print(intO2('10000'))
