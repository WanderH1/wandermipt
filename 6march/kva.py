# num1
# import math
# import heapq
#
#
# def solve_frogger():
#
#     n = int(input())
#
#     stones = []
#     for _ in range(n):
#         x, y = map(float, input().split())
#         stones.append((x, y))
#
#     d = [float('inf')] * n
#     d[0] = 0.0
#
#     pq = [(0.0, 0)]
#
#     while pq:
#         curr_max, u = heapq.heappop(pq)
#
#         if curr_max > d[u]:
#             continue
#
#         if u == 1:
#             break
#
#         for v in range(n):
#             if u == v:
#                 continue
#
#             dx = stones[u][0] - stones[v][0]
#             dy = stones[u][1] - stones[v][1]
#             dist = math.hypot(dx, dy)
#
#             new_max = max(curr_max, dist)
#
#             if new_max < d[v]:
#                 d[v] = new_max
#                 heapq.heappush(pq, (new_max, v))
#
#     print(f"{d[1]:.3f}")
#
#
# solve_frogger()
#
# num2
# def solve_wormholes():
# 
#     cases = int(input())
# 
#     for _ in range(cases):
#         n, m = map(int, input().split())
# 
#         edges = []
#         for _ in range(m):
#             u, v, t = map(int, input().split())
#             edges.append((u, v, t))
# 
#         dist = [float('inf')] * n
#         dist[0] = 0
# 
#         for _ in range(n - 1):
#             for u, v, t in edges:
#                 if dist[u] != float('inf') and dist[u] + t < dist[v]:
#                     dist[v] = dist[u] + t
# 
#         has_negative_cycle = False
#         for u, v, t in edges:
#             if dist[u] != float('inf') and dist[u] + t < dist[v]:
#                 has_negative_cycle = True
#                 break
# 
#         if has_negative_cycle:
#             print("возможно")
#         else:
#             print("не возможно")
# 
# 
# if __name__ == "__main__":
#     solve_wormholes()
# 

