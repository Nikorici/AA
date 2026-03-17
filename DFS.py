def dfs(graph, start):
    visited = set()
    order   = []
    ops     = 0

    def _dfs(node):
        nonlocal ops
        visited.add(node)
        order.append(node)
        for neighbor in graph.adj[node]:
            ops += 1
            if neighbor not in visited:
                _dfs(neighbor)

    _dfs(start)
    return order, ops
