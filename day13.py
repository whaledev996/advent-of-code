# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "numpy",
# ]
# ///
import numpy as np

test_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def min_tokens(machines):
    token_sum = 0
    for a, b, prize in machines:
        a_x, a_y = a
        b_x, b_y = b
        prize_x, prize_y = prize

        vars = np.array([[a_x, b_x], [a_y, b_y]])
        prize_arr = np.array([prize_x, prize_y])

        if np.linalg.det(vars) == 0:
            continue

        soln = np.linalg.solve(vars, prize_arr)
        a, b = soln
        a, b = round(a), round(b)
        if (a * a_x) + (b * b_x) == prize_x and (a * a_y) + (b * b_y) == prize_y:
            token_sum += (3 * a) + b

    return token_sum


def test():
    machines = [
        [(94, 34), (22, 67), (8400, 5400)],
        [(26, 66), (67, 21), (12748, 12176)],
        [(17, 86), (84, 37), (7870, 6450)],
        [(69, 23), (27, 71), (18641, 10279)],
    ]
    assert min_tokens(machines) == 480


def solve():
    machines = []
    machines2 = []
    with open("input") as f:
        machine = []
        machine2 = []
        for line in f:
            line = line.strip()
            if line != "":
                category = line.split(":")[0]
                operators = line.split(":")[1].split(",")
                if category == "Prize":
                    machine.append(
                        (
                            int(operators[0].split("X=")[1]),
                            int(operators[1].split("Y=")[1]),
                        )
                    )
                    machine2.append(
                        (
                            machine[-1][0] + 10000000000000,
                            machine[-1][1] + 10000000000000,
                        )
                    )
                else:
                    machine.append(
                        (
                            int(operators[0].split("X+")[1]),
                            int(operators[1].split("Y+")[1]),
                        )
                    )
                    machine2.append(machine[-1])
                if len(machine) == 3:
                    machines.append(machine)
                    machines2.append(machine2)
                    machine = []
                    machine2 = []

    print(f"part 1: {min_tokens(machines)}")
    print(f"part 2: {min_tokens(machines2)}")


test()
solve()
