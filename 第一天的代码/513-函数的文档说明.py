
# 假设 len 函数
# 函数的文档说明 -> 加的文档说明是Python
# help(len)
# len python 内置行数 python 创建


# 很多的时候需要程序员自己创建

# # 自定义一个函数
# def add2num(num1, num2):
#     return num1 + num2
#
# # 如果一个自定义函数 没有文档说明 默认是用 help 会打印函数上面的注释
# help(add2num)



# 自定义一个函数
# def add2num(num1, num2):
#     """
#     这个函数是用来计算两个数的和的
#     :param num1: 数字1
#     :param num2: 数字2
#     :return: 返回值是两个数相加
#     """
#     return num1 + num2
#
# help(add2num)



# 函数
def my_func(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    # 单行注释
    num = 10
    return a + b + num

"""
01- 可以在时间过了很久后 快速读懂自己的代码
02- 便于工作的交接
# 习惯 和 公司的要求
"""