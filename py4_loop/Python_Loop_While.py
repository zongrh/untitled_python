# coding=utf-8
# while 判断条件：
#     执行语句……
count = 0
while (count < 9):
    print "The count is : ", count
    count = count + 1
print "Good bye "

# while 语句时还有另外两个重要的命令 continue，break 来跳过循环，
# continue 用于跳过该次循环，
# break 则是用于退出循环，
# 此外"判断条件"还可以是个常值，表示循环必定成立，具体用法如下：

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳出输出
        # print "非双数 i = ", i
        continue
    print "输出 i = ", i  # 输出双数

i = 1
while 1:  # 循环条件为 必定成立
    print i  # 输出1-10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break
# -----------------------无限循环
# var = 1
# while var == 1:
#     num = raw_input("Enter a number :")
#     print "Yout entered: ", num
# print "good bye"

count = 0
while count < 5:
    print count, "is < than 5"
    count = count + 1
else:
    print count, "is !< than 5"
# 简单语句
flag = 1
while (flag):
    print "Given flag is really true"
print "Good Bye"
