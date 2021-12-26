# 添加元素(append,extend,insert)
# 列表是可变的 (如果对当前列表的操作 是在原有的列表上进行更改)
# 定义一个列表
my_list = [1, 3]
# # append 添加一个整体(一个对象)
# my_list.append([4,5])
# print(my_list)
# # [1, 3, [4, 5]]


# extend 添加一个可以遍历的对象(有序的字符序列)    会被拆分后在添加
# my_list.extend("456")
# print(my_list)
# # [1, 3, '4', '5', '6']


# insert   可选择下标选择添加的位置 整体添加
my_list.insert(1,"hello")
print(my_list)