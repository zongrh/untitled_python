# coding=utf-8
var1 = "Hello World!"
var2 = "Python Runoob"
print "var1[0]:", var1[0]
print "var2[2]:", var2[1:5]

print "更新字符串：-", var1[:6] + "Runoob!"
# ------------------------------------------------------Python转义字符
# 在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符。如下表：
# 转义字符	描述
# \(在行尾时)	续行符
# \\	反斜杠符号
# \'	单引号
# \"	双引号
# \a	响铃
# \b	退格(Backspace)
# \e	转义
# \000	空
# \n	换行
# \v	纵向制表符
# \t	横向制表符
# \r	回车
# \f	换页
# \oyy	八进制数，yy代表的字符，例如：\o12代表换行
# \xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
# \other	其它的字符以普通格式输出

# -----------------------------------------------Python字符串运算符
# 下表实例变量 a 值为字符串 "Hello"，b 变量值为 "Python"：
# 操作符	描述	实例
# +	字符串连接
# >>>a + b
# 'HelloPython'
# *	重复输出字符串
# >>>a * 2
# 'HelloHello'
# []	通过索引获取字符串中字符
# >>>a[1]
# 'e'
# [ : ]	截取字符串中的一部分
# >>>a[1:4]
# 'ell'
# in	成员运算符 - 如果字符串中包含给定的字符返回 True
# >>>"H" in a
# True
# not in	成员运算符 - 如果字符串中不包含给定的字符返回 True
# >>>"M" not in a
# True
# r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
# >>>print r'\n'
# \n
# >>> print R'\n'
# \n
# %	格式字符串	请看下一章节
a = "hello"
b = "python"
print "a+b输出：", a + b
print "a*2 输出：", a * 2
print "a[1]输出：", a[1]
print "a[1:4]输出：", a[1:4]

if ("h" in a):
    print "h 在 a 中"
else:
    print "h 不在 a 中"

if ("m" not in a):
    print "m 不在 a 中"
else:
    print "m 在 a 中"
print r"\n"
print R"\n"
