# 定义一个变量保存文件名
file_name= "hm.txt"

# 写数据(write)
# 以只写模式打开文件
# f = open(file_name,"w")
# # 写数据
# f.write("hello world")
# # 关闭文件
# f.close()


# 读数据(read)
# 以只读模式打开文件
# f = open(file_name, "r")
# # 读取数据
# ret = f.read()
# # 打印数据
# print(ret)
# # 关闭文件
# f.close()

# f = open(file_name, "r")
# # 读取数据
# ret = f.read(4)
# # 打印数据
# print(ret)
# ret = f.read(4)
# print(ret)
# # 关闭文件
# f.close()
"""
hell
o wo
# 第二个读取会接着上一个读取
"""


# 读数据 (readlines)
# # 以只读模式打开文件
# f = open(file_name, "r")
# # 读取数据
# # 把每行的数据保存到列表中
# ret = f.readlines()
# print(ret)
# f.close()


# 如果以w 方式打开文件  会吧原来文件的数据情况 然后在写入
# f = open(file_name, "w")
# f.write("nihao")
# f.close()


# a 追加数据
f = open(file_name, "a")
f.write("nihao")
f.close()