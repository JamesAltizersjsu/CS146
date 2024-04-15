import heapq
from typing import List

def minCostToSupplyWater(n: int, wells: List[int], pipes: List[List[int]]) -> int:
    edges = []
    well_costs = [0] + wells
    for i in range(n):
        edges.append([0, i + 1, wells[i]])
    for pipe in pipes:
        edges.append(pipe)
    edges.sort(key=lambda x: x[2])

    parent = list(range(n + 1))

    total_cost = 0
    for _, u, v, cost in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)
        if root_u != root_v:
            parent[root_u] = root_v
            total_cost += cost

    return total_cost

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
