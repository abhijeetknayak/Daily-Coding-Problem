def find_max_contiguous_subarray(a):
    graph = {}
    for i in range(len(a) - 1, -1, -1):
        minIdx = -1
        if i == len(a) - 1:
            graph.setdefault(i, [i])
        else:
            size = 0
            minIdx = i
            for k in range(i, len(a) - 1):
                if a[i] < a[k + 1]:
                    if len(graph[k + 1]) > size:
                        size = len(graph[k + 1])
                        minIdx = k + 1
            if minIdx in graph:
                graph[i] = graph[minIdx] + [i]
            else:
                graph.setdefault(minIdx, [minIdx])
    return graph

def find_max_length_key(graph):
    k = 0
    maxLen = 0
    for key in graph:
        if len(graph[key]) > maxLen:
            maxLen = len(graph[key])
            k = key
    return k

if __name__ == '__main__':
    a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    graph = find_max_contiguous_subarray(a)
    val = find_max_length_key(graph)

    l = [a[i] for i in graph[val]]

    print("Length : {}, Values : {}".format(len(l), l))