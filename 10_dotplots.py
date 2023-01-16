import matplotlib.pyplot as plt

def slyce(line, width):
    dic = {}
    for i in range(len(line)):
        curr_slice = line[i:i+width]
        if len(curr_slice) >= 5:        # Make sure that only complete 5-letter strings are used
            if curr_slice in dic:
                dic[curr_slice].append(i)
            else:
                dic[curr_slice] = [i]
    return dic


def match_warmup_1(list1, list2):
    new_list1 = []
    new_list2 = []
    for i in list1:
        for j in list2:
            new_list1.append(i)
            new_list2.append(j)
    return new_list1, new_list2


def match_warmup_2(list1, list2):
    new_list1 = []
    new_list2 = []
    for idx in range(len(list1)):
        for sub_i in list1[idx]:
            for sub_j in list2[idx]:
                new_list1.append(sub_i)
                new_list2.append(sub_j)
    return new_list1, new_list2


def match_warmup_2_with_mw1(list1, list2):
    new_list1 = []
    new_list2 = []
    for idx in range(len(list1)):
        x, y = match_warmup_1(list1[idx], list2[idx])
        new_list1.extend(x)
        new_list2.extend(y)
    return new_list1, new_list2


def match(line_1, line_2, width):
    # Make both slice dictionaries
    d1 = slyce(line_1, width)
    d2 = slyce(line_2, width)

    # Check for duplicate keys and get the position of matching keys in two lists
    d1_pos = []
    d2_pos = []
    for key in d1:
        if key in d2:
            d1_pos.append(d1[key])
            d2_pos.append(d2[key])

    # Use the function from match_warmup_2 to combine both lists and return the result
    return match_warmup_2(d1_pos, d2_pos)


def plot(x, y, lablex, labley, width):
    plt.plot(x, y, 'o')
    plt.xlabel(lablex)
    plt.ylabel(labley)
    plt.title('Dot plot with window size {}'.format(width))

if __name__ == '__main__':
    line1 = 'My care is loss of care, by old care done'
    line2 = 'Your care is gain of care, by new care won'

    # test slyce()
    d = slyce(line1, 5)
    print(d[' care'])

    # test match_warmup_1():
    x, y = match_warmup_1([7, 2, 1, 4, 8, 9], [4, 3, 9, 8, 1, 2])
    print(sum(x), sum(y))

    # test match_warmup_2():
    x, y = match_warmup_2([[4, 5, 8], [3, 2], [6], [2, 9, 6]], [[9, 3], [8, 8], [5, 3, 5, 1], [7, 3]])
    x1, y1 = match_warmup_2_with_mw1([[4, 5, 8], [3, 2], [6], [2, 9, 6]], [[9, 3], [8, 8], [5, 3, 5, 1], [7, 3]])
    print(sum(x), sum(y))
    print(sum(x1), sum(y1))

    # test match():
    (x, y) = match(line1, line2, 5)
    print(sum(x), sum(y))
    plt.figure()
    plot(x, y, line1, line2, 5)