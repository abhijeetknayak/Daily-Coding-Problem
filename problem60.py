import numpy as np

def find_all_possible_elements(a):
    b = {0}
    while len(a) != 0:
        element = a.pop() # New element from initial set

        c = set()
        while len(b) != 0: # Going through all elements of set B.
            b_element = b.pop()
            c.add(b_element) # Previous element without adding new one
            c.add(element + b_element) # New element by adding the next element in array
        b = c
    return b

def partition_possible(array):
    element_sum = np.sum(array)
    if element_sum % 2 == 0: # Possible to break into two subsets
        pos_values = find_all_possible_elements(array)
        if element_sum // 2 in pos_values: # (sum / 2) available in possible values
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    # a = [15, 5, 20, 10, 35, 15, 10]
    a = [15, 15, 15, 15]
    print(partition_possible(a))

