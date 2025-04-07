# car_dict = {'a': "merc",
#             'b': "bmw",
#             'c': "ferrari",
#             'd': "lambo",
#             'e': "jeep"}
#
# car_dict = dict(map(lambda x: (x[0],x[1] + '_'), car_dict.items()))
# print("The modified dictionary is: ")
# print(car_dict)
#
# def example(i):
#     return i%3
# set_exm  = {33,102,62,96, 44, 28, 227}
# upd_exm = map(example , set_exm)
# print(upd_exm)
# print(set(upd_exm))


# def myMap (list1, list2):
#     return list1 + list2
# mylist1 = [2,3,4,5,6,7,8]
# mylist2 = [4,8,12,16,20,24,28]
# upd_list = map(myMap, mylist1, mylist2)
# print(upd_list)
# print(list(upd_list))

# num = [12,27, 24, 26, 9, 250, 451, 3, 10]
# even = list(filter(lambda x:(x%2==0), num))
# print(even)


# from functools import reduce
# numbers = [1,2,3,4]
# product  = reduce(lambda x,y: x*y, numbers)
# print(product)

#class project
#1
nums = [1,2,3,4]
dbl_num = list(map(lambda x: x*2, nums))
print(dbl_num)
#2
nums = ['1','2', '3']
int_nums = list(map(lambda x: int(x), nums))
print(int_nums)
#3
nums = [1,4,9,16]
sqr_nums = list(map(lambda x: x**2, nums))
print(sqr_nums)
#4
l1 = [1,2,3]
l2 = [4,5,6]
add_ls = list(map(lambda x,y: x+y, l1, l2))
print(add_ls)
#5
def to_fah(celsius):
    return list(map(lambda c: (c*9/5) + 32, celsius))
print(to_fah([0,25,100]))
#6
def evens(list4):
    return list(map(lambda b:  b%2==0, list4))
print(evens([1,2,3,4,5,6]))
#7
l_str = ['banana', 'yourbynnyvrot', 'semicolon']
str_mapped = list(map(lambda x: len(x), l_str))
print(str_mapped)
#8
word = ["apple", "banana", "cherry"]
lowercase = list(map(lambda x: x.upper(), word))
print(lowercase)
#9
numbers = [1,2,3,4,5]
square = list(map(lambda x: (x**2)*2, numbers))
print(square)