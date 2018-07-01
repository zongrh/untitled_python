# coding=utf-8
# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
# 语法：
# for循环的语法格式如下：
# for iterating_var in sequence:
#    statements(s)
for letter in "python":  # 第一个实例
    print "当前字母：", letter

fruits = ["banana", "apple", "mango"]
for fruit in fruits:  # 第二个实例
    print "当前水果：", fruit
print "goog bye "

# -----------------------通过序列索引迭代
fruits = ["banana", "apple", "mango", 11]
print "len= ", len(fruits)
for index in range(len(fruits)):
    print "当前水果----", fruits[index]
print "通过序列索引 Good Bye"
# ------------------------循环使用else语句
for num in range(10, 20):  # 迭代 10 - 20之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print "%d 等于 %d * %d" % (num, i, j)
            break #跳出当前循环
    else: #循环的else部分
        print num, "是一个质数"
