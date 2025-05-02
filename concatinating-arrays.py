#Concatinating arrays

import numpy as np
#1
# a= np.array([1,2,3,4])
# b= np.array([5,6,7,8])
# print(np.concatenate((a,b)))

#2
# x= np.array([[1,2], [3,4]])
# y = np.array([[5,6]])
# print(np.concatenate((x,y), axis=0))

#3
# array_ex = np.array([[[0,1,2,3],
#                       [4,5,6,7]],
#
#                      [[0,1,2,3],
#                       [4,5,6,7]],
#
#                      [
#                       [0,1,2,3],
#                       [4,5,6,7]]])
# print(array_ex.ndim)

#4
# a = np.arange(6)
# print(a)
# b=a.reshape(3,2)
# print(b)

#5
# class ObjectCreate(object):
#     pass
# my_object = ObjectCreate()
# print(my_object)

#6
# class Snake:
#     name = "python"
#     def change_name(self, new_name):
#         self.name = new_name
# snake = Snake()
# print(snake.name)

#class examples
import numpy as np

# 1. Create a NumPy Array
arr_1d = np.arange(1, 11)
arr_2x5 = arr_1d.reshape(2, 5)
print("1. 2x5 Array:\n", arr_2x5)

# 2. Array Element-wise Operations
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("\n2. Element-wise Addition:\n", a + b)
print("Subtraction:\n", a - b)
print("Multiplication:\n", a * b)
print("Division:\n", a / b)

# 3. Array Broadcasting
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_1d = np.array([10, 20, 30])
broadcast_result = array_2d + array_1d
print("\n3. Broadcasting Result:\n", broadcast_result)

# 4. Array Indexing and Slicing
random_array = np.random.randint(0, 11, (5, 5))
diagonal_elements = np.diag(random_array)
print("\n4. 5x5 Array:\n", random_array)
print("Diagonal Elements:\n", diagonal_elements)

# 5. Matrix Multiplication
A = np.random.randint(1, 10, (3, 2))
B = np.random.randint(1, 10, (2, 4))
product = np.dot(A, B)
print("\n5. Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix Product:\n", product)

# 6. Array Aggregation
agg_array = np.random.rand(4, 4)
print("\n6. Aggregation Array:\n", agg_array)
print("Sum (entire):", np.sum(agg_array))
print("Mean (entire):", np.mean(agg_array))
print("Std Dev (entire):", np.std(agg_array))
print("Sum along axis 0:", np.sum(agg_array, axis=0))
print("Mean along axis 1:", np.mean(agg_array, axis=1))
