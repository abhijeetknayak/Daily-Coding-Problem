import numpy as np

def pow(a, b):
    k = b * np.log(a)
    return np.exp(k)

def power(a, b):
    res = [] # Storing Intermediate results
    power = [] # Storing Intermediate powers
    current_pow = 1
    diff = 0 # Stores the difference between the max current power reached and 'b'
    if b == 0: # Base Case
        return 1
    elif a == 0: # Base Case
        return 0
    elif b < 0: # Negative power, Converting this to positive power and Inverse of 'a'
        a = 1 / a
        b = abs(b)

    result = a

    while current_pow <= b:
        res.append(result)
        power.append(current_pow)
        if 2 * current_pow <= b:
            result = result * result
            current_pow = 2 * current_pow
        else:
            diff = b - current_pow
            break
    # Looping over all possible powers to see if they can be used. Aim: Diff = 0
    for i in range(len(power) - 1, 0, -1):
        if diff == 0: # Loop Exit
            break
        elif diff - power[i] >= 0: # Diff still not zero
            result = result * res[i] # Updating Result
            diff = diff - power[i] # Updating Diff
    return result

print(power(2,10))
print(power(3, 10))
print(power(2,-4))
print(power(0,3))
print(power(3,0))