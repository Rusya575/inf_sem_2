def johnson(graph):
    n = len(graph)
    h = [0] * n

    for _ in range(n):
        for u in graph:
            for v in graph[u]:
                if h[v] > h[u] + graph[u][v]:
                    h[v] = h[u] + graph[u][v]

    new_graph = {u: {} for u in graph}
    for u in graph:
        for v in graph[u]:
            new_graph[u][v] = graph[u][v] + h[u] - h[v]

    shortest = {}
    for u in graph:
        dist = {v: float('inf') for v in graph}
        dist[u] = 0
        for _ in range(n-1):
            for curr in graph:
                for neighbor in graph[curr]:
                    if dist[neighbor] > dist[curr] + new_graph[curr][neighbor]:
                        dist[neighbor] = dist[curr] + new_graph[curr][neighbor]
        shortest[u] = dist
    return shortest

graph = {
    0: {1: -1, 2: 4},
    1: {2: 3, 3: 2},
    2: {},
    3: {2: 5}
}
print(johnson(graph))