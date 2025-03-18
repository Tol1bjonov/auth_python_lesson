# write a lambda function to find the sum of two numbers pycharmcode123
#use set comprehension to create a set of vowels from a given string
#write a recursion function to calculate the factorial of a given number
#write a generator comprehension to generate even numbers from 1 to 10
#write a decorator function that adds a prefix "Hello", to the result of any function it decorates
#1
sum_lambda = lambda a, b: a + b
result = sum_lambda(5, 3)
print(result)

#2
vowels = {'a', 'e', 'i', 'o', 'u'}
get_vowels = lambda s: {char for char in s.lower() if char in vowels}
result = get_vowels("Hello, World!")
print(result)

#3
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = 5
print(factorial(num))

#4
even_numbers = (num for num in range(1, 11) if num % 2 == 0)
for num in even_numbers:
    print(num)

#5
def add_hello_prefix(func):
    def wrapper(*args, **kwargs):
        return "Hello, " + func(*args, **kwargs)
    return wrapper

@add_hello_prefix
def greet(name):
    return name

print(greet("Yusufjon"))

