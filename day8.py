from collections import defaultdict

test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def find_antinodes(grid):
    antennas = defaultdict(list)
    antinodes = set()

    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] != ".":
                antennas[grid[i][j]].append((i, j))

    for _, locs in antennas.items():
        if len(locs) > 1:
            for i in range(len(locs)):
                for j in range(i + 1, len(locs)):
                    x_dis = locs[j][0] - locs[i][0]
                    y_dis = locs[j][1] - locs[i][1]

                    possible = [
                        (locs[j][0] + x_dis, locs[j][1] + y_dis),
                        (locs[i][0] - x_dis, locs[i][1] - y_dis),
                    ]
                    for p in possible:
                        if p[0] >= 0 and p[0] < n and p[1] >= 0 and p[1] < m:
                            antinodes.add(p)

    return antinodes


def find_antinodes_part_2(grid):
    antennas = defaultdict(list)
    antinodes = set()

    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] != ".":
                antennas[grid[i][j]].append((i, j))

    for _, locs in antennas.items():
        if len(locs) > 1:
            for i in range(len(locs)):
                for j in range(i + 1, len(locs)):
                    x_dis = locs[j][0] - locs[i][0]
                    y_dis = locs[j][1] - locs[i][1]

                    p = (locs[j][0], locs[j][1])
                    while p[0] >= 0 and p[0] < n and p[1] >= 0 and p[1] < m:
                        antinodes.add(p)
                        p = (p[0] + x_dis, p[1] + y_dis)

                    p = (locs[i][0], locs[i][1])
                    while p[0] >= 0 and p[0] < n and p[1] >= 0 and p[1] < m:
                        antinodes.add(p)
                        p = (p[0] - x_dis, p[1] - y_dis)

    return antinodes


def test():
    grid = []
    for line in test_input.split("\n"):
        line = line.strip()
        grid.append(list(line))

    assert len(find_antinodes(grid)) == 14
    assert len(find_antinodes_part_2(grid)) == 34


def solve():
    grid = []
    with open("input") as f:
        for line in f:
            line = line.strip()
            grid.append(list(line))

    print(f"part 1: {len(find_antinodes(grid))}")
    print(f"part 2: {len(find_antinodes_part_2(grid))}")


test()
solve()
