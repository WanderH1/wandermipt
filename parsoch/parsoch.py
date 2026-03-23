# num1
# def solve():
#     n, m = map(int, input().split())
#
#     adj = {i: [] for i in range(1, n + 1)}
#     for _ in range(m):
#         u, v = map(int, input().split())
#         adj[u].append(v)
#         adj[v].append(u)
#
#     colors = {}
#     possible = True
#
#     for i in range(1, n + 1):
#         if i not in colors:
#             colors[i] = 0
#             queue = [i]
#
#             while queue:
#                 curr = queue.pop(0)
#                 for neighbor in adj[curr]:
#                     if neighbor not in colors:
#                         colors[neighbor] = 1 - colors[curr]
#                         queue.append(neighbor)
#                     elif colors[neighbor] == colors[curr]:
#                         possible = False
#                         break
#         if not possible:
#             break
#
#     if possible:
#         print("YES")
#     else:
#         print("NO")
#
#
# solve()
#
# num2
# def solve_assignment():
#
#     def get_numbers():
#         while True:
#             line = input().strip()
#             if line:
#                 return list(map(int, line.split()))
#
#     n = get_numbers()[0]
#
#     cost = [[0] * (n + 1) for _ in range(n + 1)]
#     elements = []
#     while len(elements) < n * n:
#         elements.extend(get_numbers())
#
#     idx = 0
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             cost[i][j] = elements[idx]
#             idx += 1
#
#     u = [0] * (n + 1)
#     v = [0] * (n + 1)
#     p = [0] * (n + 1)
#     way = [0] * (n + 1)
#
#     for i in range(1, n + 1):
#         p[0] = i
#         j0 = 0
#         minv = [float('inf')] * (n + 1)
#         used = [False] * (n + 1)
#
#         while p[j0] != 0:
#             used[j0] = True
#             i0 = p[j0]
#             delta = float('inf')
#             j1 = 0
#
#             for j in range(1, n + 1):
#                 if not used[j]:
#                     cur = cost[i0][j] - u[i0] - v[j]
#                     if cur < minv[j]:
#                         minv[j] = cur
#                         way[j] = j0
#                     if minv[j] < delta:
#                         delta = minv[j]
#                         j1 = j
#
#             for j in range(n + 1):
#                 if used[j]:
#                     u[p[j]] += delta
#                     v[j] -= delta
#                 else:
#                     minv[j] -= delta
#
#             j0 = j1
#
#         while j0 != 0:
#             j1 = way[j0]
#             p[j0] = p[j1]
#             j0 = j1
#
#     print(-v[0])
#
#
# if __name__ == '__main__':
#     solve_assignment()
#
# num3
# Полное парасочетание - разбиение 6 вершин на 3 пары.
# Берём любую вершину: у неё 5 вариантов для выбора пары, для второй вершины (из 4) будет уже 3.
# Оставшиеся две определяют последнюю вершину - итого 5*3*1=15 вариантов.
#
# num4
# def solve():
#     n = int(input())
#     name = input().strip()
#     m = len(name)
#
#     cubes = []
#     for _ in range(n):
#         cubes.append(input().strip())
#
#     adj = [[] for _ in range(m)]
#     for i in range(m):
#         for j in range(n):
#             if name[i] in cubes[j]:
#                 adj[i].append(j)
#
#     match = [-1] * n
#
#     def dfs(v, visited):
#         for u in adj[v]:
#             if not visited[u]:
#                 visited[u] = True
#                 if match[u] == -1 or dfs(match[u], visited):
#                     match[u] = v
#                     return True
#         return False
#
#     ans = 0
#     for i in range(m):
#         visited = [False] * n
#         if dfs(i, visited):
#             ans += 1
#
#     if ans == m:
#         print("YES")
#         res = [0] * m
#         for j in range(n):
#             if match[j] != -1:
#                 res[match[j]] = j + 1
#         print(*res)
#     else:
#         print("NO")
#
#
# if __name__ == '__main__':
#     solve()
#
# bonus1
# import networkx as nx
#
# G1 = nx.Graph()
# G1.add_edges_from([(1, 2), (2, 3), (3, 4)])
#
# num_nodes = G1.number_of_nodes()
# num_edges = G1.number_of_edges()
# print(f"1) Число вершин: {num_nodes}, Число ребер: {num_edges}")
#
# components = sorted(nx.connected_components(G1), key=len, reverse=True)
# gcc = G1.subgraph(components[0])
#
# radius = nx.radius(gcc)
# diameter = nx.diameter(gcc)
# print(f"2) GCC - Радиус: {radius}, Диаметр: {diameter}")
#
# shortest_path_lengths = dict(nx.all_pairs_shortest_path_length(G1))
# print("3) Длины кратчайших путей:")
# for node, paths in shortest_path_lengths.items():
#     print(f"От вершины {node}: {paths}")

# bonus2 (aknowledgments to gemini)
# import networkx as nx
#
# G2 = nx.Graph()
# G2.add_edges_from([(1, 2), (2, 3), (3, 1)])
#
# density = nx.density(G2)
# num_components = nx.number_connected_components(G2)
# print(f"1) Плотность графа: {density:.3f},"
#       f"Число связных компонент: {num_components}")
#
# dfs_preds = nx.dfs_predecessors(G2, source=1)
# print(f"2) Словарь предшественников (DFS из 1): {dfs_preds}")
#
# K5 = nx.complete_graph(5)
# simple_paths = list(nx.all_simple_paths(K5, source=2, target=4))
#
# print("3) Простые пути из 2 в 4 в полносвязном графе (K5):")
# for path in simple_paths:
#     print(f"{path}")
#
