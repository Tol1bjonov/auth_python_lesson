# def count_up_to(limit):
#     count = 0
#     while count < limit:
#         yield count
#         count +=1
# counter = (num for num in count_up_to((10)))
# for num in counter:
#     print(num)

# 1st task
# def square_up_to(num):
#     count =0
#     while count < num:
#         yield count
#         count+=1
# multiplied = (nums for nums in square_up_to(20))
# for nums in multiplied:
#     print(nums**2)

#1
even_squares = (x**2 for x in range(1,21) if x%2==0)
for square in even_squares:
    print(square)

#2nd task
def fibonacci(limit):
    a,b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a+b
fib_gen = (x for x in fibonacci(10))
for num in fib_gen:
    print(num)

#3rd task
nums = [12, -5, 9,0, -3, 7 ]
positive_nums = (y for y in nums if(y>0))
for nums in positive_nums:
    print(nums)

# 4th

