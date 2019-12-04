def count_odd_occurances(graph): # If it has to be a palindrome, it can have either one odd occurance
    # or all even. Checking that in this function
    odd_count = 0
    for key in graph:
        if graph[key] % 2 != 0:
            odd_count += 1
    return odd_count

def count_occurances(str):
    graph = {}
    for i in str: # Storing char and number of occurances in dictionary
        if i in graph:
            graph[i] += 1
        else:
            graph[i] = 1

    return(count_odd_occurances(graph))


if __name__ == '__main__':
    str = 'carrace'
    str = 'Daily'

    odd_count = count_occurances(str)

    if odd_count >= 2:
        print(False)
    else:
        print(True)




