# coding=utf-8
# 字符串或串(String)是由数字、字母、下划线组成的一串字符。
# 一般记为 :
# s="a1a2···an"(n>=0)
# 它是编程语言中表示文本的数据类型。
# python的字串列表有2种取值顺序:
# 从左到右索引默认0开始的，最大范围是字符串长度少1
# 从右到左索引默认-1开始的，最大范围是字符串开头
var1 = 1
var2 = 10
print var1
print var2
del var1
del var2
print("--------------")
# ------------------------------Python字符串
str = "hello world"
print str  # 输出完整字符串
print str[0]  # 输出字符串中的第一个字符
print str[5]  # 输出字符串中的第五个字符（null）
print str[2:5]  # 输出字符串中的第三个至第五个之间的字符串
print str[2:]  # 输出第三字符开始的字符串
print str * 2  # 输出字符串两次
print str + "TEST"  # 输出链接的字符串
print("-------------")
