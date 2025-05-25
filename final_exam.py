# map function
# def mul(i):
#     return i*i
# x = map(mul, (3,5,7,11,13))
# print(x)
# print(list(x))
#
# ez = ['welcome', "yusufjon", "dilshod"]
# y = map(len, ez)
# print(list(y))
#
# import math
# num = [9,4,5,6,7,8]
# swrt = map(math.sqrt, num)
# print(list(swrt))
#
# result = map(lambda i: i+i, num)
# print(list(result))
#
# def upper(n):
#     return n.upper()
# stri = "This is the python lesson"
# updt_list = map(upper, stri)
# print(list(updt_list))
#
# l = ['sat', 'bat', 'cat', 'mat']
# test = list(map(list, l))
# print(test)
#
# def example(s):
#     return s.upper()
# tuple_exm = ('this', 'is', 'the', 'map')
# upd_tup = map(example, tuple_exm)
# print(tuple(upd_tup))
#
# car_dict = {
#     'a':"mercedec",
#     'b': "bmw",
#     'c': "ferrari",
#     'd': "lambo"
# }
# car_dict = dict(map(lambda x: (x[0] + '+', x[1] + '_'), car_dict.items()))
# print('the modifies version is: ')
# print(car_dict)
#
# def example2(i):
#     return i%3
# set_exm = {33,23,4545,454,62,543,532}
# upds_itms = map(example2, set_exm)
# print(set(upds_itms))
# import functools
# #reduce function
# from functools import reduce
#
# product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
# print(product)
#
# lis = [1,2,3,4,5]
# print("the maximum value is: ", end="")
# print(functools.reduce(lambda a,b: a if a>b else b, lis))


#classtask
# num = [1,2,3,4]
# new_num = list(map(lambda x: x+x, num))
# print(new_num)
#
# num2 = ['1','2', '3']
# new_num2 = list(map(lambda y: int(y), num2))
# print(new_num2)
#
# def add_twp(list1, list2):
#     return list1 + list2
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# new_list = map(add_twp, list1, list2)
# print(list(new_list))
#
#
# words = ["apple", "banana", "cherry"]
# upper_word = map(lambda x: x.upper(), words)
# print(list(upper_word))

#Numpy and Metaclasses
import numpy as np
# a = np.array([1,2,3,4,5,6])
# print(a)
# print(type(a))
# print(np.__version__)
#
# arr = np.array((1,2,3,4,5))
# print(arr)

print(np.empty(3))
print(np.array([3.14, 42. ]))
print(np.arrange(2,9,2))
print(np.array([2,4,6,8]))

