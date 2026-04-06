# num1
# from collections import deque
#
#
# def solve_network():
#     tokens = []
#
#     def next_token():
#         while not tokens:
#             try:
#                 line = input()
#                 tokens.extend(line.split())
#             except EOFError:
#                 return None
#         return tokens.pop(0)
#
#     network_id = 1
#
#     while True:
#         n_str = next_token()
#         if n_str is None:
#             break
#         n = int(n_str)
#
#         if n == 0:
#             break
#
#         s = int(next_token())
#         t = int(next_token())
#         c = int(next_token())
#
#         capacity = [[0] * (n + 1) for _ in range(n + 1)]
#         adj = [set() for _ in range(n + 1)]
#
#         for _ in range(c):
#             u = int(next_token())
#             v = int(next_token())
#             cap = int(next_token())
#
#             if u != v:
#                 capacity[u][v] += cap
#                 capacity[v][u] += cap
#                 adj[u].add(v)
#                 adj[v].add(u)
#
#         def bfs():
#             visited = [False] * (n + 1)
#             parent = [-1] * (n + 1)
#             queue = deque([s])
#             visited[s] = True
#
#             while queue:
#                 u = queue.popleft()
#                 for v in adj[u]:
#                     if not visited[v] and capacity[u][v] > 0:
#                         parent[v] = u
#                         visited[v] = True
#                         if v == t:
#                             return parent
#                         queue.append(v)
#             return None
#
#         max_flow = 0
#         while True:
#             parent = bfs()
#             if not parent:
#                 break
#
#             path_flow = float('inf')
#             curr = t
#             while curr != s:
#                 prev = parent[curr]
#                 path_flow = min(path_flow, capacity[prev][curr])
#                 curr = prev
#
#             curr = t
#             while curr != s:
#                 prev = parent[curr]
#                 capacity[prev][curr] -= path_flow
#                 capacity[curr][prev] += path_flow
#                 curr = prev
#
#             max_flow += path_flow
#
#         print(f"Network {network_id}")
#         print(f"The bandwidth is {max_flow}.")
#         print()
#         network_id += 1
#
#
# if __name__ == '__main__':
#     solve_network()
#
# num2
# from collections import defaultdict, deque
# 
# 
# def solve_cards():
#     tokens = []
# 
#     def next_token():
#         while not tokens:
#             try:
#                 line = input()
#                 tokens.extend(line.split())
#             except EOFError:
#                 return None
#         return tokens.pop(0)
# 
#     t_str = next_token()
#     if not t_str:
#         return
#     t = int(t_str)
# 
#     for _ in range(t):
#         n = int(next_token())
# 
#         initial_cards = defaultdict(int)
#         for _ in range(n):
#             card = int(next_token())
#             initial_cards[card] += 1
# 
#         e = int(next_token())
# 
#         source = 0
#         sink = n + 1
# 
#         graph = [[] for _ in range(n + 2)]
# 
#         def add_edge(u, v, cap, cost):
#             graph[u].append([v, cap, cost, len(graph[v])])
#             graph[v].append([u, 0, -cost, len(graph[u]) - 1])
# 
#         for card, count in initial_cards.items():
#             if 1 <= card <= n:
#                 add_edge(source, card, count, 0)
# 
#         for _ in range(e):
#             u, v = int(next_token()), int(next_token())
#             if 1 <= u <= n and 1 <= v <= n:
#                 add_edge(u, v, float('inf'), 1)
#                 add_edge(v, u, float('inf'), 1)
# 
#         for card in range(1, n + 1):
#             add_edge(card, sink, 1, 0)
# 
#         def spfa():
#             dist = [float('inf')] * (n + 2)
#             parent_edge = [None] * (n + 2)
#             parent_node = [-1] * (n + 2)
#             in_queue = [False] * (n + 2)
# 
#             queue = deque([source])
#             dist[source] = 0
#             in_queue[source] = True
# 
#             while queue:
#                 u = queue.popleft()
#                 in_queue[u] = False
# 
#                 for i, edge in enumerate(graph[u]):
#                     v, cap, cost, rev_idx = edge
#                     if cap > 0 and dist[u] + cost < dist[v]:
#                         dist[v] = dist[u] + cost
#                         parent_node[v] = u
#                         parent_edge[v] = i
# 
#                         if not in_queue[v]:
#                             queue.append(v)
#                             in_queue[v] = True
#             return dist, parent_node, parent_edge
# 
#         total_cost = 0
#         total_flow = 0
# 
#         while total_flow < n:
#             dist, parent_node, parent_edge = spfa()
# 
#             if dist[sink] == float('inf'):
#                 break
# 
#             path_flow = float('inf')
#             curr = sink
#             while curr != source:
#                 p = parent_node[curr]
#                 idx = parent_edge[curr]
#                 path_flow = min(path_flow, graph[p][idx][1])
#                 curr = p
# 
#             curr = sink
#             while curr != source:
#                 p = parent_node[curr]
#                 idx = parent_edge[curr]
#                 rev_idx = graph[p][idx][3]
# 
#                 graph[p][idx][1] -= path_flow
#                 graph[curr][rev_idx][1] += path_flow
#                 curr = p
# 
#             total_flow += path_flow
#             total_cost += path_flow * dist[sink]
# 
#         print(total_cost)
# 
# 
# if __name__ == '__main__':
#     solve_cards()
# 

