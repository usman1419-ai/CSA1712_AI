from itertools import permutations


def tour_cost(tour, dist):
    cost = sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return cost + dist[tour[-1]][tour[0]]


def tsp_brute_force(dist, start=0):
    cities = [c for c in range(len(dist)) if c != start]
    best_cost, best_tour = float("inf"), None
    for perm in permutations(cities):
        tour = [start] + list(perm)
        cost = tour_cost(tour, dist)
        if cost < best_cost:
            best_cost, best_tour = cost, tour
    return best_tour + [start], best_cost


def tsp_nearest_neighbour(dist, start=0):
    n = len(dist)
    unvisited = set(range(n)) - {start}
    tour = [start]
    while unvisited:
        nxt = min(unvisited, key=lambda c: dist[tour[-1]][c])
        tour.append(nxt)
        unvisited.remove(nxt)
    return tour + [start], tour_cost(tour, dist)


names = ["A", "B", "C", "D"]
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]
tour, cost = tsp_brute_force(dist)
print("Optimal tour (brute force):", " -> ".join(names[i] for i in tour))
print("Cost:", cost)
tour, cost = tsp_nearest_neighbour(dist)
print("Nearest neighbour tour    :", " -> ".join(names[i] for i in tour))
print("Cost:", cost)
