# 定义一个字符串
a = "abcdef"

# find
# 获取对应字符串的下标索引
# 如果查询到对应的字符串 会返回一个下标索引
# 如果没有查询到 会返回一个 -1
# ret1 = a.find("cdd")
# print(ret1)

# index
# 跟find()方法一样,只不过如果str不在mystr中会报一个异常
# ret2 = a.index("cdd")
# print(ret2)

# count
# 返回str在start和end之间 在mystr里面出现的次数
# ret3 = a.count("q")
# print(ret3)

# repalce
# 把mystr中的str1替换成str2,如果count指定,则替换不超过count次
# ret4 = a.replace("a","w",1)
# print(ret4)
# print(a)

# split
# 以str为分隔符切片mystr,如果maxsplit有指定值,则仅分隔maxsplit个子字符串
# ret5 = a.split("a")
# print(ret5)

# 可以使用count来判断下字符的个数 如果字符的个数大于0  存在index
count = a.count("a")
# 如果大于0
if count > 0:
    index = a.index("a")
    print(index)
