
#Ex1
# def cubeVolume(sideLength):
#     volume = sideLength**3
#     return volume
# reuslt1 = cubeVolume(2)
# print("A cube with side length 2 has ", reuslt1)
#
#
# def main():
#     result = cubeVolume(2)
#     print("A cube with side length 2 has volume", result)
# def cubeVolume(sideLength):
#     colume = sideLength**3
#     return colume
# main()

#Ex2
# input_list = [1,2,3,4,5,6,7,7]
# list_using_comp = [var for var in input_list if var%2==0]
# print("Output list using list comprehensions: ", list_using_comp)
#
# input_list2 = [1,2,3,4,5,66,7]
# dict_using_comp = {var: var**3 for var in input_list2 if var%2!=0}
# print("Output list using dictionary comp:", dict_using_comp)

#Ex3
input_list = [1,12,13,14,15,2,3]
list_using_list_comp = [var for var in input_list if var%5==0 and var>5]
print("Numbers greater and divisible by 5 from the list is: ", list_using_list_comp)
