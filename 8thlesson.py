#Recursion function problems
# def find_sum(n):
#     sum=0
#     for i in range(1, n+1):
#         sum+=i
#     return sum
# if __name__ == '__main__':
#     print(find_sum(6))
#
# def find_summ(n):
#     if n == 1:
#         return 1
#     return n + find_summ(n - 1)
#
# if __name__ == '__main__':
#     print(find_summ(6))


# def Fibonacci(n):
#     if n==0 :
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci((n-2))
# if __name__ == '__main__':
#     print(Fibonacci(6))


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
#
# if __name__ == '__main__':
#     print(factorial(5))

#checking prime
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# if __name__ == '__main__':
#     print(is_prime(7))
#     print(is_prime(10))
#
# def str_rcs(n):
#     if len(n) == 0:
#         return n
#     return n[-1] + str_rcs((n[:-1]))
# print(str_rcs("Nematullo"))

# def sum_dgt(n):
#     if n == 0:
#         return 0
#     return (n%10) + sum_dgt(n // 10)
# print(sum_dgt(1234))