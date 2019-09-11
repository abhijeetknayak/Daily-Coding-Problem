a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

graph = {}
for i in range(len(a) - 1, -1, -1):
    minIdx = -1
    if i == len(a) - 1:
        graph.setdefault(i, [i])
    else:
        size = 0
        minIdx = i
        for k in range(i, len(a) - 1):
            min = a[i]
            if min < a[k + 1]:
                if len(graph[k + 1]) > size:
                    size = len(graph[k + 1])
                    minIdx = k + 1
                # min = a[k + 1] # Index with minimum value. This would lead to a list with max number of elements
                # minIdx = k + 1
        if minIdx in graph:
            graph[i] = graph[minIdx] + [i]
        else:
            graph.setdefault(minIdx, [minIdx])

print(graph)