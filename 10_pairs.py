
# Option 1
def make_pairs(lys):
    pairs = []
    for i in lys:
        for j in lys:
            if [j, i] not in pairs and [i, j] not in pairs and j != i:
                pairs.append([i, j])
    return pairs

# Option 2:
# ?

# Option 3:
def make_pairs(lys):
    # Make list with all pairs
    pairs = []
    for i in lys:
        for j in lys:
            pairs.append([i, j])

    # Loop through the pairs list backwards (not avoid indexing errors while deleting
    for i in range(len(pairs)-1, -1, -1):
        # Save the current pair
        current_pair = pairs[i]
        # Test if the current pair exists in "pairs" in reverse order, or if both elements are the same
        if [current_pair[1], current_pair[0]] in pairs or current_pair[0] == current_pair[1]:
            pairs.remove(current_pair)
    return pairs

if __name__ == '__main__':
    l = ['ball','clock','glass','table']
    pair = make_pairs(l)
