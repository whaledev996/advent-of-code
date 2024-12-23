def solve(a, b, c, p):
    ip = 0
    reg = [a, b, c]

    def combo(op):
        if op <= 3:
            return op
        return reg[op - 4]

    output = []
    while ip < len(p) - 1:
        jmp = False
        op = p[ip + 1]
        if p[ip] == 0:
            reg[0] = reg[0] // (2 ** combo(op))
        elif p[ip] == 1:
            reg[1] = reg[1] ^ op
        elif p[ip] == 2:
            reg[1] = combo(op) % 8
        elif p[ip] == 3:
            if reg[0] != 0:
                ip = op
                jmp = True
        elif p[ip] == 4:
            reg[1] = reg[1] ^ reg[2]
        elif p[ip] == 5:
            output.append(combo(op) % 8)
        elif p[ip] == 6:
            reg[1] = reg[0] // (2 ** combo(op))
        elif p[ip] == 7:
            reg[2] = reg[0] // (2 ** combo(op))
        if not jmp:
            ip += 2
    return output


def solve2(p):
    n = int("".join(map(str, p)))
    count, result = 1, -1
    for i in range(1, len(p) + 1):
        while True:
            result = solve(count, 0, 0, p)
            result = int("".join(map(str, result)))
            if result == n % 10**i:
                break
            count += 1
        count *= 8
    return count


if __name__ == "__main__":
    a = int(input().split()[-1])
    b = int(input().split()[-1])
    c = int(input().split()[-1])
    input()
    p = list(map(int, input().split()[-1].split(",")))
    print(",".join(map(str, solve(a, b, c, p))))
    print(solve2(p))
