
test = []
with open("input") as f:
    for line in f:
        test.append(list(line))

# test = [['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'], ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'], ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'], ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'], ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'], ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'], ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'], ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'], ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'], ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']]
count = 0

def get_str(arr):
    # given array of row,col coordinates, return string
    str = ''
    for i, j in arr:
        if i >= 0 and i < len(test) and j >= 0 and j < len(test[0]):
            str += test[i][j]
    return str

def search(row, col):
    # generate all possible 4 letter strings from row,col
    # should be 8 total
    count = 0
    part1_searches = [
        [(row + i, col) for i in range(0,4)],
        [(row - i, col) for i in range(0,4)],
        [(row, col + i) for i in range(0,4)],
        [(row, col - i) for i in range(0,4)],
        [(row + i, col + i) for i in range(0,4)],
        [(row - i, col - i) for i in range(0,4)],
        [(row + i, col - i) for i in range(0,4)],
        [(row - i, col + i) for i in range(0,4)],
    ]
    part2_searches = [
        [(row-1, col-1), (row, col), (row+1, col+1)],
        [(row-1, col+1), (row, col), (row+1, col-1)]
    ]

    # for s in part1_searches:
    #     if get_str(s) == 'XMAS':
    #         count += 1

    valid = ['MAS', 'SAM']
    if get_str(part2_searches[0]) in valid and get_str(part2_searches[1]) in valid:
        count += 1

    return count

for row in range(len(test)):
    for col in range(len(test[0])):
        # if test[row][col] == 'X':
        if test[row][col] == 'A':
            count += search(row, col)

print(count)





