def arb(m):
    for i in m:
        return i

def state_to_str(state):
    indent = ' ' * 4
    line = indent + '+-+-+-\n'
    result = '\n' + line
    for row in range(0, 3):
        result += indent + '|'
        for col in range(0, 3):
            cell = state[row][col]
            if cell > 0:
                result += str(cell)
            else:
                result += ' '
            result += '|'
        result += '\n'
        result += line
    return result

def find_path(start, goal, next_states):
    count = 1
    paths = {(start,)}
    states = {start}
    explored = set()
    while states != explored:
        print("Iteration number:", count)
        count += 1
        explored = states.copy()
        paths = {l + (s,) for l in paths for s in next_states(l[-1]) if s not in states}
        states |= {p[-1] for p in paths}
        print("Number of states:", len(states))
        if goal in states:
            for l in paths:
                if l[-1] == goal:
                    return l

def find_space(state):
    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] == 0:
                return i, j

def find_neighbors(state, coords):
    i, j = coords
    return {
        (k, l) for k in range(0, 3) for l in range(0, 3) if
        k in range(i - 1, i + 2) and l in range(j - 1, j + 2) and
        (k == i or l != j) and (l == j or k != i)
    }

def next_states(state):
    i, j = find_space(state)
    neighbors = find_neighbors(state, (i, j))
    return {
        tuple(tuple(
            state[k][l] if (a, b) == (i, j) else
            state[i][j] if (a, b) == (k, l) else
            state[a][b]
        for b in range(0, 3)) for a in range(0, 3))
    for k, l in neighbors}

start = (
    (8, 0, 6),
    (5, 4, 7),
    (2, 3, 1)
)
goal = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8)
)

path = find_path(start, goal, next_states)
if path is not None:
    print("Number of steps to solve the puzzle:", len(path) - 1)
    for state in path:
        print(state_to_str(state))
else:
    print("No solution found")