import random


def reflex_vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    return "Right" if location == "A" else "Left"


def run(steps=8):
    world = {"A": random.choice(["Clean", "Dirty"]),
             "B": random.choice(["Clean", "Dirty"])}
    location = random.choice(["A", "B"])
    print("Initial state:", world, "| Vacuum at", location)
    print("-" * 50)

    for step in range(1, steps + 1):
        action = reflex_vacuum_agent(location, world[location])
        print(f"Step {step}: at {location} ({world[location]}) -> {action}")
        if action == "Suck":
            world[location] = "Clean"
        elif action == "Right":
            location = "B"
        elif action == "Left":
            location = "A"
        if all(s == "Clean" for s in world.values()):
            print("Both rooms are clean. State:", world)
            break
    print("Final state:", world, "| Vacuum at", location)


run()
