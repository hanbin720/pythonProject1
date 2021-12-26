# 定义一个字符串
a = "abcdbef"

# rfind
# 类似于  find()函数,不过是从右边开发查找

# 从左侧到右侧查找
# ret1 = a.find("b")
# print(ret1)

# 从右侧到左侧查找
# ret2 = a.rfind("b")
# print


# rindex
# 类似于index(),不过是从右边开始,异常

# partition  开发中使用
# 把mystr 以str分隔成三部分,str前,str和str后
# ret2 = a.partition("c")
# print(type(ret2))
# print(ret2)

# repartition
# 类似于partition()函数,不过是从右边开始
ret3 = a.rpartition("c")
print(ret3)