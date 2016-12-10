def arb(s):
    for x in s:
        return x

def find_path(start, goal, R):
    paths = { (start,) }
    states = { start }
    explored = set()
    while states != explored:
        explored = set(states)
        paths = { l for l in path_product(paths, R) if l[-1] not in states }
        paths = clean(paths)
        states |= { l[-1] for l in paths }
        if goal in states:
            return arb({ l for l in paths if l[-1] == goal })

def path_product(p, q):
    return { x + (y[1],) for x in p for y in q if x[-1] == y[0] }

def clean(paths):
    states = { k[-1] for k in paths }
    return { arb({ k for k in paths if k[-1] == s }) for s in states }

def print_state(a, b):
    print("A (max 5l):", a, "; B (max 3l):", b)

def print_path(path):
    print("Solution:\n")
    for (a, b) in path:
        print_state(a, b)

P = { (a, b) for a in range(0, 6) for b in range(0, 4) }
R = {
    ((a1, b1), (a2, b2)) for (a1, b1) in P for (a2, b2) in P if
    (a2 in { 0, 5, a1 } and b2 in { 0, 3, b1 }) or
    (a1 + b1 == a2 + b2 and (a2 in { 5, 0 } or b2 in { 3, 0 }))
}

start = (0, 0)
goal = (4, 0)

path = find_path(start, goal, R)

if path is not None:
    print("Anzahl der Schritte:", len(path) - 1)
    print_path(path)
else:
    print("No solution found")