def edmonds_karp(graph, source, sink):
    n = len(graph)
    max_flow = 0

    while True:
        parent = [-1] * n
        visited = [False] * n
        queue = [source]
        visited[source] = True

        found = False
        while queue:
            u = queue.pop(0)
            for v in range(n):
                if not visited[v] and graph[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        found = True
                        break
            if found:
                break

        if not found:
            break

        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow


def can_allocate_credits(a, b, edges):
    total_a = sum(a)
    total_b = sum(b)
    if total_a != total_b:
        return False

    m = len(a)
    n = len(b)
    size = m + n + 2
    graph = [[0] * size for _ in range(size)]
    source = 0
    sink = size - 1

    for i in range(m):
        graph[source][i + 1] = a[i]

    for j in range(n):
        graph[m + 1 + j][sink] = b[j]

    for i in range(m):
        for j in edges[i]:
            graph[i + 1][m + 1 + j] = float('inf')

    max_flow = edmonds_karp(graph, source, sink)
    return max_flow == total_a

a = [100, 200]
b = [150, 150]
edges = [[0, 1], [1]]
print("Кредиты возможны:", can_allocate_credits(a, b, edges))