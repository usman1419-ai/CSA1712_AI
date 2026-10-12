def dfs_recursive(graph, node, visited=None, order=None):
    if visited is None:
        visited, order = set(), []
    visited.add(node)
    order.append(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited, order)
    return order


def dfs_iterative(graph, start):
    visited, order, stack = set(), [], [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)
    return order


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}
print("DFS (recursive):", " -> ".join(dfs_recursive(graph, "A")))
print("DFS (iterative):", " -> ".join(dfs_iterative(graph, "A")))
