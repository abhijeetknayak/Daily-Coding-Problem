def find_max_subset(max_set):
    graph = {}    # Dict to store possible subsets
    skip = False  # For new elements
    for val in max_set:  # Iterating through all elements in super set
        for key in graph:
            if val % key == 0 or key % val == 0:  # Part of the same 'key' subset
                graph[key].append(val)
                skip = True
        if skip is False:  # No valid subset available. Add a new key
            graph[val] = []

    max_len = 0  # Length of max subset
    final_key = None
    for key in graph:
        if len(graph[key]) > max_len:  # max Len
            max_len = len(graph[key])
            final_key = key
    max_subset = [final_key] + graph[final_key]

    return max_subset


if __name__ == '__main__':
    s = [3, 5, 10, 20, 21, 27, 33]
    print(find_max_subset(s))
    s = [2, 4, 5, 54, 65, 43, 22, 29, 78, 75]
    print(find_max_subset(s))
