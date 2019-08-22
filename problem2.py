import numpy as np

def rotate_list(input):
    list_without_last = input[0:-1]
    final = [input[-1]] + list_without_last
    return final

def multiply(input):
    ones = [1] * len(input)
    for i in range(len(input) - 1):
        rotated = rotate_list(input)
        ones = np.multiply(ones, rotated)
        input = rotated
    return ones

print(multiply([1,2,3,4,5]))
print(multiply([1,1,2,1,2,4,5,6]))