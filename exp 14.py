INF = float("inf")
counts = {"minimax": 0, "alphabeta": 0}


def minimax(node, is_max):
    counts["minimax"] += 1
    if not isinstance(node, list):
        return node
    values = [minimax(c, not is_max) for c in node]
    return max(values) if is_max else min(values)


def alpha_beta(node, is_max, alpha=-INF, beta=INF, depth=0):
    counts["alphabeta"] += 1
    if not isinstance(node, list):
        return node

    if is_max:
        value = -INF
        for child in node:
            value = max(value, alpha_beta(child, False, alpha, beta, depth + 1))
            alpha = max(alpha, value)
            if alpha >= beta:
                print(f"{'  ' * depth}Pruned at MAX node (alpha={alpha}, beta={beta})")
                break
        return value

    value = INF
    for child in node:
        value = min(value, alpha_beta(child, True, alpha, beta, depth + 1))
        beta = min(beta, value)
        if alpha >= beta:
            print(f"{'  ' * depth}Pruned at MIN node (alpha={alpha}, beta={beta})")
            break
    return value


tree = [[[3, 5], [6, 9]],
        [[1, 2], [0, -1]]]

print("Alpha-Beta search:")
ab = alpha_beta(tree, True)
mm = minimax(tree, True)
print()
print("Alpha-Beta value:", ab, "| nodes visited:", counts["alphabeta"])
print("Minimax value   :", mm, "| nodes visited:", counts["minimax"])
print("Same result     :", ab == mm)
