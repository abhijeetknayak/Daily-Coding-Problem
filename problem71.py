import numpy as np
from tqdm import tqdm

graph = {}
sum = 0
result = []

def rand7():
    return np.random.randint(1, 8)


def rand5():
    global one, two, three, four, five
    a = [(rand7() % 5) + 1 for i in range(0, 5)]

    sum = (np.sum(a) % 5 + 1)
    if sum in graph:
        graph[sum] = graph[sum] + 1
    else:
        graph.setdefault(sum, 1)

if __name__ == '__main__':
    for i in tqdm(range(0, 1000000)):
        rand5()
    for i in graph.keys():
        sum = sum + graph[i]
    for i in graph.keys():
        result.append(round((graph[i] / sum), 2))

    print(result)

