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


def reconstruct(lys, overlaps):
    # Start to reconstruct the string with the element that has no matching end.
    new_line_idx = None
    for key, value in overlaps.items():
        if len(value) == 0:
            if new_line_idx is None:
                s = lys[key]
                new_line_idx = key
            else:
                raise Exception('More than one line without matching end! Could not determine end of string!')
    if new_line_idx is None:
        raise Exception('No line without matching end! Could not determine end of string!')

    # Reconstruct rest of the string (back to front) by finding the current line (key) as a value in the next line
    for i in range(len(lys)-1):
        # Find value with the current line_idx and the longest matching string, and save it as max_overlap
        max_overlap = (0, 0)
        for key, value in overlaps.items():
            for match in value:
                if new_line_idx in match:
                    if match[1] > max_overlap[1]:
                        max_overlap = (key, match[1])
        # Update new_line_idx for the next for-loop round
        new_line_idx = max_overlap[0]
        # Remove overlapping characters from the new line
        new_line = lys[new_line_idx][:-max_overlap[1]]
        # Check if this string is already part of the reconstruction (can happen with small duplicate substrings)
        if new_line not in s:
            # Prepend the new line to s
            s = new_line + s

    return s

lys = ['the men and women merely players;/',
       'one man in his time',
       "All the world's",
       "their entrances,/And one man",
       'stage,/And all the men and women',
       'They have their exits and their entrances,/',
       "world's a stage,/And all",
       "their entrances,/And one man",
       "in his time plays many parts.",
       "merely players;/They have"]

overlaps = get_overlaps(lys)
reconstruction = reconstruct(lys, overlaps)
print(reconstruction)


