list_1 = []
list_2 = []
list_2_hist = {}
with open("input") as f:
    for line in f:
        if line:
            line_split = line.split()
            line_1 = int(line_split[0])
            line_2 = int(line_split[1])
            list_1.append(line_1)
            list_2.append(line_2)
            if line_2 in list_2_hist:
                list_2_hist[line_2] += 1
            else:
                list_2_hist[line_2] = 1

list_1.sort()
list_2.sort()

list_distance = sum([abs(list_2[i] - list_1[i]) for i in range(len(list_1))])
similarity_score = sum([list_item * (list_2_hist[list_item] if list_item in list_2_hist else 0) for list_item in list_1])
print(similarity_score)





