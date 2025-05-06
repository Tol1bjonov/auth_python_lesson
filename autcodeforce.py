#Lame King A
# t = int(input())
# for i in range(t):
#     a, b = map(int, input().split())
#     a = abs(a)
#     b = abs(b)
#     if a == b:
#         print(a * 2)
#     else:
#         print(max(a, b) * 2 - 1)

# H
# t=int(input())
# for i in range(t):
#     s=input()
#     a= int(s[0]) + int(s[1]) + int(s[2])
#     b = int(s[3]) + int(s[4]) + int(s[5])
#     if a == b:
#         print("yes")
#     else:
#         print("no")



# J
# banan_sum, dollar, banan = map(int, input().split())
# summa = banan_sum * banan * (banan + 1) / 2
# borow = max(0, summa - dollar)
#
# print(borow)
# import math
# print(math.factorial(9))

class Solution(object):
    def maxProduct(self, n):
        digits = [int(d) for d in str(n)]
        max_prod = 0
        for i in range(len(digits)):
            for j in range(i+1, len(digits)):
                product = digits[i] * digits[j]
                if product > max_prod:
                    max_prod= product
        return max_prod

sol =Solution()
print(sol.maxProduct(123))


a  = "Yusufjon"
for i in a:
    print(i)
