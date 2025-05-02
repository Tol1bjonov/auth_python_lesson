#Itertools
import itertools

#1
# result = itertools.count(start=0, step=2)
# for number in result:
#     if number < 8:
#         print(number)
#     else:
#         break
# print(result)

#2
# result = itertools.cycle('123456')
# counter = 0
# for number in result:
#     if counter <10:
#         print(number)
#         counter=counter+1
#     else:
#         break
# print(result)

#3
# result = itertools.repeat('hello', times=2)
# for word in result:
#     print(word)

#4
# from typing import Iterable
#
# def running_product(iterable: Iterable):
#     result = []
#     product = 1
#     for num in iterable:
#         product *= num
#         result.append(product)
#     return result
#
# numbers = [1, 2, 3, 4, 5]
# print("Original list:", numbers)
# print("Running product:", running_product(numbers))


#5
import itertools as it
def cycle_data(iter):
    return it.cycle(iter)
result = cycle_data(['A', 'B', 'C'])
print('the')
for i in result:
    print(i)
