#coding=utf-8

# 元组是另一个数据类型，类似于List（列表）。
# 元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。

tuple = ("runoob", 1788, 2033, "jhon", 70.2)
tinytuple = (123456, "john")

print tuple  # 输出完整元组
print tinytuple  # 输出完整元组
print tuple[0]  # 输出元组第一个元素
print tuple[1:3]  # 输出第二个至第四个元素
print tuple[2:]  # 输出第三个开始至列表末尾所有元素
print tinytuple * 2#输出元组两次
print tuple + tinytuple#打印组合的元组
