test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def count(grid, row, col):
    move = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    n = len(grid)
    m = len(grid[0])
    visited = set()
    dir = 0
    if grid[row][col] == "#":
        return visited
    while True:
        visited.add((row, col))

        next_row, next_col = row + move[dir][0], col + move[dir][1]

        if next_row >= n or next_row < 0 or next_col < 0 or next_col >= m:
            break

        if grid[next_row][next_col] == "#":
            dir = (dir + 1) % 4
        else:
            row, col = next_row, next_col

    return visited


def is_loop(grid, row, col):
    move = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    n = len(grid)
    m = len(grid[0])
    seen = set()
    dir = 0
    if grid[row][col] == "#":
        return False

    while True:
        if (row, col, dir) in seen:
            return True
        seen.add((row, col, dir))
        next_row, next_col = row + move[dir][0], col + move[dir][1]
        if next_row >= n or next_row < 0 or next_col < 0 or next_col >= m:
            return False
        if grid[next_row][next_col] == "#":
            dir = (dir + 1) % 4
        else:
            row, col = next_row, next_col


def num_obstacles(grid, row, col):
    visited = count(grid, row, col)
    count_obstacles = 0
    for v_i, v_j in visited:
        if v_i == row and v_j == col:
            continue
        grid[v_i][v_j] = "#"
        count_obstacles += is_loop(grid, row, col)
        grid[v_i][v_j] = "."

    return count_obstacles


def test():
    test_grid = []
    for row in test_input.split("\n"):
        test_grid.append(list(row))

    row, col = 0, 0
    n, m = len(test_grid), len(test_grid[0])
    for i in range(n):
        for j in range(m):
            if test_grid[i][j] == "^":
                row = i
                col = j

    assert len(count(test_grid, row, col)) == 41
    assert num_obstacles(test_grid, row, col) == 6


def solve():
    grid = []
    with open("input") as f:
        for line in f:
            grid.append(list(line.strip()))
    row, col = 0, 0
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "^":
                row = i
                col = j
    print(f"part 1: {len(count(grid, row, col))}")
    print(f"part 2: {num_obstacles(grid, row, col)}")


test()
solve()
