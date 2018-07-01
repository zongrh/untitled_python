# coding=utf-8
# is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
# is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。

a = 10
b = 20
if (a is b):
    print"ab 有相同的标识"
else:
    print "ab没有相同的标识"

if (a is not b):
    print "ab 没相同的标识"
else:
    print "ab 有相同的标识"

# 修改变量 b的值
b = 10
if (a is b):
    print "ab有相同的标识"
else:
    print "ab没有相同标识"

if (a is not b):
    print "ab没有相同的标识"
else:
    print "ab有相同的标识"

# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。

