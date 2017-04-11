"""列表的一些常用运算符"""
list1 = [123]
list2 = [234]
print(list1 > list2)
""" 输出结果:
False
"""

"""列表中有多个元素，比较时从第0个开始，比较出的结果为最终结果"""
list1 = [123, 456]
list2 = [234, 123]
print(list1 > list2)
print(list1 < list2)
""" 输出结果:
False
True
"""

list4 = list1 + list2
print(list4)
""" 输出结果:
[123, 456, 234, 123]
"""

"""in 语法  not in """
print (123 in list4)
""" 输出结果:
True
"""

print(123 not in list4)
""" 输出结果:
False
"""

"""count(元素) 返回该元素在列表中出现的个数"""
print(list4.count(123))
""" 输出结果:
2
"""

print(list4.index(123))
""" 输出结果:
0
"""

"""reverse 将列表反序"""
list1.reverse()
print(list1)
""" 输出结果:
[456, 123]
"""

"""sort 根据指定的方式排序"""
list5 = [4, 2, 5, 6, 1, 9, 0]
list5.sort()
print(list5)
""" 输出结果:
[0, 1, 2, 4, 5, 6, 9]
"""

"""reverse参数默认为False"""
list5.sort(reverse = True)
print(list5)
""" 输出结果:
[9, 6, 5, 4, 2, 1, 0]
"""









