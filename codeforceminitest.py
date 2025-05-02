#A+B+C
# a, b, c = map(int, input().split())
#
# result = a + b + c
#
# print(result)

#Baby Geometry
# a, b, c = map(int, input().split())
#
# if a + b > c and b + c > a and c + a > b:
#     print("Yes")
# else:
#     print("No")

# Read the number of elements

#Count odd numbers
# n = int(input())
#
# arr = list(map(int, input().split()))
# odd_count = sum(1 for num in arr if num % 2 == 1)
# print(odd_count)

#Increasing
# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#
#     if len(set(a)) == n:
#         print("YES")
#     else:
#         print("NO")

#Baby girl
# username = input()
# unique_chars = set(username)
#
# if len(unique_chars) % 2 == 0:
#     print("CHAT WITH HER!")
# else:
#     print("IGNORE HIM!")

#Beautifull matrix
# matrix = []
#
# for i in range(5):
#     row = list(map(int, input().split()))
#     matrix.append(row)
#     for j in range(5):
#         if row[j] == 1:
#             x, y = i, j
# moves = abs(x - 2) + abs(y - 2)
# print(moves)

#Genrers line
# from collections import Counter
#
# n = int(input())
# slopes = []
#
# for _ in range(n):
#     a, b = map(int, input().split())
#     slopes.append(a)
#
# slope_count = Counter(slopes)
#
# total_pairs = n * (n - 1) // 2
# non_intersecting = sum(count * (count - 1) // 2 for count in slope_count.values())
#
# print(total_pairs - non_intersecting)

# Divisibility trick
# d = int(input())
#
# if d == 1:
#     print(1)
# else:
#
#     n = str(d) * d
#     print(n)

l, h = map(int, input().split())
if l % 2 == 1:
    print(h)
else:
    print(2 * (h // 2))
