from collections import deque


def bfs(graph, start, goal=None):
    visited = {start}
    queue = deque([start])
    parent = {start: None}
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        if node == goal:
            break
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = node
                queue.append(neighbour)

    path = None
    if goal is not None and goal in parent:
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path.reverse()
    return order, path


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}
order, path = bfs(graph, "A", "F")
print("BFS traversal order:", " -> ".join(order))
print("Shortest path A to F:", " -> ".join(path))
