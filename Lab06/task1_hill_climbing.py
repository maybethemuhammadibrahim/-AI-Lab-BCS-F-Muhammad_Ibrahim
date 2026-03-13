import random

def f(x):
    return -x * x + 6 * x

def hill_climb():
    x = random.randint(0, 6)
    print("start x:", x, "f(x):", f(x))
    while True:
        neighbors = []
        if x - 1 >= 0:
            neighbors.append(x - 1)
        if x + 1 <= 6:
            neighbors.append(x + 1)
        if not neighbors:
            break
        best = max(neighbors, key=lambda n: f(n))
        if f(best) <= f(x):
            break
        x = best
        print("move to x:", x, "f(x):", f(x))
    print("final x:", x, "f(x):", f(x))

hill_climb()