test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def sum_trailhead(grid):
    def get_valid(row, col):
        valid = set()
        val = grid[row][col]
        possible = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ]
        for p in possible:
            if p[0] >= 0 and p[0] < len(grid) and p[1] >= 0 and p[1] < len(grid[0]):
                if grid[p[0]][p[1]] - val == 1:
                    valid.add(p)

        return valid

    roots = set()
    graph = {}

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                roots.add((i, j))
            graph[(i, j)] = get_valid(i, j)

    def bfs(start):
        stack = [start]
        valid_paths = 0
        valid_endings = set()
        while len(stack):
            current = stack.pop()
            if grid[current[0]][current[1]] == 9:
                valid_endings.add(current)
                valid_paths += 1
            for n in graph[current]:
                stack.append(n)
        return len(valid_endings), valid_paths

    total_scores, total_ratings = 0, 0
    for r in roots:
        sum_scores, sum_ratings = bfs(r)
        total_scores += sum_scores
        total_ratings += sum_ratings

    return total_scores, total_ratings


def test():
    grid = []
    for line in test_input.split("\n"):
        grid.append([int(i) for i in list(line)])

    scores, ratings = sum_trailhead(grid)
    assert scores == 36
    assert ratings == 81


def solve():
    grid = []
    with open("input") as f:
        for line in f:
            grid.append([int(i) for i in list(line.strip())])

    scores, ratings = sum_trailhead(grid)
    print(f"part 1: {scores}")
    print(f"part 2: {ratings}")


test()
solve()
