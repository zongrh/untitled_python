# coding=utf-8
# =	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
# +=	加法赋值运算符	c += a 等效于 c = c + a
# -=	减法赋值运算符	c -= a 等效于 c = c - a
# *=	乘法赋值运算符	c *= a 等效于 c = c * a
# /=	除法赋值运算符	c /= a 等效于 c = c / a
# %=	取模赋值运算符	c %= a 等效于 c = c % a
# **=	幂赋值运算符	c **= a 等效于 c = c ** a
# //=	取整除赋值运算符	c //= a 等效于 c = c // a

a = 5
b = 2
c = 0

c = a + b
print c

c += a
print "c+=a", c

c *= a
print "c*=a", c
c /= a
print "c/=a", c
c = 2
c %= a
print "c%=a", c
c **= a
print "c**=a", c
c // a
print "c//a", c
