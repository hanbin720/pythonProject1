# and  x and y 布尔"与":若果x为False,x and y 返回False,否则它返回y的值.True and False,返回False
# or  x or y 布尔"或":如果x是True,否则它返回y的值.False or True ,返回True
# not  not x 布尔"非":如果x为True,返回False.如果x为False,它返回True.not True 返回False,not False返回True

# # 定义一个变量 记录名字
# my_name = "mngr"
# # 定义一个变量  记录密码
# my_passwd = "12345"
#
# # 使用and "且" 或者 "与
# # 同真为真(True)  一假为假(False)
# # 进行判断
# if my_name == "mngr" and my_passwd == "12345":
#     print("用户名和密码正确登录成功")


# # or  或
# # 定义一个变量 记录名字
# my_name = "mngr"
# # 定义一个变量 记录密码
# my_passwd ="12345"
#
# # 全假为假 一真则真
# if my_name != "mngr" or my_passwd != "123456":
#     print("您输入的用户名或者密码错误!!!")


# not 非
# 非真则假  非假则真
is_man = False
print(is_man)
if not is_man:
    print("是女性")
