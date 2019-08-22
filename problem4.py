import numpy as np

def calculate_MinVal(input):
    maxval = 0
    input = [x for x in input if x > 0]
    for i in range(len(input)):
        if 1 not in input:
            return (maxval + 1)
        else:
            maxval = maxval + 1
            input = np.subtract(input, [1] * len(input))
    return (maxval + 1)


print(calculate_MinVal([-2,-1,0,1,2,3,4]))
print(calculate_MinVal([1,2,0]))
print(calculate_MinVal([-2,-1,0,1,2,3,4,5,6,67,7,8,10]))
print(calculate_MinVal([-2,-1,0,67,7,8,10]))
print(calculate_MinVal([1,-2,-1]))