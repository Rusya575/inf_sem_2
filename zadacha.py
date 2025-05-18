def ans(n, edges):
    dist = [float('inf')] * (n + 1)
    dist[0] = 1.0

    for _ in range(20):
        updated = False
        for (u, v, rate) in edges:
            new_val = dist[u] * rate
            if new_val > dist[v]:
                dist[v] = new_val
                updated = True
        if not updated:
            break

    final_rub = dist[0]
    for (u, v, rate) in edges:
        if u == 0 and dist[v] * rate > final_rub:
            return True
    return False

edges = [
    (0, 1, 2.0),
    (1, 2, 2.0),
    (2, 0, 4.0)
]
print(ans(2, edges))