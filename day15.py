test_input = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""


def gps_coordinates(g, s):
    move = {">": (0, 1), "^": (-1, 0), "v": (1, 0), "<": (0, -1)}
    n, m = len(g), len(g[0])
    cur_r, cur_c = 0, 0

    for i in range(n):
        for j in range(m):
            if g[i][j] == "@":
                cur_r, cur_c = i, j

    for i in range(len(s)):
        diff_r, diff_c = move[s[i]]
        next_r, next_c = cur_r + diff_r, cur_c + diff_c
        if g[next_r][next_c] == ".":
            g[cur_r][cur_c] = "."
            cur_r, cur_c = next_r, next_c
        elif g[next_r][next_c] == "O":
            tmp_r, tmp_c = next_r, next_c
            while g[tmp_r][tmp_c] == "O":
                tmp_r, tmp_c = tmp_r + diff_r, tmp_c + diff_c
            if g[tmp_r][tmp_c] == ".":
                g[next_r][next_c] = "."
                g[tmp_r][tmp_c] = "O"
                g[cur_r][cur_c] = "."
                cur_r, cur_c = next_r, next_c
        g[cur_r][cur_c] = "@"

    sum = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == "O":
                sum += (100 * i) + j

    return sum


def gps_coordinates_part_2(g, s):
    move = {">": (0, 1), "^": (-1, 0), "v": (1, 0), "<": (0, -1)}
    match = {"[": "]", "]": "["}
    n, m = len(g), len(g[0])
    cur_r, cur_c = 0, 0

    for i in range(n):
        for j in range(m):
            if g[i][j] == "@":
                cur_r, cur_c = i, j

    for i in range(len(s)):
        diff_r, diff_c = move[s[i]]
        next_r, next_c = cur_r + diff_r, cur_c + diff_c
        if g[next_r][next_c] == ".":
            g[cur_r][cur_c] = "."
            cur_r, cur_c = next_r, next_c
        elif g[next_r][next_c] in "[]":
            if s[i] in "<>":
                tmp_r, tmp_c = next_r, next_c
                while g[tmp_r][tmp_c] in "[]":
                    tmp_r, tmp_c = tmp_r + diff_r, tmp_c + diff_c
                if g[tmp_r][tmp_c] == ".":
                    g[tmp_r][tmp_c] = g[next_r][next_c]
                    g[next_r][next_c] = "."
                    tmp2_r, tmp2_c = next_r + diff_r, next_c + diff_c
                    while (tmp2_r, tmp2_c) != (tmp_r, tmp_c):
                        g[tmp2_r][tmp2_c] = match[g[tmp2_r][tmp2_c]]
                        tmp2_r, tmp2_c = tmp2_r + diff_r, tmp2_c + diff_c
                    g[tmp_r][tmp_c] = match[g[tmp_r][tmp_c]]
                    g[cur_r][cur_c] = "."
                    cur_r, cur_c = next_r, next_c
            else:
                visited = set()
                to_move = []
                stack = [(next_r, next_c)]
                should_move = True
                while len(stack) > 0:
                    tmp_r, tmp_c = stack.pop(0)
                    if (tmp_r, tmp_c) in visited:
                        continue
                    visited.add((tmp_r, tmp_c))
                    if g[tmp_r][tmp_c] == "#":
                        should_move = False
                        break
                    elif g[tmp_r][tmp_c] == ".":
                        continue
                    elif g[tmp_r][tmp_c] == "]":
                        to_move.insert(0, (tmp_r, tmp_c))
                        pair = (tmp_r, tmp_c - 1)
                        if pair not in visited:
                            stack.append(pair)
                    elif g[tmp_r][tmp_c] == "[":
                        to_move.insert(0, (tmp_r, tmp_c))
                        pair = (tmp_r, tmp_c + 1)
                        if pair not in visited:
                            stack.append(pair)

                    tmp2_r, tmp2_c = tmp_r + diff_r, tmp_c + diff_c
                    to_add = (tmp2_r, tmp2_c)
                    if to_add not in visited:
                        stack.append(to_add)
                if should_move:
                    for idx in range(len(to_move)):
                        to_move_r, to_move_c = to_move[idx]
                        tmp2_r, tmp2_c = to_move_r + diff_r, to_move_c + diff_c
                        g[tmp2_r][tmp2_c] = g[to_move_r][to_move_c]
                        g[to_move_r][to_move_c] = "."
                    g[cur_r][cur_c] = "."
                    cur_r, cur_c = next_r, next_c

        g[cur_r][cur_c] = "@"

    sum = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == "[":
                sum += (100 * i) + j

    return sum


def test():
    grid = []
    grid2 = []
    moves = []
    parse_moves = False
    for line in test_input.split("\n"):
        line = line.strip()
        if line == "":
            parse_moves = True
            continue
        if parse_moves:
            moves += list(line)
        else:
            new_line = ""
            for c in line:
                if c == "#":
                    new_line += "##"
                elif c == "O":
                    new_line += "[]"
                elif c == ".":
                    new_line += ".."
                elif c == "@":
                    new_line += "@."

            grid.append(list(line))
            grid2.append(list(new_line))

    assert gps_coordinates(grid, moves) == 10092
    assert gps_coordinates_part_2(grid2, moves) == 9021


def solve():
    grid2 = []
    grid = []
    moves = []
    parse_moves = False
    with open("inputs/day15") as f:
        for line in f:
            line = line.strip()
            if line == "":
                parse_moves = True
                continue
            if parse_moves:
                moves += list(line)
            else:
                new_line = ""
                for c in line:
                    if c == "#":
                        new_line += "##"
                    elif c == "O":
                        new_line += "[]"
                    elif c == ".":
                        new_line += ".."
                    elif c == "@":
                        new_line += "@."
                grid.append(list(line))
                grid2.append(list(new_line))

    print(f"part 1: {gps_coordinates(grid, moves)}")
    print(f"part 2: {gps_coordinates_part_2(grid2, moves)}")


test()
solve()
