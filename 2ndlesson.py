# def cubeVolume(a):
#     return a*a*a
# print(cubeVolume(3))
#
# print(cubeVolume(cubeVolume(2)))
#
# def squareArea(b):
#     return 4*b
# print(squareArea(4))
#
# def mystery(x,y):
#     result = (x+y)/ (y-x)
#     return result
# print(mystery(2,3))

# lambda function
# numbers = [1,2,3,4]
# squared = list(map(lambda x: x**2, numbers))
# evens = list(filter(lambda x: x%2==0, numbers))
# print(squared)
# print(evens)
#
# from functools import reduce
# product = reduce(lambda x, y: x*y, numbers)
# print(product)
#
# pairs = [(1,2), (4,1), (3,5)]
# sorter_pairs = sorted(pairs, key=lambda x: x[1])
# print(sorter_pairs)
#
#
# students = [
#     {"name": "Alice", "score" : 88, "age": 20},
#     {"name": "Bob", "score" : 92, "age": 22},
#     {"name": "Charlie", "score" : 88, "age": 19},
#     {"name": "David", "score" : 95, "age": 21},
# ]
#
# sorted_by_age_score = sorted(students, key=lambda x:(-x['score'],x['age']))
# print(sorted_by_age_score)
#
# words = ["apple", "banana", "cherry", "blueberry", "strawberry"]
# longest_word = reduce(lambda a, b: a if len(a) > len(b) else b, words)
# print(longest_word)

#
# numbers2 = [10,17, 19, 21, 23, 29, 30, 31]
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# numbers2 = [10, 17, 19, 21, 23, 29, 30, 31]
#
# non_primes = list(filter(lambda x: not is_prime(x), numbers2))
#
# print(non_primes)

words = ["hi", "hello", "to", "world", 'a', 'python']

capitalized_words = list(map(lambda word: word.capitalize() if len(word) > 3 else word, words))

print(capitalized_words)
