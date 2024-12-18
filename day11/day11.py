from collections import defaultdict
import math


def num_stones(inp_str, num_blinks):

    inp = [int(i) for i in inp_str.split()]

    def num_stones_for_single(num):
        stack = [num]
        num_stones = 1
        for _ in range(num_blinks):
            new_stack = []
            while len(stack) > 0:
                curr = stack.pop()
                if curr == 0:
                    new_stack.append(1)
                elif len(str(curr)) % 2 == 0:
                    num_stones += 1
                    mid = len(str(curr)) // 2
                    new_stack.append(int(str(curr)[:mid]))
                    new_stack.append(int(str(curr)[mid:]))
                else:
                    new_stack.append(curr * 2024)
            stack = new_stack
        return num_stones

    return sum([num_stones_for_single(n) for n in inp])


def num_stones_part_2(inp_str, num_blinks):
    inp = [int(i) for i in inp_str.split()]
    # memo[(n, k)] = number of stones produced for number n after k blinks
    memo = defaultdict(int)

    def num_stones_for_single_recursive(n, k):
        num_digits = math.floor(math.log(n, 10)) + 1 if n > 0 else 1
        if (n, k) in memo:
            return memo[(n, k)]
        if k == 0:
            memo[(n, k)] = 1
        elif n == 0:
            memo[(n, k)] = num_stones_for_single_recursive(1, k - 1)
        elif num_digits % 2 == 0:
            left = n // (10 ** (num_digits // 2))
            right = n % (10 ** (num_digits // 2))
            memo[(n, k)] = num_stones_for_single_recursive(
                left, k - 1
            ) + num_stones_for_single_recursive(right, k - 1)
        else:
            memo[(n, k)] = num_stones_for_single_recursive(n * 2024, k - 1)
        return memo[(n, k)]

    def num_stones_for_single(num):
        stack = [(num, num_blinks)]
        while len(stack) > 0:
            curr, gen = stack[-1]
            if (curr, gen) in memo:
                stack.pop()
            elif gen == 0:
                memo[(curr, gen)] = 1
                stack.pop()
            elif curr == 0:
                next = (1, gen - 1)
                if next in memo:
                    memo[(curr, gen)] = memo[next]
                    stack.pop()
                else:
                    stack.append(next)
            elif len(str(curr)) % 2 == 0:
                mid = len(str(curr)) // 2
                left = (int(str(curr)[:mid]), gen - 1)
                right = (int(str(curr)[mid:]), gen - 1)
                if right not in memo:
                    stack.append(right)
                if left not in memo:
                    stack.append(left)
                if left in memo and right in memo:
                    memo[(curr, gen)] = memo[left] + memo[right]
            else:
                next = (curr * 2024, gen - 1)
                if next in memo:
                    memo[(curr, gen)] = memo[next]
                    stack.pop()
                else:
                    stack.append(next)
        return memo[(num, num_blinks)]

    return sum([num_stones_for_single_recursive(n, num_blinks) for n in inp])


def test():
    test_input = "125 17"

    assert num_stones(test_input, 6) == 22
    assert num_stones(test_input, 25) == 55312
    assert num_stones_part_2(test_input, 6) == 22
    assert num_stones_part_2(test_input, 25) == 55312


def solve():
    with open("input") as f:
        inp = f.read().strip()

        print(f"part 1: {num_stones(inp, 25)}")
        print(f"part 2: {num_stones_part_2(inp, 75)}")


test()
solve()
