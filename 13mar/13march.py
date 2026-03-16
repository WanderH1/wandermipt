#num1
# import math
#
#
# def solve_spanning_tree():
#     n = int(input().strip())
#
#     points = []
#     for _ in range(n):
#         x, y = map(int, input().split())
#         points.append((x, y))
#
#     used = [False] * n
#     min_e = [float('inf')] * n
#     min_e[0] = 0.0
#     mst_weight = 0.0
#
#     for _ in range(n):
#         v = -1
#         for j in range(n):
#             if not used[j] and (v == -1 or min_e[j] < min_e[v]):
#                 v = j
#
#         used[v] = True
#         mst_weight += min_e[v]
#
#         for to in range(n):
#             if not used[to]:
#                 dist = math.hypot(points[v][0] - points[to][0],
#                                   points[v][1] - points[to][1])
#                 if dist < min_e[to]:
#                     min_e[to] = dist
#
#     print(mst_weight)
#
#
# if __name__ == '__main__':
#     solve_spanning_tree()
#
#num2
# import re
#
#
# def solve_boggle():
#     n = int(input().strip())
#
#     dictionary = input().strip().split()
#
#     m_l_line = []
#     while not m_l_line:
#         m_l_line = input().strip().split()
#     m, l = int(m_l_line[0]), int(m_l_line[1])
#
#     board_letters = []
#     while len(board_letters) < m * l:
#         line = input()
#         letters = re.findall(r'[A-Za-z]', line)
#         board_letters.extend(letters)
#
#     board = [board_letters[i * l:(i + 1) * l] for i in range(m)]
#
#     dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),
#             (-1, -1), (-1, 1), (1, -1), (1, 1)]
#
#     def dfs(r, c, word, index, visited):
#         if index == len(word):
#             return True
#
#         if (r < 0 or r >= m or c < 0 or c >= l or
#                 visited[r][c] or board[r][c] != word[index]):
#             return False
#
#         visited[r][c] = True
#
#         for dr, dc in dirs:
#             if dfs(r + dr, c + dc, word, index + 1, visited):
#                 return True
#
#         visited[r][c] = False
#         return False
#
#     found_words = set()
#
#     for word in dictionary:
#         found = False
#         for i in range(m):
#             for j in range(l):
#                 if board[i][j] == word[0]:
#                     visited = [[False] * l for _ in range(m)]
#                     if dfs(i, j, word, 0, visited):
#                         found_words.add(word)
#                         found = True
#                         break
#             if found:
#                 break
#
#     print(" ".join(sorted(list(found_words))))
#
#
# if __name__ == '__main__':
#     solve_boggle()
#
#num3 (acknowledgements to gemini)
# import time
# import random
# import heapq
#
#
# class DSU:
#
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.rank = [0] * n
#
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
#
#     def union(self, x, y):
#         root_x = self.find(x)
#         root_y = self.find(y)
#         if root_x == root_y:
#             return False
#
#         if self.rank[root_x] < self.rank[root_y]:
#             self.parent[root_x] = root_y
#         elif self.rank[root_x] > self.rank[root_y]:
#             self.parent[root_y] = root_x
#         else:
#             self.parent[root_y] = root_x
#             self.rank[root_x] += 1
#         return True
#
#
# def kruskal(n, edges):
#     dsu = DSU(n)
#     mst_weight = 0
#
#     sorted_edges = sorted(edges, key=lambda x: x[0])
#
#     for w, u, v in sorted_edges:
#         if dsu.union(u, v):
#             mst_weight += w
#     return mst_weight
#
#
# def prim(n, graph):
#     used = [False] * n
#     min_heap = [(0, 0)]
#     mst_weight = 0
#     edges_used = 0
#
#     while min_heap and edges_used < n:
#         w, u = heapq.heappop(min_heap)
#
#         if used[u]:
#             continue
#
#         used[u] = True
#         mst_weight += w
#         edges_used += 1
#
#         for v, weight in graph[u]:
#             if not used[v]:
#                 heapq.heappush(min_heap, (weight, v))
#
#     return mst_weight
#
#
# def generate_random_connected_graph(v, e):
#     edges = []
#     graph = [[] for _ in range(v)]
#
#     for i in range(1, v):
#         u = random.randint(0, i - 1)
#         w = random.randint(1, 100)
#         edges.append((w, i, u))
#         graph[i].append((u, w))
#         graph[u].append((i, w))
#
#     remaining_edges = e - (v - 1)
#     for _ in range(remaining_edges):
#         u = random.randint(0, v - 1)
#         v_node = random.randint(0, v - 1)
#         if u != v_node:
#             w = random.randint(1, 100)
#             edges.append((w, u, v_node))
#             graph[u].append((v_node, w))
#             graph[v_node].append((u, w))
#
#     return edges, graph
#
#
# def run_tests():
#     print(
#         f"{'Тест':<5} | {'Вершины (V)':<12} | {'Рёбра (E)':<10} | "
#         f"{'Время Краскала (сек)':<22} | {'Время Прима (сек)':<22}")
#     print("-" * 80)
#
#     test_cases = [
#         (100, 200), (100, 1000), (100, 4000),
#         (500, 1000), (500, 10000), (500, 100000),
#         (1000, 2000), (1000, 50000), (1000, 400000),
#         (2000, 4000), (2000, 100000), (2000, 1000000),
#         (5000, 10000), (5000, 250000), (5000, 2000000)
#     ]
#
#     for i, (v, e) in enumerate(test_cases, 1):
#         edges, graph = generate_random_connected_graph(v, e)
#
#         start_k = time.perf_counter()
#         kruskal_res = kruskal(v, edges)
#         time_k = time.perf_counter() - start_k
#
#         start_p = time.perf_counter()
#         prim_res = prim(v, graph)
#         time_p = time.perf_counter() - start_p
#
#         assert kruskal_res == prim_res,\
#             "Ошибка! Алгоритмы выдали разные веса MST."
#
#         print(f"{i:<5} | {v:<12} | {e:<10} |"
#               f"{time_k:<22.5f} | {time_p:<22.5f}")
#
#
# if __name__ == '__main__':
#     run_tests()
#
#num4
# import heapq
# 
# 
# def solve_districts():
#     first_line = []
#     while not first_line:
#         try:
#             first_line = input().split()
#         except EOFError:
#             return
# 
#     n = int(first_line[0])
#     m = int(first_line[1])
# 
#     centers = [int(x) for x in first_line[2:]]
# 
#     graph = [[] for _ in range(n)]
#     for _ in range(m):
#         line = []
#         while not line:
#             line = input().split()
#         u, v, w = map(int, line)
#         graph[u].append((v, w))
#         graph[v].append((u, w))
# 
#     dist = [float('inf')] * n
#     min_heap = []
# 
#     for c in centers:
#         dist[c] = 0
#         heapq.heappush(min_heap, (0, c))
# 
#     while min_heap:
#         d, u = heapq.heappop(min_heap)
# 
#         if d > dist[u]:
#             continue
# 
#         for v, weight in graph[u]:
#             if dist[u] + weight < dist[v]:
#                 dist[v] = dist[u] + weight
#                 heapq.heappush(min_heap, (dist[v], v))
# 
#     total_sum = 0
#     for d in dist:
#         if d != float('inf'):
#             total_sum += d
# 
#     print(total_sum)
# 
# 
# if __name__ == '__main__':
#     solve_districts()
# 
