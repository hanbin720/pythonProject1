# + 加 两个对象相加 a+b 输出结果30
# - 减 得到负数或是一个数减去另一个数 a-b 输出结果 -10
# * 乘 两个数相乘或是返回一个被重复若干次的字符串 a * b 输出结果200
# / 除 b/a 输出结果2
# // 取整除 返回商的整数部分 9//2 输出结果4 , 9.0//2.0 输出结果是4.0
# % 取余  返回除法的余数  b % a  输出结果0
# ** 指数  a**b 为10的20次方  输出结果

# # 请输入第一个数字a:
# a = int(input("请输入第一个数字a:"))
# # 请输入第二个数字b:
# b = int(input("请输入第二个数字b:"))
#
# # 加法
# ret1 = a + b
# print("加法结果:%d" % ret1)
#
# # 减法
# ret2 = a - b
# print("减法结果:%d" % ret2)
#
# # 乘法
# ret3 = a * b
# print("乘法结果:%d" % ret3)
#
# # 除法
# ret4 = a / b
# print("除法结果:%d" % ret4)

# // 取整除 返回商的整数部分 9//2 输出结果4 , 9.0//2.0 输出结果是4.0
# % 取余  返回除法的余数  b % a  输出结果0
# ** 指数  a**b 为10的20次方  输出结果
num1 = 10
num2 = 2
# 取整除
# ret5 = num1 // num2
# print(ret5)
# 取余
# ret6 = num1 % num2
# print(ret6)
# 指数
# ret7 = num2 ** num1
# print(ret7)

# ret8 = 10 ** 10000
# print(ret8)
# print(type(ret8))

# 注意:混合运算时:优先级顺序为:** 高于* /  %  //  高于 +  -  ,为了避免歧义,建议使用()来处理运算符优先级
(10 + 2) * 5