# 字典是无序的  可变的

# 定义一个字典:  名字 年龄 学号
my_dict = {"name":"小红", "age":22, "no":"009"}

# 修改元素
# 字典的每个元素中的数据是可以修改的,只要通过key找到,即可修改
# 通过key 获取对应key的value的值
# print(my_dict["age"])
# # 通过key 修改对应key 的 value值
# my_dict["age"] =220
# print(my_dict)

# 添加元素
# title - "哈哈"
# 格式: 字典名[key] = value
# 如果使用上面的格式 如果这个key不存在 添加一组键值对
# 如果使用上面格式 如果这个key存在 会把key原来的value的值进行覆盖
# my_dict["title"] = "哈哈"
# print(my_dict)

# 删除元素
# 对字典中进行删除操作,有del(python内置函数)  clear
# 删除no 009
# 删除键值对  格式:del 字典名[key]
# del my_dict["no"]
# print(my_dict)

# clear 删除字典中的所有的元素
my_dict.clear()
# 等价于 my_dict = {}   或者my_dict = dict()
print(my_dict)