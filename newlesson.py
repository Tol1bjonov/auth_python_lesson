from collections import Counter
from collections import deque
# s = 'lkserddfggdfgdgds'
# print("Most common three charcters of the said string: ")
# print(Counter(s).most_common(3))


# dq = deque('aeui')
# for element in dq:
#     print(element)

# n = int(input())
# arr = list(map(int, input().split()))
#
# max_sum = arr[0]
# current_sum = arr[0]
#
# for i in range(1, n):
#     current_sum = max(arr[i], current_sum + arr[i])
#     max_sum = max(max_sum, current_sum)
#
# print(max_sum)
#




#
# import sys
#
# def main():
#     input = sys.stdin.read().split()
#     idx = 0
#     t = int(input[idx])
#     idx += 1
#     for _ in range(t):
#         n = int(input[idx])
#         idx += 1
#         s = input[idx]
#         idx += 1
#         if n == 2:
#             print(int(s))
#             continue
#         min_total = float('inf')
#         for i in range(n-1):
#             groups = []
#             for j in range(i):
#                 groups.append(s[j])
#             groups.append(s[i] + s[i+1])
#             for j in range(i+2, n):
#                 groups.append(s[j])
#             group_vals = []
#             for g in groups:
#                 group_vals.append(int(g))
#             k = len(group_vals)
#             dp = [{} for _ in range(k)]
#             first_val = group_vals[0]
#             dp[0][first_val] = 0
#             for step in range(1, k):
#                 current_val = group_vals[step]
#                 prev_dp = dp[step-1]
#                 current_dp = {}
#                 for product in prev_dp:
#                     sum_so_far = prev_dp[product]
#                     new_sum_add = sum_so_far + product
#                     new_product_add = current_val
#                     if new_product_add in current_dp:
#                         if new_sum_add < current_dp[new_product_add]:
#                             current_dp[new_product_add] = new_sum_add
#                     else:
#                         current_dp[new_product_add] = new_sum_add
#                     new_sum_mul = sum_so_far
#                     new_product_mul = product * current_val
#                     if new_product_mul in current_dp:
#                         if new_sum_mul < current_dp[new_product_mul]:
#                             current_dp[new_product_mul] = new_sum_mul
#                     else:
#                         current_dp[new_product_mul] = new_sum_mul
#                 dp[step] = current_dp
#             if not dp[-1]:
#                 continue
#             current_min = min((s + p) for p, s in dp[-1].items())
#             if current_min < min_total:
#                 min_total = current_min
#         print(min_total)
#
# if __name__ == "__main__":
#     main()


def main():
    import sys
    input = sys.stdin.read().split()
    t = int(input[0])
    cases = input[1:t+1]
    for s in cases:
        n = len(s)
        min_cost = float('inf')
        max_len = 0
        for i in range(n):
            for j in range(i+1, n+1):
                substr = s[i:j]
                if int(substr) == 0:
                    continue
                sum_digits = sum(int(c) for c in substr)
                cost = int(substr) / sum_digits
                if cost < min_cost or (cost == min_cost and (j - i) > max_len):
                    min_cost = cost
                    max_len = j - i
                elif cost == min_cost and (j - i) == max_len:
                    pass
        print(n - max_len)

if __name__ == "__main__":
    main()