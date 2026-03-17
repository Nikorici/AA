from collections import defaultdict, deque
import random
import time

# ── Graph class ───────────────────────────────────────────────────────────────
class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    @staticmethod
    def random_graph(n, p=0.1):
        g = Graph(n)
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < p:
                    g.add_edge(i, j)
        return g

# ── Algorithms ────────────────────────────────────────────────────────────────
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

    import sys
    sys.setrecursionlimit(100000)
    _dfs(start)
    return order, ops

# ── Benchmark ─────────────────────────────────────────────────────────────────
SIZES      = [100, 500, 1000, 2000, 5000]
DENSITIES  = [("sparse", 0.05), ("medium", 0.15), ("dense", 0.30)]
RUNS       = 5

print(f"{'Density':<10} {'n':>6} {'Edges':>10} {'BFS Ops':>12} {'DFS Ops':>12} {'BFS Time':>12} {'DFS Time':>12}")
print("-" * 80)

for label, p in DENSITIES:
    for n in SIZES:
        bfs_times, dfs_times = [], []
        bfs_ops_total, dfs_ops_total = 0, 0

        for _ in range(RUNS):
            g = Graph.random_graph(n, p)
            edges = sum(len(v) for v in g.adj.values()) // 2

            t0 = time.perf_counter()
            _, b_ops = bfs(g, 0)
            bfs_times.append(time.perf_counter() - t0)
            bfs_ops_total += b_ops

            t0 = time.perf_counter()
            _, d_ops = dfs(g, 0)
            dfs_times.append(time.perf_counter() - t0)
            dfs_ops_total += d_ops

        avg_bfs_time = sum(bfs_times) / RUNS
        avg_dfs_time = sum(dfs_times) / RUNS
        avg_bfs_ops  = bfs_ops_total  // RUNS
        avg_dfs_ops  = dfs_ops_total  // RUNS

        print(f"{label:<10} {n:>6} {edges:>10,} {avg_bfs_ops:>12,} {avg_dfs_ops:>12,} {avg_bfs_time:>12.6f} {avg_dfs_time:>12.6f}")
    print()