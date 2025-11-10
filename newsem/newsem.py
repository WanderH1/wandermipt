# num1
#
# def is_min_heap(arr: list) -> int:
#
#     n = len(arr)
#     for i in range(n):
#         left = 2 * i + 1
#         right = 2 * i + 2
#
#         if left < n and arr[i] > arr[left]:
#             return 0
#
#         if right < n and arr[i] > arr[right]:
#             return 0
#
#     return 1
#
#
# if __name__ == "__main__":
#     arr = list(map(int, input().split()))
#     print(is_min_heap(arr))
#
# num2
#
# def main() -> None:
#
#     french = set(map(int, input().split()))
#     swimmers = set(map(int, input().split()))
#     pianists = set(map(int, input().split()))
#
#     result = swimmers & pianists - french
#
#     sorted_result = sorted(result)
#     print(" ".join(map(str, sorted_result)))
#
#
# if __name__ == "__main__":
#     main()
#
# num3
#
# n = int(input())
# votes = {}
#
# for _ in range(n):
#     film = input().strip()
#     votes[film] = votes.get(film, 0) + 1
#
# sorted_films = sorted(votes.items(), key=lambda x: (-x[1], x[0]))
#
# for film, count in sorted_films:
#     print(f"{film} {count}")
#
# num4
#
# import sys
#
#
# def main() -> None:
#
#     n = int(sys.stdin.readline().strip())
#     lists = []
#
#     for _ in range(n):
#         line = sys.stdin.readline().strip()
#         if line:
#             lst = list(map(int, line.split()))
#             lists.append(lst)
#
#     combined = []
#     for idx, lst in enumerate(lists):
#         for num in lst:
#             combined.append((num, idx))
#
#     combined.sort(key=lambda x: x[0])
#
#     left = 0
#     count = [0] * n
#     unique_count = 0
#     min_range = [-10**9, 10**9]
#     min_diff = 10**9
#
#     for right in range(len(combined)):
#         num, list_idx = combined[right]
#         count[list_idx] += 1
#         if count[list_idx] == 1:
#             unique_count += 1
#
#         while unique_count == n and left <= right:
#             current_min = combined[left][0]
#             current_max = combined[right][0]
#             current_diff = current_max - current_min
#
#             condition = (
#                 current_diff < min_diff or
#                 (current_diff == min_diff and current_min < min_range[0])
#             )
#             if condition:
#                 min_diff = current_diff
#                 min_range = [current_min, current_max]
#
#             left_num, left_list_idx = combined[left]
#             count[left_list_idx] -= 1
#             if count[left_list_idx] == 0:
#                 unique_count -= 1
#             left += 1
#
#     print(f"{min_range[0]}-{min_range[1]}")
#
#
# if __name__ == "__main__":
#     main()
#
# num5
#
# def heapify(arr: list[int], n: int, i: int) -> None:
#
#     largest = i
#     left = 2 * i + 1
#     right = 2 * i + 2
#
#     if left < n and arr[left] > arr[largest]:
#         largest = left
#
#     if right < n and arr[right] > arr[largest]:
#         largest = right
#
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)
#
#
# def heap_sort(arr: list[int]) -> None:
#
#     n = len(arr)
#
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
#
#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
#
#
# def main() -> None:
#
#     arr = list(map(int, input().split()))
#     heap_sort(arr)
#     print(" ".join(map(str, arr)))
#
#
# if __name__ == "__main__":
#     main()
#
# num6
#
# def max_to_min_heap(arr: list[int]) -> None:
#
#     n = len(arr)
#     for i in range(n // 2 - 1, -1, -1):
#         min_heapify(arr, n, i)
#
#
# def min_heapify(arr: list[int], n: int, i: int) -> None:
#
#     smallest = i
#     left = 2 * i + 1
#     right = 2 * i + 2
#
#     if left < n and arr[left] < arr[smallest]:
#         smallest = left
#
#     if right < n and arr[right] < arr[smallest]:
#         smallest = right
#
#     if smallest != i:
#         arr[i], arr[smallest] = arr[smallest], arr[i]
#         min_heapify(arr, n, smallest)
#
#
# def main() -> None:
#
#     arr = list(map(int, input().split()))
#     max_to_min_heap(arr)
#     print(" ".join(map(str, arr)))
#
#
# if __name__ == "__main__":
#     main()
#
