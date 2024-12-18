# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "numpy",
# ]
# ///
import numpy as np

test_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def safety_factor(p, v, secs, n, m):
    result = (p + v * secs) % np.array([m, n])
    mid_x = m // 2
    mid_y = n // 2
    quadrants = [0, 0, 0, 0]
    for x, y in result:
        if x > mid_x and y < mid_y:
            quadrants[0] += 1
        elif x < mid_x and y < mid_y:
            quadrants[1] += 1
        elif x < mid_x and y > mid_y:
            quadrants[2] += 1
        elif x > mid_x and y > mid_y:
            quadrants[3] += 1

    return np.multiply.reduce(quadrants)


def test():
    p = []
    v = []
    for line in test_input.split("\n"):
        line = line.strip()
        p_x = int(line.split()[0].split("=")[1].split(",")[0])
        p_y = int(line.split()[0].split("=")[1].split(",")[1])
        v_x = int(line.split()[1].split("=")[1].split(",")[0])
        v_y = int(line.split()[1].split("=")[1].split(",")[1])
        p.append([p_x, p_y])
        v.append([v_x, v_y])

    assert safety_factor(np.array(p), np.array(v), 100, 7, 11) == 12


def solve():
    p = []
    v = []
    with open("input") as f:
        for line in f:
            line = line.strip()
            p_x = int(line.split()[0].split("=")[1].split(",")[0])
            p_y = int(line.split()[0].split("=")[1].split(",")[1])
            v_x = int(line.split()[1].split("=")[1].split(",")[0])
            v_y = int(line.split()[1].split("=")[1].split(",")[1])
            p.append([p_x, p_y])
            v.append([v_x, v_y])

    print(f"part 1: {safety_factor(np.array(p), np.array(v), 100, 103, 101)}")


test()
solve()
