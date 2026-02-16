# num1
# from collections import defaultdict
# import sys
#
# sys.setrecursionlimit(10 ** 6)
#
#
# def find_social_clusters(n, relationships):
#
#     graph = defaultdict(list)
#     reversed_graph = defaultdict(list)
#
#     all_users = set()
#     if isinstance(n, int):
#         all_users = set(range(n))
#
#     for u, v in relationships:
#         graph[u].append(v)
#         reversed_graph[v].append(u)
#         all_users.add(u)
#         all_users.add(v)
#
#     visited = set()
#     stack = []
#
#     def dfs_fill_stack(u):
#         visited.add(u)
#         for v in graph[u]:
#             if v not in visited:
#                 dfs_fill_stack(v)
#         stack.append(u)
#
#     for user in all_users:
#         if user not in visited:
#             dfs_fill_stack(user)
#
#     visited.clear()
#     sccs = []
#
#     def dfs_collect_scc(u, current_component):
#         visited.add(u)
#         current_component.append(u)
#         for v in reversed_graph[u]:
#             if v not in visited:
#                 dfs_collect_scc(v, current_component)
#
#     while stack:
#         user = stack.pop()
#         if user not in visited:
#             component = []
#             dfs_collect_scc(user, component)
#             sccs.append(component)
#
#     for group in sccs:
#         group.sort()
#
#     sccs.sort(key=lambda x: (-len(x), x[0]))
#
#     return sccs
#
#
# if __name__ == "__main__":
#     n_users = 6
#     rels = [
#         (0, 1), (1, 2), (2, 0),
#         (3, 0),
#         (4, 5)
#     ]
#
#     result = find_social_clusters(n_users, rels)
#
#     print("Группы пользователей (кластеры):")
#     print(result)
#
# num2
# from collections import deque
#
#
# def knight_shortest_path(n, start_x, start_y):
#     moves = [
#         (-2, -1), (-2, 1), (-1, -2), (-1, 2),
#         (1, -2), (1, 2), (2, -1), (2, 1)
#     ]
#
#     dist = [[-1] * n for _ in range(n)]
#
#     dist[start_x][start_y] = 0
#     queue = deque([(start_x, start_y)])
#
#     while queue:
#         x, y = queue.popleft()
#
#         for dx, dy in moves:
#             nx, ny = x + dx, y + dy
#
#             if 0 <= nx < n and 0 <= ny < n:
#                 if dist[nx][ny] == -1:
#                     dist[nx][ny] = dist[x][y] + 1
#                     queue.append((nx, ny))
#
#     return dist
#
#
# if __name__ == "__main__":
#     N = 8
#     x0, y0 = 0, 0
#
#     result = knight_shortest_path(N, x0, y0)
#
#     print(f"Минимальные ходы коня из точки ({x0}, {y0}) на доске {N}x{N}:")
#     for row in result:
#         print(" ".join(f"{val:2}" for val in row))
#
#num3 (acknowledgements to gemini)
# import heapq
#
#
# def dijkstra_minimax(graph, start, end):
#
#     pq = [(0, start)]
#     min_max_dist = {node: float('inf') for node in graph}
#     min_max_dist[start] = 0
#
#     while pq:
#         curr_max, u = heapq.heappop(pq)
#
#         if curr_max > min_max_dist[u]:
#             continue
#         if u == end:
#             return curr_max
#
#         for v, w in graph.get(u, []):
#
#             new_cost = max(curr_max, w)
#             if new_cost < min_max_dist[v]:
#                 min_max_dist[v] = new_cost
#                 heapq.heappush(pq, (new_cost, v))
#     return float('inf')
#
#
# def dijkstra_product(graph, start, end):
#
#     pq = [(1, start)]
#     prod_dist = {node: float('inf') for node in graph}
#     prod_dist[start] = 1
#
#     while pq:
#         curr_prod, u = heapq.heappop(pq)
#
#         if curr_prod > prod_dist[u]:
#             continue
#         if u == end:
#             return curr_prod
#
#         for v, w in graph.get(u, []):
#
#             new_cost = curr_prod * w
#             if new_cost < prod_dist[v]:
#                 prod_dist[v] = new_cost
#                 heapq.heappush(pq, (new_cost, v))
#     return float('inf')
#
#
# def dijkstra_string(graph, start, end):
#
#     pq = [("", start)]
#     str_dist = {node: None for node in graph}
#     str_dist[start] = ""
#
#     while pq:
#         curr_str, u = heapq.heappop(pq)
#
#         if str_dist[u] is not None and curr_str > str_dist[u]:
#             continue
#         if u == end:
#             return curr_str
#
#         for v, w_str in graph.get(u, []):
#
#             new_cost = curr_str + w_str
#             if str_dist[v] is None or new_cost < str_dist[v]:
#                 str_dist[v] = new_cost
#                 heapq.heappush(pq, (new_cost, v))
#     return None
#
#
# def dijkstra_widest_path(graph, start, end):
#
#     pq = [(-float('inf'), start)]
#
#     max_min_dist = {node: -float('inf') for node in graph}
#     max_min_dist[start] = float('inf')
#
#     while pq:
#         val, u = heapq.heappop(pq)
#         curr_min = -val
#
#         if curr_min < max_min_dist[u]:
#             continue
#         if u == end:
#             return curr_min
#
#         for v, w in graph.get(u, []):
#
#             new_cost = min(curr_min, w)
#
#             if new_cost > max_min_dist[v]:
#                 max_min_dist[v] = new_cost
#                 heapq.heappush(pq, (-new_cost, v))
#     return -float('inf')
#
#
# def dijkstra_colors(graph, start, end, node_colors):
#
#     pq = [(0, 0, start)]
#
#     dists = {node: (float('inf'), float('inf')) for node in graph}
#     dists[start] = (0, 0)
#
#     while pq:
#         switches, w_sum, u = heapq.heappop(pq)
#
#         if (switches, w_sum) > dists[u]:
#             continue
#         if u == end:
#             return (switches, w_sum)
#
#         for v, w in graph.get(u, []):
#
#             is_switch = 1 if node_colors.get(u) != node_colors.get(v) else 0
#
#             new_switches = switches + is_switch
#             new_w_sum = w_sum + w
#             new_cost = (new_switches, new_w_sum)
#
#             if new_cost < dists[v]:
#                 dists[v] = new_cost
#                 heapq.heappush(pq, (new_switches, new_w_sum, v))
#
#     return (float('inf'), float('inf'))
#
