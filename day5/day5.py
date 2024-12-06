from collections import defaultdict
test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

rules = defaultdict(set)
correct = []
incorrect = []

with open('input') as f:
    for line in f:
        if '|' in line:
            left, right = line.split('|')
            rules[int(left)].add(int(right))
        if ',' in line:
            update = line.split(',')
            update = [int(u) for u in update]
            seen = []
            broken = False
            for page in update:
                seen.append(page)
                intersect = set(seen) & rules[page]
                if len(intersect) > 0:
                    broken = True
                    idx = min([seen.index(i) for i in intersect])
                    seen.pop()
                    seen.insert(idx, page)
            if not broken:
                correct.append(update)
            if broken:
                incorrect.append(seen)


# print(correct)
# print(sum([update[(len(update) - 1) // 2] for update in correct]))
# print(incorrect)
print(sum([update[(len(update) - 1) // 2] for update in incorrect]))




