# coding=utf-8
# if 语句的判断条件可以用 >（大于）、 < (小于)、 == （等于）、
#  >= （大于等于）、 <= （小于等于）来表示其关系。

# if 判断条件：
#     执行语句……
# else：
#     执行语句……

flag = False
name = "luren"
if name == "python":  # 判断变量是否为”python“
    flag = True  # 条件成立时设置标志为 真
    print "welcome boss"  # 并输出欢迎信息
else:
    print name, flag  # 条件不成立时输出变量名称

# if 判断条件1:
#     执行语句1……
# elif 判断条件2:
#     执行语句2……
# elif 判断条件3:
#     执行语句3……
# else:
#     执行语句4……

num = 5
if num == 3:  # 判断num的值
    print "boss 3 "
elif num == 2:
    print "user 2"
elif num == 1:
    print "worker 1"
elif num < 0:  # 值小于零时输出
    print "error "
else:
    print "roadman"  # 条件均不成立时输出
# -------------------------------------------
num = 9
if num >= 0 and num < 10:  # 判断值是否在0-9之间
    print "hello"

num = 10
if num < 0 or num > 10:  # 判断值是否在小于0或者大于10之间
    print "hello"
else:
    print "undefine"

num = 8
# 判断值是否在0-5或者10-15之间
if (num >= 0 and num < 5) or (num < 10 and num <= 15):
    print "hello"
else:
    print "undefine"

var = 100
if (var == 100):
    print "变量var 的值为100"
print "good bye"
