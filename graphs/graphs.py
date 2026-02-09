# num1
# from collections import defaultdict
#
# graph = defaultdict(list)
# all_nodes = set()
#
# n = int(input())
# for i in range(n):
#     u, v = map(int,input().split())
#     graph[u].append(v)
#     graph[v].append(u)
#     all_nodes.add(u)
#     all_nodes.add(v)
#
#
# def bfs(graph, start_node):
#     visited = set()
#     queue = []
#     queue.append(start_node)
#     visited.add(start_node)
#     while queue:
#         node = queue.pop(0)
#         print(node)
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)
#     if len(visited) == len(all_nodes):
#         return True
#     else:
#         return False
#
#
# if all_nodes:
#     start_point = list(all_nodes)[0]
#     print(bfs(graph, start_point))
# else:
#     print(True)

#num2
# from collections import defaultdict
#
# n = int(input())
#
# graph = defaultdict(list)
#
# for i in range(n):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#
#
# def bfs(graph, start, target):
#     visited = set()
#     queue = [start]
#     visited.add(start)
#
#     while queue:
#         node = queue.pop(0)
#
#         if node == target:
#             return True
#
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)
#
#     return False
#
#
# a, b = map(int, input().split())
# print(bfs(graph, a, b))
#
# num3
# from collections import defaultdict
#
# graph = defaultdict(list)
# n = int(input())
# all_cities = set()
#
# for i in range(n):
#     u, v = map(str, input().split())
#     graph[u].append(v)
#     all_cities.add(u)
#     all_cities.add(v)
#
#
# def bfs(graph, start):
#     path = []
#     queue = [start]
#     visited = {start}
#
#     while queue:
#         node = queue.pop(0)
#         path.append(node)
#
#         for neighbour in graph[node]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)
#     return path
#
#
# for city in all_cities:
#     route = bfs(graph, city)
#     if len(route) == n + 1:
#         print(route)
#
# num4
# from collections import defaultdict
#
# graph = defaultdict(list)
# n = int(input())
# for _ in range(n):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)
#
# visited = set()
#
#
# def has_cycle(node, parent, graph):
#     visited.add(node)
#     for neighbor in graph[node]:
#         if neighbor == parent:
#             continue
#
#         if neighbor in visited:
#             return True
#
#         if has_cycle(neighbor, node, graph):
#             return True
#     return False
#
#
# print(has_cycle(0, 0, graph))
#
# num5
# import heapq
# from collections import defaultdict
# 
# graph = defaultdict(list)
# n = int(input())
# 
# for _ in range(n):
#     u, v, w = map(int, input().split())
#     graph[u].append((v, w))
# 
# start, end = map(int, input().split())
# 
# 
# def dijkstra(graph, start, end):
#     queue = [(0, start)]
#     costs = {start: 0}
# 
#     while queue:
#         cost, u = heapq.heappop(queue)
# 
#         if u == end:
#             return cost
# 
#         if cost > costs.get(u, float('inf')):
#             continue
# 
#         for v, weight in graph[u]:
#             new_cost = cost + weight
#             if new_cost < costs.get(v, float('inf')):
#                 costs[v] = new_cost
#                 heapq.heappush(queue, (new_cost, v))
#     return -1
# 
# 
# print(dijkstra(graph, start, end))
# 
# num6
# from collections import defaultdict
# 
# words = input().replace('[', '').replace(']', '').replace(',', '').split()
# n = len(words)
# graph = defaultdict(list)
# 
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             continue
#         if words[i][-1] == words[j][0]:
#             graph[i].append(j)
# 
# 
# def dfs(u, start, count, visited):
#     visited.add(u)
#     if count == n:
#         if words[u][-1] == words[start][0]:
#             return True
#         visited.remove(u)
#         return False
# 
#     for v in graph[u]:
#         if v not in visited:
#             if dfs(v, start, count + 1, visited):
#                 return True
# 
#     visited.remove(u)
#     return False
# 
# 
# found = False
# for i in range(n):
#     if dfs(i, i, 1, set()):
#         found = True
#         break
# 
# print(found)
#
