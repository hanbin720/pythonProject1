# 字符串其实就是一个有序的字符序列(顺序是不可以改变的)

# python中定义一个字符串 无论是单引号 还是双引号 是等价的
# 定义一个字符串
# name = "hello"
# name1 = 'hello'
# # 判断
# if name == name1:
#     print("name和name1是等价的")

# 定义一个空的字符串'' 或者"" 或者str()
# 空字符串 代表的就是 字符串中没有一个字符
# Python中提供了一个len函数(内置函数)计算字符串中的字符个数
# name = ""
# print(type(name))
# # 定义一个变量 记录字符个数
# l = len(name)
# print("name的字符个数:%d" % l)


# 哈喽
# 你好
# 世界
# print("哈喽\n你好\n世界")

# 保留其复制过来的文本格式 可以使用三引号( " 或者 ')
my_str ="""哈喽你好世界哈喽你好世界哈喽你好世界哈喽你好世界
哈喽你好世界哈喽你好世界哈喽你好世界
哈喽你好世界哈喽你好世界哈喽你好世界哈喽你好世界
哈喽你好世界哈喽你好世界
哈喽你好世界哈喽你好世界
哈喽你好世界"""
print(my_str)
print(len(my_str))