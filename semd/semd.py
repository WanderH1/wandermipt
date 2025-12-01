# num1
# import sys
#
#
# def build_tree(arr, n):
#     size = 1
#     while size < n:
#         size <<= 1
#
#     tree = [0] * (2 * size)
#
#     for i in range(n):
#         tree[size + i] = arr[i]
#
#     for i in range(size - 1, 0, -1):
#         tree[i] = max(tree[2 * i], tree[2 * i + 1])
#
#     return tree, size
#
#
# def query_max(tree, size, left, right):
#     left += size
#     right += size
#     max_val = 0
#
#     while left <= right:
#         if left % 2 == 1:
#             max_val = max(max_val, tree[left])
#             left += 1
#         if right % 2 == 0:
#             max_val = max(max_val, tree[right])
#             right -= 1
#
#         left //= 2
#         right //= 2
#
#     return max_val
#
#
# def main():
#     n = int(sys.stdin.readline().strip())
#     arr = list(map(int, sys.stdin.readline().strip().split()))
#     k = int(sys.stdin.readline().strip())
#
#     tree, size = build_tree(arr, n)
#
#     results = []
#     for _ in range(k):
#         left, right = map(int, sys.stdin.readline().strip().split())
#         left, right = min(left, right), max(left, right)
#         left -= 1
#         right -= 1
#
#         result = query_max(tree, size, left, right)
#         results.append(str(result))
#
#     print(" ".join(results))
#
#
# if __name__ == "__main__":
#     main()
#

# num2
# import sys
# import math
#
#
# def main():
#     try:
#         n_line = sys.stdin.readline()
#         if not n_line:
#             return
#         n = int(n_line.strip())
#
#         arr_line = sys.stdin.readline()
#         arr = list(map(int, arr_line.strip().split()))
#
#         k_line = sys.stdin.readline()
#         k = int(k_line.strip())
#
#         tree_size = 1
#         while tree_size < n:
#             tree_size <<= 1
#
#         tree = [0] * (2 * tree_size)
#
#         for i in range(n):
#             tree[tree_size + i] = arr[i]
#
#         for i in range(tree_size - 1, 0, -1):
#             tree[i] = math.gcd(tree[2 * i], tree[2 * i + 1])
#
#         results = []
#         for _ in range(k):
#             query_line = sys.stdin.readline()
#             if not query_line:
#                 break
#
#             left, right = map(int, query_line.strip().split())
#             left -= 1
#             right -= 1
#
#             if left > right:
#                 left, right = right, left
#
#             left_idx = left + tree_size
#             right_idx = right + tree_size
#             current_gcd = 0
#
#             while left_idx <= right_idx:
#                 if left_idx % 2 == 1:
#                     current_gcd = math.gcd(current_gcd, tree[left_idx])
#                     left_idx += 1
#                 if right_idx % 2 == 0:
#                     current_gcd = math.gcd(current_gcd, tree[right_idx])
#                     right_idx -= 1
#
#                 left_idx //= 2
#                 right_idx //= 2
#
#             results.append(str(current_gcd))
#
#         print(" ".join(results))
#
#     except Exception as e:
#         print(f"Ошибка: {e}")
#
#
# if __name__ == "__main__":
#     main()

# num3
# import sys
#
#
# def main() -> None:
#     data = []
#     for line in sys.stdin:
#         data.append(line.strip())
#
#     if not data:
#         return
#
#     n = int(data[0])
#     arr = list(map(int, data[1].split()))
#     m = int(data[2])
#
#     queries = []
#     for i in range(3, 3 + m):
#         left, right, k_value = map(int, data[i].split())
#         queries.append((left, right, k_value))
#
#     zeros = [1 if x == 0 else 0 for x in arr]
#
#     size = 1
#     while size < n:
#         size <<= 1
#
#     tree = [0] * (2 * size)
#
#     for i in range(n):
#         tree[size + i] = zeros[i]
#
#     for i in range(size - 1, 0, -1):
#         tree[i] = tree[2 * i] + tree[2 * i + 1]
#
#     def query_sum(left_idx: int, right_idx: int) -> int:
#
#         res = 0
#         left_idx += size
#         right_idx += size
#
#         while left_idx < right_idx:
#             if left_idx & 1:
#                 res += tree[left_idx]
#                 left_idx += 1
#             if right_idx & 1:
#                 right_idx -= 1
#                 res += tree[right_idx]
#             left_idx >>= 1
#             right_idx >>= 1
#
#         return res
#
#     results = []
#
#     for left_query, right_query, k_value in queries:
#         left_0 = left_query - 1
#         right_0 = right_query - 1
#
#         total_zeros = query_sum(left_0, right_0 + 1)
#
#         if total_zeros < k_value:
#             results.append("0")
#             continue
#
#         left_bound = left_0
#         right_bound = right_0
#         answer = -1
#
#         while left_bound <= right_bound:
#             mid = (left_bound + right_bound) // 2
#             zeros_count = query_sum(left_0, mid + 1)
#
#             if zeros_count >= k_value:
#                 answer = mid
#                 right_bound = mid - 1
#             else:
#                 left_bound = mid + 1
#
#         results.append(str(answer + 1))
#
#     print(" ".join(results))
#
#
# if __name__ == "__main__":
#     main()
#
