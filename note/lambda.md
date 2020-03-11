Lambda关键词是一种轻量级的函数生成方式，其返回一个匿名函数，Lambda的调用格式如下： 
    Lambda [ aru……] : expression 
Lambda的应用实例：

```
1 固定参数：
>>> x = lambda a,b:a+b**2
>>> x(1,2)
5

2 可变参数
>>> z = lambda **a:len(a)
>>> z(a=1,b=2,c=3)
3

3 接受任意多个参数，只是以字典的键值对形式返回给函数体
>>> z = lambda **a:len(a)
>>> z(a=1,b=2,c=3)
31234567891011121314
```

在python中实现switch语句的Lambda方式：

```
def operator(a,b,c):
...     if b == '+':
...         return a+c
...     elif b == '-':
...         return a-c
...     elif b == '*':
...         return a*c
...     elif b == '/':
...         return a/c
... 
>>> operator(5,'*',5)#调用函数
25
>>> 

此结果的Lambda实现:
def operator1(a,b,c):
...     result = {'+':lambda a,c:a+c ,'-':lambda a,c:a-c,
...               '*':lambda a,c:a*c ,'/':lambda a,c:a/c}
...     return result
... 
>>> operator(5,'*',5)
25
```