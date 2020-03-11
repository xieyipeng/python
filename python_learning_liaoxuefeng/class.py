# 定制类：

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s.' % self.name)

    def __str__(self):
        return 'Student object (name : %s)' % self.name

    __repr__ = __str__  # 偷懒的写法


print(Student('xieyipeng'))

s = Student('xieyipeng')

print(s)


# 但是：
# s = Student('xieyizhao')
# s
# <Student object at 0x000001F3496F06D8>

# __str__()返回用户看到的字符串
# __repr__()返回程序开发者看到的字符串


# __iter__()：一个类想被用于for...in...循环，就要实现__iter__()和__next__()方法

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)


# __getitem__()：Fib()函数只是看起来像list，但不能像list
# 那样用，想按照下表取值，需要实现__getitem__()方法

class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib()
print(f[0])  # 按照下标取值
print(f[0:5])  # 切片


# __getattr__()：


class GetAttrTest(object):
    def __init__(self):
        self.name = 'xieyipeng'

    def __getattr__(self, item):
        if item == 'score':
            return 99
        if item == 'age':  # 返回方法
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)


s = GetAttrTest()
print(s.name)
print(s.score)


# 利用__getattr__()写一个链式调用API：、
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)

# __call__()


s = Student('xieyipeng')
print(s())

# callable()方法
