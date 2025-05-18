def has_eulerian_path(graph):

    in_degree = {node: 0 for node in graph}
    out_degree = {node: 0 for node in graph}
    for u in graph:
        for v in graph[u]:
            out_degree[u] += 1
            in_degree[v] = in_degree.get(v, 0) + 1

    start_node = None
    end_node = None
    for node in graph:
        diff = out_degree[node] - in_degree.get(node, 0)
        if diff == 1:
            if start_node is not None: return False, None
            start_node = node
        elif diff == -1:
            if end_node is not None: return False, None
            end_node = node
        elif diff != 0:
            return False, None

    if start_node is None:
        start_node = list(graph.keys())[0]
    return True, start_node

def find_eulerian_path(graph):
    valid, start_node = has_eulerian_path(graph)
    if not valid:
        return None

    stack = [start_node]
    path = []
    temp_graph = {u: list(v) for u, v in graph.items()}

    while stack:
        current = stack[-1]
        if temp_graph.get(current, []):
            next_node = temp_graph[current].pop()
            stack.append(next_node)
        else:
            path.append(stack.pop())
    return path[::-1]

graph = {
    0: [1],
    1: [2],
    2: [0]
}
print(has_eulerian_path(graph))