def bfs(graph, start):
    visited = set([start])
    queue   = deque([start])
    order   = []
    ops     = 0
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.adj[node]:
            ops += 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order, ops