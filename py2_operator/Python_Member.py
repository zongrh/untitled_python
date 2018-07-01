# coding=utf-8
# in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
# not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。

a = 10
b = 20
list = [1, 2, 3, 4, 5, 10]
if (a in list):
    print "a 在list 中"
else:
    print "a 不在list 中"

if (a not in list):
    print "a 不在list中"
else:
    print "a在list中"
if (b in list):
    print "b 在list中"
else:
    print "b 不在list中"
