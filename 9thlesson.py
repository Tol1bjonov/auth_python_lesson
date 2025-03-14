#Hashability in Python

# class Point:
#     def __init__(self, x,y):
#         self.x = x
#         self.y =y
#     def __hash__(self):
#         return hash((self.x, self.y))
#
#     def __eq__(self, other):
#         if isinstance(other, Point):
#             return self.x == other.x and self.y == other.y
#         return False
#
# point1 = Point(1,2)
# point2 = Point(1,2)
# point3 = Point(3,4)
#
# points = {point1, point2, point3}
# print(len(points))

#2
# def is_hashsable(obj):
#     try:
#         hash(obj)
#         return True
#     except TypeError:
#         return False
# print(is_hashsable(42))
# print(is_hashsable([1,2,3]))


#3

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def __eq__(self, other):
#         if isinstance(other, Car):
#             return (self.brand, self.model, self.year) == (other.brand, other.model, other.year)
#         return False
#
#     def __hash__(self):
#         return hash((self.brand, self.model, self.year))
#
# # Testing in a set
# car1 = Car("Toyota", "Corolla", 2020)
# car2 = Car("Toyota", "Corolla", 2020)
# car3 = Car("Honda", "Civic", 2021)
#
# car_set = {car1, car2, car3}
# print(len(car_set))  # Output: 2 (car1 and car2 are considered the same)
#
# #3
# mutable_key = { "key": "value" }
#
# try:
#     my_dict = {mutable_key: "test"}
# except TypeError as e:
#     print(f"Error: {e}")
#
# #4
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return isinstance(other, Point) and (self.x, self.y) == (other.x, other.y)
#
#     def __hash__(self):
#         return hash(self.x + self.y)
#
# # Testing hash conflict
# p1 = Point(1, 2)
# p2 = Point(2, 1)
# p3 = Point(3, 0)
#
# point_set = {p1, p2, p3}
# print(len(point_set))
#
# #4
# class HashableObject:
#     def __init__(self, value):
#         self.value = value
#
#     def __hash__(self):
#         return hash(self.value)
#
# class NonHashableObject:
#     def __init__(self, value):
#         self.value = value
#
# hashable = HashableObject(10)
# non_hashable = NonHashableObject(20)
#
# my_set = {hashable}
#
# try:
#     my_set.add(non_hashable)
# except TypeError as e:
#     print(f"Error: {e}")
# #5
# key1 = frozenset([1, 2, 3])
# key2 = frozenset([4, 5, 6])
#
# my_dict = {key1: "Group A", key2: "Group B"}
# print(my_dict)

max_num = 0
def find_max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(f'the biggest number is {find_max(11,22,3)}')

# def factorial_cal():
#     i = 1
#     factorial = 1
#     n = int(input('enter a number: '))
#     while i <= n:
#         factorial = factorial * i
#         i = i + 1
#     return factorial
# print(f'{factorial_cal()}')

# def factorial_call():
#     i=1
#     factorial =1
#     n = int(input('enter the number: '))
#     while i <= n:
#         factorial = factorial*i
#         i = i+1
#     return factorial
# print(factorial_call())


def LinearSearch(arr, target):

        for i in range(len(arr)):

            if arr[i] == target:

             return i


        return -1


myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]

target = 7

index = LinearSearch(myList, target)


if index != -1:
    print(target, "was found at index", index)

else:
    print(target, "was not found")






