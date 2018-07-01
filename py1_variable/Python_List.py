# coding=utf-8
# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
# 列表用 [ ] 标识，是 python 最通用的复合数据类型。
# 列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
# 加号 + 是列表连接运算符，星号 * 是重复操作。如下实例：

list = ["runoob", 786, 2.23, "jhon", 70.25]
tinylist = [123, "jhon"]
print list  # 输出完整列表
print tinylist  # 输出完整列表
print list[0]  # 输出列表第一个元素
print list[1:3]  # 输出第二个至第四个元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list + tinylist  # 打印组合列表

# 因为元组是不允许更新的。而列表是允许更新的：
list = [111111, 22222]
print list
