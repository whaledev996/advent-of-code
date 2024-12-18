def compute_checksum(str):
    n = [int(s) for s in str]
    arr = [-1] * sum(n)
    offset = 0
    id = 0
    for i in range(len(n)):
        if i % 2 == 0:
            for _ in range(n[i]):
                arr[offset] = id
                offset += 1
            id += 1
        else:
            offset += n[i]

    def find_next_free(idx):
        for i in range(idx, len(arr)):
            if arr[i] == -1:
                return i
        return -1

    def find_next_avail(idx):
        for i in range(idx, -1, -1):
            if arr[i] != -1:
                return i
        return -1

    left, right = 0, len(arr) - 1
    while True:
        left = find_next_free(left)
        right = find_next_avail(right)
        if left >= right:
            break
        tmp = arr[left]
        arr[left] = arr[right]
        arr[right] = tmp

    checksum = 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            checksum += i * arr[i]

    return checksum


def compute_checksum_part_2(str):
    n = [int(s) for s in str]
    arr = [-1] * sum(n)
    offset = 0
    id = 0
    seen = {-1}
    for i in range(len(n)):
        if i % 2 == 0:
            for _ in range(n[i]):
                arr[offset] = id
                offset += 1
            id += 1
        else:
            offset += n[i]

    def find_next_free_block(size, end_idx):
        i = 0
        while i < end_idx:
            tmp_size = 0
            idx = i
            while i < end_idx and arr[i] == -1:
                tmp_size += 1
                i += 1
            if tmp_size >= size:
                return idx, tmp_size
            i += 1
        return -1, 0

    def find_next_avail(idx):
        for i in range(idx, -1, -1):
            if arr[i] not in seen:
                tmp_size = 0
                tmp_idx = i
                while i >= 0 and arr[i] == arr[i - 1]:
                    tmp_size += 1
                    i -= 1
                return tmp_idx, tmp_size + 1
        return -1, 0

    right = len(arr) - 1
    while right > 0:
        start_idx, size = find_next_avail(right)
        if start_idx == -1:
            break
        seen.add(arr[start_idx])
        free_idx, _ = find_next_free_block(size, right)
        if free_idx > start_idx:
            break
        if free_idx != -1:
            for j in range(size):
                tmp = arr[free_idx + j]
                arr[free_idx + j] = arr[start_idx - j]
                arr[start_idx - j] = tmp
        right = start_idx - size

    checksum = 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            checksum += i * arr[i]

    return checksum


def test():
    test_input = "2333133121414131402"
    assert compute_checksum(test_input) == 1928
    assert compute_checksum_part_2(test_input) == 2858


def solve():
    input = ""
    with open("input") as f:
        input = f.read().strip()

    print(f"part 1: {compute_checksum(input)}")
    print(f"part 2: {compute_checksum_part_2(input)}")


test()
solve()
