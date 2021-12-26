# 定义一个字符串
a = " 223abcd "

# ljust
# 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
# ret1 = a.ljust(10,"1")
# print(ret1)

# rjust
# 返回一个原字符串右对齐,并使用空格填充至长度width 的新字符串
# ret2 = a.rjust(10,"1")
# print(ret2)

# center
# 返回一个原字符串居中,并使用空格填充至长度width的新字符串
# ret3 = a.center(10,"2")
# print(ret3)

# lstrip
# 删除mystr 左边的空白字符(无论是空格 还是\n 或者是\t)
# \t 就是键盘上的tab键
# print(a)
# ret4 = a.lstrip("")
# print(ret4)

# rstrip
# 删除mystr 字符串末尾的空白字符
# ret5 = a.rstrip("3")
# print(ret5)

# strip
# 删除mystr字符串两端的空白字符
ret6 = a.strip()
print(ret6)
print(a)