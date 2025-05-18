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

graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]
source, sink = 0, 5
print(edmonds_karp(graph, source, sink))