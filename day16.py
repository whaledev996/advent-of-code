import math
from collections import defaultdict
import heapq

test_input = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""


def paths(g):
    n, m = len(g), len(g[0])
    cur_r, cur_c = 0, 0
    end_r, end_c = 0, 0

    # 0 - north, 1 - east, 2 - south, 3 - west
    dir = 1
    move = {1: (0, 1), 2: (1, 0), 3: (0, -1), 0: (-1, 0)}
    for i in range(n):
        for j in range(m):
            if g[i][j] == "S":
                cur_r, cur_c = i, j
            if g[i][j] == "E":
                end_r, end_c = i, j

    def in_bounds(i, j):
        return i >= 0 and i < n and j >= 0 and j < m

    def compute_shortest(row, col, dir):
        dist = defaultdict(lambda: math.inf)
        h = []
        heapq.heappush(h, (0, (row, col, dir)))
        dist[(row, col)] = 0
        visited = set()
        while len(h) > 0:
            p, item = heapq.heappop(h)
            i, j, dir = item
            if (i, j) in visited:
                continue
            visited.add((i, j))
            dir2 = (dir - 1) % 4
            dir3 = (dir + 1) % 4

            s1_i, s1_j = i + move[dir][0], j + move[dir][1]
            s2_i, s2_j = i + move[dir2][0], j + move[dir2][1]
            s3_i, s3_j = i + move[dir3][0], j + move[dir3][1]

            # relax neighbors
            if dist[(i, j)] + 1 < dist[(s1_i, s1_j)]:
                dist[(s1_i, s1_j)] = dist[(i, j)] + 1

            if dist[(i, j)] + 1001 < dist[(s2_i, s2_j)]:
                dist[(s2_i, s2_j)] = dist[(i, j)] + 1001

            if dist[(i, j)] + 1001 < dist[(s3_i, s3_j)]:
                dist[(s3_i, s3_j)] = dist[(i, j)] + 1001

            if in_bounds(s1_i, s1_j) and g[s1_i][s1_j] == ".":
                heapq.heappush(h, (dist[(s1_i, s1_j)], (s1_i, s1_j, dir)))
            if in_bounds(s2_i, s2_j) and g[s2_i][s2_j] == ".":
                heapq.heappush(h, (dist[(s2_i, s2_j)], (s2_i, s2_j, dir2)))
            if in_bounds(s3_i, s3_j) and g[s3_i][s3_j] == ".":
                heapq.heappush(h, (dist[(s3_i, s3_j)], (s3_i, s3_j, dir3)))

        return dist

    stack = [(end_r, end_c)]
    visited2 = set()
    other = []
    dist = compute_shortest(cur_r, cur_c, dir)
    print(dist[(end_r + 1, end_c)])
    print(dist[(end_r, end_c - 1)])
    dist2 = compute_shortest(end_r, end_c, 2)

    while len(stack) > 0:
        row, col = stack.pop()
        if (row, col) in visited2:
            continue
        other.append((row, col))
        visited2.add((row, col))
        possible = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        possible = [
            p for p in possible if in_bounds(p[0], p[1]) and g[p[0]][p[1]] != "#"
        ]
        if len(possible):
            # min_dist = min([dist[p] for p in possible])
            for p in possible:
                if dist[p] + dist2[p] <= 95444:
                    stack.append(p)

    return dist[(end_r, end_c)], len(visited2)


def test():
    grid = []
    for line in test_input.split("\n"):
        line = line.strip()
        grid.append(list(line))

    min_dist, num_stones = paths(grid)
    print(num_stones)
    assert min_dist == 11048
    assert num_stones == 64


def solve():
    grid = []
    with open("inputs/day16") as f:
        for line in f:
            line = line.strip()
            grid.append(list(line))

    min_dist, num_stones = paths(grid)
    print(f"part 1: {min_dist}")
    print(f"part 2: {num_stones}")


# test()
solve()
