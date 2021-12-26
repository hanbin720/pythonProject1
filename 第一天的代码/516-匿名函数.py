# 匿名函数 藏匿名字的函数

# # lambda函数的语法只包含一个语句,如下:
# # lambda [arg1 [arg2, ...argn]]: expression
# # 其中 lambda是Python预留的关键字,arg和expression由用户自定义
# # 代码示例:
# # 普通Python函数
# def func(a, b, c):
#      return a + b + c
# print(func(1, 2, 3))
#  # 结果为6
#
#  # lambda 匿名函数
# f = lambda a, b, c : a + b + c
# print(f(1, 2, 3))
# # 结果为6
# # 在代码:f = lambda a, b, c : a + b + c 中, lambda表示匿名函数
# # 冒号":" 之前的 a,b ,c 表示它们是这个函数的参数
# # 匿名函数不需要return来返回值,表达式本身的结果就是返回值


# 对函数的简写

# # 无参数无返回值的函数
# # def my_print():
# #     print("hello python")
# # my_print()
#
# 表达式的定义
# f = lambda : print("hello python")
# # 执行
# f()
# # 等价于
# (lambda : print("hello python"))()


# # 无参数有返回值的函数
# def my_pi():
#     return 3.14
# print(my_pi())
#
# # 表达式的定义
# f = lambda : 3.14
# print(f())


# # 定义一个有参数无返回值的函数
# def my_print(name):
#     print("你好%s" % name)
# my_print("龟叔")
#
# f = lambda name: print("你好%s" % name)
# # 执行
# f("龟叔")


# 定义一个有参数有返回值的函数
# def add2num(a, b):
#     return a + b
#
# f = lambda a, b: a + b
# print(f(10, 20))


# ======================================

# 函数
# def fun(a, b, opt):
#     print("a = %d" % a)
#     print("b = %d" % b)
#     result = opt(a, b)
#     print("result = %d" % result)
#
# # 表达式
# f = lambda x, y: x + y
#
# # 调用函数
# fun(1, 2, f)


# f = lambda x, y: x + y
# def fun(a, b , opt):
#     result = opt(a,b)
#     print("结果:%d" % result)
# fun(10, 10, f)


# ===============================================
# 自定义排序 (最外层肯定是列表)
# my_list = [1, 4, -10, 20, 3]
# my_list.sort()
# print(my_list)


# stus = [{"name": "zhangsan", "age": 180}, {"name": "lisi", "age": 19}, {"name": "wangwu", "age": 17}]
# # [{'name': 'zhangsan', 'age': 180}, {'name': 'lisi', 'age': 19}, {'name': 'wangwu', 'age': 17}]
# # 按照年龄排序
# # [{'name': 'wangwu', 'age': 17}, {'name': 'lisi', 'age': 19}, {'name': 'zhangsan', 'age': 180}]
# print(stus)
# # stus.sort(key = lambda my_dict: my_dict["age"])
# # print(stus)
#
# # 按照名字排序
# # 使用的是每个名字的首字母排序(规则是按照ascii码完成的)
# stus.sort(key = lambda my_dict: my_dict["age"])
# print(stus)


# 列表的嵌套
my_list = [[10, 8, 9], [7, 10, 19], [9, 10, 29]]
# 按照列表元素(小列表)最后一个元素排序
my_list.sort(key=lambda new_list: new_list[2], reverse=True)
print(my_list)
