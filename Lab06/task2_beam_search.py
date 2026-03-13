def next_states(n):
    return [n + 2, n + 3, n * 2]

def beam_search(start, goal, k):
    beam = [(abs(goal - start), [start])]
    level = 0
    while beam:
        level += 1
        candidates = []
        explored = []
        for cost, path in beam:
            current = path[-1]
            if current == goal:
                return path
            for nxt in next_states(current):
                new_path = path + [nxt]
                h = abs(goal - nxt)
                candidates.append((h, new_path))
                explored.append(nxt)
        print("level", level, "explored:", explored)
        if not candidates:
            break
        candidates.sort(key=lambda x: x[0])
        beam = candidates[:k]
    return None

path = beam_search(1, 20, 2)
if path:
    print("path to 20:", path)
else:
    print("no path")