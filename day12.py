from collections import defaultdict

test_input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


def find_area(g):
    visited = set()
    n, m = len(g), len(g[0])
    id = 0
    regions = defaultdict(set)

    def neighbors(i, j):
        possible = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        return [
            p for p in possible if p[0] >= 0 and p[0] < n and p[1] >= 0 and p[1] < m
        ]

    def edges_for_perimeter(i, j):
        possible = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        return [
            (p[0], p[1])
            for p in possible
            if p[0] < 0
            or p[0] >= n
            or p[1] < 0
            or p[1] >= m
            or g[p[0]][p[1]] != g[i][j]
        ]

    def edges_for_sides(i, j):
        possible = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        filtered = []
        for p in possible:
            if (
                p[0] < 0
                or p[0] >= n
                or p[1] < 0
                or p[1] >= m
                or g[p[0]][p[1]] != g[i][j]
            ):
                if p[0] < i:
                    filtered.append((i, j, "UP"))
                elif p[0] > i:
                    filtered.append((i, j, "DOWN"))
                elif p[1] > j:
                    filtered.append((i, j, "RIGHT"))
                elif p[1] < j:
                    filtered.append((i, j, "LEFT"))
        return filtered

    def edge_neighbors(i, j, dir):
        if dir == "UP" or dir == "DOWN":
            possible = [(i, j - 1, dir), (i, j + 1, dir)]
            return [p for p in possible if p[1] >= 0 and p[1] < m]
        elif dir == "LEFT" or dir == "RIGHT":
            possible = [(i - 1, j, dir), (i + 1, j, dir)]
            return [p for p in possible if p[0] >= 0 and p[0] < n]
        return []

    def all_sides(nodes):
        edge_list = set()
        visited = set()
        sides = 0
        for i, j in nodes:
            edge_list.update(edges_for_sides(i, j))

        while len(edge_list) > 0:
            i, j, dir = edge_list.pop()
            if (i, j, dir) in visited:
                continue

            # explore this node
            stack = [(i, j, dir)]
            while len(stack) > 0:
                curr_i, curr_j, curr_dir = stack.pop()
                visited.add((curr_i, curr_j, curr_dir))
                possible = edge_neighbors(curr_i, curr_j, curr_dir)
                for p in possible:
                    if p in edge_list and p not in visited:
                        stack.append(p)
            sides += 1

        return sides

    def dfs(i, j):
        stack = [(i, j)]
        nodes = set()
        while len(stack) > 0:
            row, col = stack.pop()
            nodes.add((row, col))
            for n_i, n_j in neighbors(row, col):
                if g[row][col] == g[n_i][n_j] and (n_i, n_j) not in nodes:
                    stack.append((n_i, n_j))
        return nodes

    for i in range(n):
        for j in range(m):
            if (i, j) in visited:
                continue
            else:
                nodes = dfs(i, j)
                regions[id].update(nodes)
                visited.update(nodes)
                id += 1

    count = 0
    count2 = 0
    for _, nodes in regions.items():
        area = len(nodes)
        perimeter = sum([len(edges_for_perimeter(node[0], node[1])) for node in nodes])
        count += area * perimeter
        count2 += area * all_sides(nodes)

    return count, count2


def test():
    grid = []
    for line in test_input.split("\n"):
        grid.append(list(line.strip()))

    part1, part2 = find_area(grid)
    assert part1 == 1930
    assert part2 == 1206


def solve():
    grid = []
    with open("input") as f:
        for line in f:
            grid.append(list(line.strip()))

    part1, part2 = find_area(grid)
    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


test()
solve()
