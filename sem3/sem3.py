#num1
# import heapq
#
#
# def solve():
#
#     n, m, s, f = map(int, input().split())
#
#     graph = {i: [] for i in range(n)}
#
#     for _ in range(m):
#         u, v, w = map(int, input().split())
#         graph[u].append((v, w))
#         graph[v].append((u, w))
#
#     distances = {i: float('inf') for i in range(n)}
#     distances[s] = 0
#
#     parents = {i: -1 for i in range(n)}
#
#     pq = [(0, s)]
#
#     while pq:
#         current_dist, u = heapq.heappop(pq)
#
#         if current_dist > distances[u]:
#             continue
#
#         for v, weight in graph[u]:
#             distance = current_dist + weight
#
#             if distance < distances[v]:
#                 distances[v] = distance
#                 parents[v] = u
#                 heapq.heappush(pq, (distance, v))
#
#     path_length = 0
#     current = f
#
#     while current != -1:
#         path_length += 1
#         current = parents[current]
#
#     print(path_length)
#
#
# if __name__ == '__main__':
#     solve()
#
#num2
# import ast
#
#
# def solve():
#
#     v, e = map(int, input().split())
#
#     adj_str = input().strip()
#
#     list_str = adj_str.replace('{', '[').replace('}', ']')
#     graph_array = ast.literal_eval(list_str)
#
#     used = [False] * v
#     has_cycle = False
#
#     def dfs(node: int, parent: int) -> None:
#         nonlocal has_cycle
#         used[node] = True
#
#         for neighbor in graph_array[node]:
#             if not used[neighbor]:
#                 dfs(neighbor, node)
#             elif neighbor != parent:
#
#                 has_cycle = True
#
#     for i in range(v):
#         if not used[i]:
#             dfs(i, -1)
#
#     if has_cycle:
#         print("'YES'")
#     else:
#         print("'NO'")
#
#
# if __name__ == '__main__':
#     solve()
#
# num3
# def solve():
#
#     n = int(input())
#
#     starts = list(map(int, input().split()))
#     ends = list(map(int, input().split()))
#
#     meetings = list(zip(starts, ends))
#     meetings.sort(key=lambda x: x[1])
#
#     count = 0
#     last_end = -1
#
#     for s, e in meetings:
#
#         if s > last_end:
#             count += 1
#             last_end = e
#
#     print(count)
#
#
# if __name__ == '__main__':
#     solve()
#
#num4 (acknowledgments to gemini)
# import heapq
# import json
# import networkx as nx
# import matplotlib.pyplot as plt
#
#
# def solve():
#
#     first_line = input().split()
#     v = int(first_line[0])
#     e = int(first_line[1])
#     start_station = first_line[2]
#     end_station = first_line[3]
#
#     graph = {}
#     edges_list = []
#
#     for _ in range(e):
#         u, v_node, time_str = input().split()
#         time = int(time_str)
#
#         if u not in graph:
#             graph[u] = []
#         if v_node not in graph:
#             graph[v_node] = []
#
#         graph[u].append((v_node, time))
#         graph[v_node].append((u, time))
#         edges_list.append((u, v_node, time))
#
#     distances = {node: float('inf') for node in graph}
#
#     if start_station not in distances:
#         distances[start_station] = float('inf')
#
#     distances[start_station] = 0
#     parents = {node: None for node in graph}
#
#     pq = [(0, start_station)]
#
#     while pq:
#         current_dist, current_node = heapq.heappop(pq)
#
#         if current_dist > distances.get(current_node, float('inf')):
#             continue
#
#         for neighbor, weight in graph.get(current_node, []):
#             distance = current_dist + weight
#
#             if distance < distances.get(neighbor, float('inf')):
#                 distances[neighbor] = distance
#                 parents[neighbor] = current_node
#                 heapq.heappush(pq, (distance, neighbor))
#
#     path = []
#     curr = end_station
#     while curr is not None:
#         path.append(curr)
#         curr = parents.get(curr)
#     path.reverse()
#
#     min_time = distances.get(end_station, -1)
#     print(min_time)
#
#     result_data = {
#         "start": start_station,
#         "end": end_station,
#         "min_time_minutes": min_time,
#         "path": path if min_time != float('inf') else []
#     }
#     with open("metro_path.json", "w", encoding="utf-8") as f:
#         json.dump(result_data, f, ensure_ascii=False, indent=4)
#
#     try:
#         g = nx.Graph()
#         for u, v_node, w in edges_list:
#             g.add_edge(u, v_node, weight=w)
#
#         pos = nx.spring_layout(g, seed=42)
#         plt.figure(figsize=(10, 8))
#
#         nx.draw_networkx_nodes(g, pos, node_color='lightblue', node_size=600)
#         nx.draw_networkx_edges(g, pos, edge_color='gray')
#         nx.draw_networkx_labels(g, pos, font_size=9)
#
#         edge_labels = nx.get_edge_attributes(g, 'weight')
#         nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
#
#         if min_time != float('inf') and len(path) > 1:
#             path_edges = list(zip(path, path[1:]))
#             nx.draw_networkx_nodes(g, pos, nodelist=path,
#                                    node_color='lightgreen', node_size=700)
#             nx.draw_networkx_edges(g, pos, edgelist=path_edges,
#                                    edge_color='red', width=2)
#
#         plt.title(f"Кратчайший путь от {start_station} до "
#                   f"{end_station} ({min_time} мин.)")
#         plt.axis('off')
#         plt.savefig("metro_graph.png")
#         plt.show()
#     except Exception as e:
#         print(f"Ошибка при визуализации: {e}")
#
#
# if __name__ == '__main__':
#     solve()
#
#num5
# from collections import deque
#
#
# def solve():
#     n, m = map(int, input().split())
#
#     graph = [[] for _ in range(n)]
#
#     for _ in range(m):
#         u, v = map(int, input().split())
#
#         graph[u].append(v)
#         graph[v].append(u)
#
#     distances = [-1] * n
#
#     distances[0] = 0
#
#     queue = deque([0])
#
#     while queue:
#
#         current = queue.popleft()
#
#         for neighbor in graph[current]:
#             if distances[neighbor] == -1:
#
#                 distances[neighbor] = distances[current] + 1
#
#                 queue.append(neighbor)
#
#     for d in distances:
#         print(d)
#
#
# if __name__ == '__main__':
#     solve()
#
#num6 (acknowledgments to gemini)
# import sys
#
# sys.setrecursionlimit(20000)
#
#
# def solve():
#
#     n = int(input())
#
#     m = int(input())
#
#     graph = {i: [] for i in range(n)}
#
#     for _ in range(m):
#         u, v = map(int, input().split())
#
#         graph[u].append(v)
#         graph[v].append(u)
#
#     used = [False] * n
#     components_count = 0
#
#     def dfs(node: int) -> None:
#         used[node] = True
#         for neighbor in graph[node]:
#             if not used[neighbor]:
#                 dfs(neighbor)
#
#     for i in range(n):
#         if not used[i]:
#
#             components_count += 1
#
#             dfs(i)
#
#     print(components_count)
#
#
# if __name__ == '__main__':
#     solve()
#
