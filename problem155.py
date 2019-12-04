def maxNumElements(list):
    dict = {} # Dict to store value and the number of occurances
    value = None # Element with max occurances
    target = len(list) // 2 # Target value. Needs to be >= this

    for val in list:
        if val in dict: # Value already in Dict
            dict[val] += 1 # Increment
            if dict[val] >= target: # Greater than target
                value = val
                break
        else:
            dict[val] = 1

    return value

if __name__ == '__main__':
    list = [1,2,1,1,3,4,0,2,2,1,1]

    # Finding if any element has more occurances than half the size of the list
    value = maxNumElements(list)

    print(value)
