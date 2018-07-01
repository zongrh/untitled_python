# coding=utf-8
# Python pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句。
for letter in "python":
    if letter == "h":
        pass
        print "这pass块"
    print "当前字母：", letter
print "Good bye"
