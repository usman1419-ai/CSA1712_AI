import heapq


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = [(heuristic(start, goal), 0, start)]  # (f, g, node)
    g_cost = {start: 0}
    parent = {start: None}
    closed = set()

    while open_list:
        f, g, current = heapq.heappop(open_list)
        if current in closed:
            continue
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], g
        closed.add(current)

        r, c = current
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                new_g = g + 1
                if new_g < g_cost.get((nr, nc), float("inf")):
                    g_cost[(nr, nc)] = new_g
                    parent[(nr, nc)] = current
                    heapq.heappush(
                        open_list, (new_g + heuristic((nr, nc), goal), new_g, (nr, nc)))
    return None, float("inf")


grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]
start, goal = (0, 0), (4, 4)
path, cost = a_star(grid, start, goal)
print("Path found:", path)
print("Path cost :", cost)

display = [["#" if cell else "." for cell in row] for row in grid]
for r, c in path:
    display[r][c] = "*"
display[start[0]][start[1]], display[goal[0]][goal[1]] = "S", "G"
print()
for row in display:
    print(" ".join(row))
    
