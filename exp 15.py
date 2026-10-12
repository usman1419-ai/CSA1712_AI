import math
from collections import Counter


def entropy(rows):
    counts = Counter(r[-1] for r in rows)
    total = len(rows)
    return -sum((c / total) * math.log2(c / total) for c in counts.values())


def information_gain(rows, col):
    total = len(rows)
    remainder = 0.0
    for value in set(r[col] for r in rows):
        subset = [r for r in rows if r[col] == value]
        remainder += len(subset) / total * entropy(subset)
    return entropy(rows) - remainder


def build_tree(rows, attrs):
    labels = [r[-1] for r in rows]
    if len(set(labels)) == 1:
        return labels[0]
    if not attrs:
        return Counter(labels).most_common(1)[0][0]

    best = max(attrs, key=lambda a: information_gain(rows, a))
    tree = {best: {}}
    remaining = [a for a in attrs if a != best]
    for value in set(r[best] for r in rows):
        subset = [r for r in rows if r[best] == value]
        tree[best][value] = build_tree(subset, remaining)
    return tree


def predict(tree, sample):
    while isinstance(tree, dict):
        attr = next(iter(tree))
        tree = tree[attr][sample[attr]]
    return tree


def print_tree(tree, names, indent=""):
    if not isinstance(tree, dict):
        print(indent + "->", tree)
        return
    attr = next(iter(tree))
    for value, subtree in tree[attr].items():
        print(f"{indent}[{names[attr]} = {value}]")
        print_tree(subtree, names, indent + "    ")


names = ["Outlook", "Temperature", "Humidity", "Wind", "PlayTennis"]
data = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny", "Mild", "High", "Weak", "No"],
    ["Sunny", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "Normal", "Weak", "Yes"],
    ["Sunny", "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High", "Strong", "Yes"],
    ["Overcast", "Hot", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Strong", "No"],
]

print("Information gain of each attribute:")
for i in range(4):
    print(f"  {names[i]:12s}: {information_gain(data, i):.3f}")

tree = build_tree(data, [0, 1, 2, 3])
print("\nDecision tree:")
print_tree(tree, names)

sample = ["Sunny", "Cool", "High", "Strong"]
print("\nNew sample:", dict(zip(names, sample)))
print("Prediction (PlayTennis):", predict(tree, sample))
