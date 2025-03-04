# array2 = [1,2,3,4,5,6, 7]
# maxNum = array2[0]
# for num in array2:
#     if num> maxNum:
#         maxNum=num
# print("Max num is: ", maxNum)

# input_list = [1,2,3,4,5,6,7,7]
# output_list = []
#
# for var in input_list:
#     if var%2==0:
#         output_list.append(var)
# print("output using for loop: ", output_list)
#
# list_using_comp = [var for var in input_list if var%2==0]
# print("output using comprehension: ", list_using_comp)

# output_list = []
# for var in range(1,10):
#     output_list.append(var**2)
# print("output using for loop: ", output_list)
#
# list_using_comp = [var**2 for var in range(1,10)]
# print("output using comp: ", list_using_comp)


#
# # 1
# primes = [2, 3, 5, 7, 11]
#
# # 2
# for i in range(2):
#     primes[4 - i] = primes[i]
#
# print(primes)
#
# # 3
# for i in range(5):
#     primes[i] = primes[i] + 1
#
# print(primes)
#
# # 4
# values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# values[0] = 10
# values[-1] = 10
#
# print(values)
# responses = ["Yes", "No"]
#
# print(responses)


# 7
names = ["Fritz"]
names.insert(1, "Ann")
names.insert(0, "Sue")
names.pop(2)
names.append("Lee")
print(names)

# 8
def remove_all(lst, value):
    return [x for x in lst if x != value]

my_list = [1, 2, 3, 2, 4, 2, 5]
print(remove_all(my_list, 2))

# 9
a = [1, 2]
b = [2, 1]
print(a + b == b + a)
print(a == b)

# 10
print([2] * 3)
print(2 * [3])

# 11
original_list = [1, 2, 3]
copy1 = original_list[:]
copy2 = [x for x in original_list]
copy3 = original_list.copy()

print(copy1, copy2, copy3)

# 12
def compute_average(lst):
    return sum(lst) / len(lst)

numbers = [10, 20, 30, 40, 50]
print(compute_average(numbers))



