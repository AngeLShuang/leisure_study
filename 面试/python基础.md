### 赋值、深拷贝、浅拷贝
```
赋值：对象的引用
浅拷贝：没有拷贝子对象，原始数据改变，子对象会改变
深拷贝：增加一个指针并且开辟了新的内存，这个增加的指针指向这个新的内存
        把元素内部的元素完全进行拷贝复制.,不会产生一个改变另一个跟着改变的问题

```

### Django和Flask
```
Flask:可扩展性强,代码架构需要自己设计
      与关系型数据库的配合使用不弱于Django，与NoSQL数据库的配合远远优于Django
Django:第三方库最丰富 
       提供了mvc,orm,admin,shell,migrate等等功能
       自带ORM使Django与关系型数据库耦合度过高，如果想使用MongoDB等NoSQL数据，需要选取合适的第三方库
一种风格是走极简，只保留核心部分；一种是大而全，啥都有。
```

### 装饰器应用场景
```
装饰器本质上是一个Python函数，它能使其他函数在没有任何代码变化的情况下增加额外的功能。
装饰器以抽出大量与函数功能无关的相同代码，重复使用。

应用场景：插入日志、性能测试、事务处理、缓存和权限验证。
```

### 可迭代对象、迭代器、生成器
```
迭代器模式:当内存中放不下数据集时，我们要找到一种惰性获取数据的方式，即按需一次获取一个数据项，这就是迭代器模式。

1.可迭代对象:实现了__iter__方法(能用for循环进行迭代的对象就是可迭代对象。比如：字符串，列表，元祖，字典，集合等等)
  调用可迭代对象的__inter__方法返回一个迭代器对象
2.迭代器:实现了__next__和__iter__两个方法(__iter__返回迭代器自身，__next__返回容器中的下一个值)
  迭代器就像一个懒加载的工厂，等到有人需要的时候才给它生成值返回，没调用的时候就处于休眠状态等待下一次调用。直到无元素可调用，返回StopIteration异常。
class Fib():
    def __init__(self,max):
        self.n = 0
        self.prev = 0
        self.curr = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            value = self.curr
            self.curr += self.prev
            self.prev = value
            self.n += 1
            return value
        else:
            raise StopIteration
   可迭代对象的__iter__用于实例化一个迭代器对象，而迭代器中的__iter__用于返回迭代器本身，与__next__共同完成迭代器的迭代作用。
   总结：1. 省内存 -> 生成器  2. 惰性机制  3. 只能向前. 不能反复
3.生成器:生成器是一种特殊的迭代器，它不需要再像上面的类一样写__iter__()和__next__()方法了，只需要一个yiled关键字。
  生成器特殊的地方在于函数体中没有return关键字，函数的返回值是一个生成器对象。当执行f=fib()返回的是一个生成器对象，此时函数体中的代码并不会执行，只有显示或隐示地调用next的时候才会真正执行里面的代码。
def fib(max):
    n, prev, curr = 0, 0, 1
    while n<max:
        yield curr
        prev, curr = curr, curr + prev
        n += 1
   生成器仅仅保存了一套生成数值或者对象的算法, 并且没有让这个算法现在就开始执行, 而是什么时候调它, 什么时候开始计算一个新的值, 并返回.
   存储海量的数据会占用内存资源, 如果什么时候需要的时候就去生成, 这样将极大地减少内存占用.
```

### 内置函数
```
1. lamda匿名函数
    zed= lambda a,b : a+b 
    ret=zed(2,3)
2. sorted()排序函数   sorted(Iterable, key=None, reverse=False)  key:排序规则 reverse=True正序
    d = {'c':1,'e':5,'b':7}
    sorted(d.items(), key=lambda d:d[1], reverse=True) 
3. filter()筛选函数   filter(function. Iterable)
    lst = [23, 28, 15, 27, 24, 22]
    print(list(filter(lambda age:age >18 and age % 2 ==0,lst)))
    用来筛选的函数, 在filter中会自动的把iterable中的元素传递给function. 然后根据function返回的True或者False来判断是否保留此项数据
4. map()映射函数       map(function, iterable)
    lst1 = [1, 2, 3, 4, 5] 
    lst2 = [2, 4, 6, 8, 10] 
    print(list(map(lambda x, y: x + y , lst1, lst2)))
    对可迭代对象中的每一个元素进行映射,分别取执行function
5. reduce()累计函数    reduce(function, iterable)
    from functools import reduce
    print(reduce(lambda x,y:x+y, [1,2,3,4]))
    对于序列里面的所有内容进行累计操作
    
应用场景:一般定义调用一次
```