def min_edge_cover_bipartite(U_size, V_size, edges):
    match_U = [-1] * U_size
    match_V = [-1] * V_size

    def dfs(u, visited):
        for v in edges[u]:
            if not visited[v]:
                visited[v] = True
                if match_V[v] == -1 or dfs(match_V[v], visited):
                    match_U[u] = v
                    match_V[v] = u
                    return True
        return False

    max_matching = 0
    for u in range(U_size):
        if dfs(u, [False] * V_size):
            max_matching += 1

    edge_cover = []
    for u in range(U_size):
        if match_U[u] != -1:
            edge_cover.append((u, match_U[u]))

    for v in range(V_size):
        if match_V[v] == -1:
            for u in range(U_size):
                if v in edges[u]:
                    edge_cover.append((u, v))
                    break

    return edge_cover

U_size = 2
V_size = 3
edges = [[0, 1], [2]]
print("Минимальное покрытие:", min_edge_cover_bipartite(U_size, V_size, edges))