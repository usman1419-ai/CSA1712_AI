def is_consistent(region, color, assignment, neighbors):
    return all(assignment.get(n) != color for n in neighbors[region])


def backtrack(assignment, regions, domains, neighbors):
    if len(assignment) == len(regions):
        return assignment

    region = next(r for r in regions if r not in assignment)
    for color in domains[region]:
        if is_consistent(region, color, assignment, neighbors):
            assignment[region] = color
            result = backtrack(assignment, regions, domains, neighbors)
            if result:
                return result
            del assignment[region]  # backtrack
    return None


regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": [],
}
colors = ["Red", "Green", "Blue"]
domains = {r: list(colors) for r in regions}

solution = backtrack({}, regions, domains, neighbors)
if solution:
    print("Colouring found:")
    for region in regions:
        print(f"  {region:4s} -> {solution[region]}")
    valid = all(solution[r] != solution[n] for r in regions for n in neighbors[r])
    print("Valid colouring:", valid)
else:
    print("No solution with", len(colors), "colours")
