import re

enabled = True

def mul(x,y):
    return x*y

def compute(match):
    global enabled
    op = match.split('(')[0]
    if (op == 'mul'):
        if enabled:
            return eval(match)
        else:
            return 0
    if (op == "don't"):
        enabled = False
        return 0
    if (op == 'do'):
        enabled = True
        return 0
    return 0


with open("input") as f:
    count = 0
    for line in f:
        matches = re.findall(r'mul\(\d*\,\d*\)|don\'t\(\)|do\(\)', line)
        count += sum([compute(match) for match in matches])
    print(count)

