# coding=utf-8
# Python break语句，就像在C语言中，打破了最小封闭for或while循环。
# break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。
# break语句用在while和for循环中。
# 如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。

for letter in "Python":  # 第一个实例
    if letter == "h":
        break
    print "当前字母：", letter

var = 10
while var > 0:  # 第二个实例
    print "当前变量值：", var
    var = var - 1
    if var == 5:  # 当 var =5时退出循环
        break
print "good bye "
