node_count = 0


def minimax(node, is_max):
    global node_count
    node_count += 1
    if not isinstance(node, list):  # leaf
        return node
    values = [minimax(child, not is_max) for child in node]
    return max(values) if is_max else min(values)


def best_move(tree):
    values = [minimax(child, False) for child in tree]
    return values.index(max(values)), values


tree = [[3, 5], [2, 9], [0, 7]]
value = minimax(tree, True)
print("Minimax value at root:", value)
print("Nodes evaluated      :", node_count)
move, values = best_move(tree)
print("Child values (MIN nodes):", values)
print("Best move for MAX: branch", move + 1)

node_count = 0
deep = [[[3, 5], [6, 9]], [[1, 2], [0, -1]]]
print("\nDeeper tree value:", minimax(deep, True))
print("Nodes evaluated  :", node_count)
