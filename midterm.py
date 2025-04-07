#1
primes = [2,3,5,7,11]

#2
for i in range(2):
    primes[4 -i] = primes[i] #i = 1: primes[4 - 1] = primes[1] → primes[3] = 3
print(primes)

#3
for i in range(5):
    primes[i] = primes[i] +1
print(primes)

#4
values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
values[0] = 10
values[-1] = 10
print(values)

#5
responses = ["yes", "no"]

#7
names = ["Firtz"]
names.insert(1, "Ann")
names.insert(0, "Sue")
names.pop(2)
names.append("Lee")
print(names)

#8
my_list = [1, 2, 3, 2, 4, 2, 5]
my_list = [x for x in my_list if x!=2]
print(my_list)
while 2 in my_list:
    my_list.remove(2)
#9

#10 difference between [2]*3 and 2*[3]
print([2]*3)
print(2*[3])

#11 copying of list whithout list function
original = [1,2,3]
copy = original[:]
print(copy)
copy2 = original.copy()
print(copy2)
copy3 = [x for x in original]
print(copy3)

#12
numbers = [1,2,3,4,5,22]
average = sum(numbers)/len(numbers)
print(average)

#Set comprehensions
frameworks = { "Django", "NamPy", "Pandas"}
lowercase_set = set(map(lambda tag: tag.lower(), frameworks))
uppercase_set = {element.upper() for element in frameworks}
print(lowercase_set)
print(uppercase_set)
#4
ss = set()
for i in range(1,5):
    ss.add(i*i)
    ss.add(-i)
print(ss)
#5
s= set()
for i in range(0,20,2):
    s.add(i)
for i in range(0,20,3):
    s.discard(i)
print(s)

#Generator comprehensions

#1 even numbers square
even_gene_comp = (x**2 for x in range(1,21) if x%2==0)
for square in even_gene_comp:
    print(square)
#2 first 10 fibonacci sequence
def fibonacci(limit):
    a,b = 0,1
    for _ in range(limit):
        yield a
        a,b = b, a+b
fib_gen = (x for x in fibonacci(10))
for num in fib_gen:
    print(num)
#3 non-positive numbers
input_list = [12,-5,9,0,-3,7]
output_generator = (x for x in input_list if x>0)
for positive in output_generator:
    print(positive)

#4
cubes_generator = (x**3 for x in range(1,11))
for cubes in cubes_generator:
    print(cubes)


#Decorator function
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper
@my_decorator
def hello():
    print("Hello world")
hello()

#2
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function
@decorator_function
def display():
    print("Display fucntion executed")
display()