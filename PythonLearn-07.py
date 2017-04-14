"""字符串"""

str1 = "I love fish"
print(str1[:6])
"""输出结果为：
I love
"""

print(str1[5])
"""输出结果为：
e
"""

"""将字符换的首字符变成大写 capitalize())"""
str2 = "hello"
print(str2.capitalize())
"""输出结果为：
Hello
"""

"""将整个字符串的所有字符改成小写 casefold())"""
str3 = "HELLO"
print(str3.casefold())
"""输出结果为：
hello
"""

"""将字符串居中，并使用空格填充值长度width的新字符串 center(width)"""
print(str2.center(40))
"""输出结果为：

"""

"""返回sub在字符串里面出现的次数，start和end参数表示范围，可选"""
print(str3.count('O'))
"""输出结果为：
1
"""


