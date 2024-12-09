test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def can_solve(result, operands):
    if len(operands) == 1:
        return result == operands[0]
    elif operands[0] >= result:
        return False
    else:
        sum = operands[0] + operands[1]
        product = operands[0] * operands[1]
        return can_solve(result, [sum] + operands[2:]) or can_solve(
            result, [product] + operands[2:]
        )


def can_solve_part_2(result, operands):
    if len(operands) == 1:
        return result == operands[0]
    elif operands[0] >= result:
        return False
    else:
        sum = operands[0] + operands[1]
        product = operands[0] * operands[1]
        concatenation = int(str(operands[0]) + str(operands[1]))
        return (
            can_solve_part_2(result, [sum] + operands[2:])
            or can_solve_part_2(result, [product] + operands[2:])
            or can_solve_part_2(result, [concatenation] + operands[2:])
        )


def test():
    solvable = []
    solvable2 = []
    for line in test_input.split("\n"):
        line = line.strip()
        result, operands = int(line.split(":")[0]), [
            int(i) for i in line.split(":")[1].split()
        ]
        if can_solve(result, operands):
            solvable.append(result)
        if can_solve_part_2(result, operands):
            solvable2.append(result)

    assert sum(solvable) == 3749
    assert sum(solvable2) == 11387


def solve():
    solvable = []
    solvable2 = []
    with open("input") as f:
        for line in f:
            result, operands = int(line.split(":")[0]), [
                int(i) for i in line.split(":")[1].split()
            ]
            if can_solve(result, operands):
                solvable.append(result)
            if can_solve_part_2(result, operands):
                solvable2.append(result)

    print(f"part 1: {sum(solvable)}")
    print(f"part 2: {sum(solvable2)}")


test()
solve()
