lys = ['the men and women merely players;/',
       'one man in his time', "All the world's",
       "their entrances,/And one man",
       'stage,/And all the men and women',
       'They have their exits and their entrances,/',
       "world's a stage,/And all",
       "their entrances,/And one man",
       "in his time plays many parts.",
       "merely players;/They have"]

def get_overlaps(lys):
    overlaps = {}
    # Go through all lines for each line
    for idx1, first in enumerate(lys):
        for idx2, second in enumerate(lys):
            # get the length of the shorter line (maximum possible overlap)
            min_len = min(len(first), len(second))
            # Go through all possible overlaps
            for i in range(min_len):
                # Check if the end of the first and the start of the second strings match
                if first[-i:] == second[:i]:
                    # If yes, add them to the dict
                    if idx1 in overlaps:
                        overlaps[idx1].append((idx2, i))
                    else:
                        overlaps[idx1] = [(idx2, i)]
        # If no match has been found for the current line, add an empty list to the dict
        if idx1 not in overlaps:
            overlaps[idx1] = []
    return overlaps
