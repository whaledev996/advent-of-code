def is_safe(report):
    if len(report) < 2:
        return True
    else:
        check = 1 if report[1] > report[0] else -1
        for i in range(1, len(report)):
            if check == 1:
                if report[i] < report[i-1]:
                    return False
            if check == -1:
                if report[i] > report[i-1]:
                    return False
            diff = abs(report[i] - report[i-1])
            if diff > 3 or diff < 1:
                return False
        return True

# assert is_safe([7, 6, 4, 2, 1]) == True
# assert is_safe([1, 2, 7, 8, 9]) == False
# assert is_safe([9, 7, 6, 2, 1]) == False
# assert is_safe([1, 3, 2, 4, 5]) == False
# assert is_safe([8, 6, 4, 4, 1]) == False
# assert is_safe([1, 3, 6, 7, 9]) == True
            
with open("input") as f:
    num_safe = 0
    for line in f:
        report = line.split()
        report = [int(r) for r in report]
        safe = is_safe(report)
        if safe:
            num_safe += 1
        else:
            # try other combos
            for i in range(len(report)):
                is_other_safe = is_safe(report[0:i] + report[i+1:len(report)])
                if is_other_safe:
                    num_safe += 1
                    break
    print(num_safe)
            
