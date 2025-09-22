# num1
# def fib(n):
#     if n < 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# num = int(input())
# print(fib(num))

#num2
# import math
# def func1(a):
#     m=set()
#     for i in range(1, int(math.ceil(a**0.5))+1):
#         if a % i == 0:
#             m.add(i)
#             m.add(int(a/i))
#     m=sorted(list(m))[1:]
#     return m
# a = int(input())
# if a == 1:
#     print("a = 1")
# else:
#     print(f"a = {' * '.join(map(str, func1(a)))}")

#num3
# import sys
# def extended_gcd(a, b):
#     x0, x1 = 1, 0
#     y0, y1 = 0, 1
#     while b:
#         q = a // b
#         a, b = b, a % b
#         x0, x1 = x1, x0 - q * x1
#         y0, y1 = y1, y0 - q * y1
#     return a, x0, y0
#
# for line in sys.stdin:
#     data = line.split()
#     if not data:
#         continue
#     a = int(data[0])
#     b = int(data[1])
#     d, x0, y0 = extended_gcd(a, b)
#     t = b // d
#     s = a // d
#
#     candidates = set()
#     candidates.add(0)
#     if t != 0:
#         k_floor = (-x0) // t
#         k_ceil = (-x0 + t - 1) // t
#         candidates.add(k_floor)
#         candidates.add(k_ceil)
#     if s != 0:
#         k2_floor = y0 // s
#         k2_ceil = (y0 + s - 1) // s
#         candidates.add(k2_floor)
#         candidates.add(k2_ceil)
#
#     best_x = None
#     best_y = None
#     best_sum = None
#
#     for k in candidates:
#         x = x0 + k * t
#         y = y0 - k * s
#         current_sum = abs(x) + abs(y)
#         if best_sum is None or current_sum < best_sum or (current_sum == best_sum and x < best_x):
#             best_x = x
#             best_y = y
#             best_sum = current_sum
#
#     print(f"{best_x} {best_y} {d}")

#num4
# def tr(size, symb, c=""):
#     for i in range(size+1):
#         n=int(-abs((size+1)/2-i)+(size+1)/2)
#         c+=f"{symb*n}\n"
#     return c
# print(tr(5,"ca"))

# num5
# def spiral_matrix(n, m):
#     matrix = [[0] * m for _ in range(n)]
#     top, bottom, left, right = 0, n - 1, 0, m - 1
#     num = 1
#
#     while num <= n * m:
#         for i in range(left, right + 1):
#             if num > n * m:
#                 break
#             matrix[top][i] = num
#             num += 1
#         top += 1
#
#         for i in range(top, bottom + 1):
#             if num > n * m:
#                 break
#             matrix[i][right] = num
#             num += 1
#         right -= 1
#
#         for i in range(right, left - 1, -1):
#             if num > n * m:
#                 break
#             matrix[bottom][i] = num
#             num += 1
#         bottom -= 1
#
#         for i in range(bottom, top - 1, -1):
#             if num > n * m:
#                 break
#             matrix[i][left] = num
#             num += 1
#         left += 1
#
#     return matrix
#
# def multiply_rows_by_index(matrix):
#     result = []
#     for i, row in enumerate(matrix):
#         new_row = [elem * i for elem in row]
#         result.append(new_row)
#     return result
#
# def print_matrix(matrix):
#     for row in matrix:
#         print(' '.join(f'{num:4}' for num in row))
#
# n, m = 6, 7
# spiral = spiral_matrix(n, m)
# result = multiply_rows_by_index(spiral)
# print_matrix(result)

# num6
# def mnk(m1,m2, ach = 0, azn = 0):
#     if len(m1) != len(m2) or len(m1) == 0:
#         return 0
#     else:
#         sr1 = sum(m1)/len(m1)
#         sr2 = sum(m2)/len(m2)
#         for i in range(len(m1)):
#             ach += (m1[i]-sr1)*(m2[i]-sr2)
#             azn += (m1[i]-sr1)**2
#         a = ach/azn
#         b = sr2 - a*sr1
#         return a,b
#
# x = list(map(int, input().split()))
# y = list(map(int, input().split()))
# print(f"y = {mnk(x,y)[0]} * x + {mnk(x,y)[1]}")



#num7
# def gaussian_elimination():
#     N, M = map(int, input().split())
#     matrix = []
#     for _ in range(N):
#         row = list(map(float, input().split()))
#         matrix.append(row)
#
#     for col in range(min(N, M - 1)):
#         for r in range(col, N):
#             if abs(matrix[r][col]) > 1e-10:
#                 matrix[col], matrix[r] = matrix[r], matrix[col]
#                 break
#         else:
#             continue
#
#         divisor = matrix[col][col]
#         for j in range(col, M):
#             matrix[col][j] /= divisor
#
#         for i in range(col + 1, N):
#             factor = matrix[i][col]
#             for j in range(col, M):
#                 matrix[i][j] -= factor * matrix[col][j]
#
#     for i in range(N):
#         all_zeros = all(abs(matrix[i][j]) < 1e-10 for j in range(M - 1))
#         if all_zeros and abs(matrix[i][M - 1]) > 1e-10:
#             print("Нет решений")
#             return
#
#     solution = [0] * (M - 1)
#     for i in range(min(N, M - 1) - 1, -1, -1):
#         solution[i] = matrix[i][M - 1]
#         for j in range(i + 1, M - 1):
#             solution[i] -= matrix[i][j] * solution[j]
#
#     if len(solution) < M - 1:
#         print("Бесконечно много решений")
#     else:
#         for x in solution:
#             print(f"{x:.3f}", end=" ")
#         print()
# gaussian_elimination()

# num8
# import random
# def gen(N, mean = 0, st = 1):
#     return [random.gauss(mean, st) for i in range(N)]
# def mnk(m1,m2, ach = 0, azn = 0):
#     sr1 = sum(m1)/len(m1)
#     sr2 = sum(m2)/len(m2)
#     for i in range(len(m1)):
#         ach += (m1[i]-sr1)*(m2[i]-sr2)
#         azn += (m1[i]-sr1)**2
#     a = ach/azn
#     b = sr2 - a*sr1
#     return a,b
# N = int(input())
# n1 = gen(N)
# n2 = gen(N)
# print(f"y = {mnk(n1,n2)[0]} * x + {mnk(n1,n2)[1]}")












