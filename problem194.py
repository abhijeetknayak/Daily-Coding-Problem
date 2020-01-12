def recursive_function(list1, list2, first_index):
    global count
    for i in range(first_index + 1, len(list1)):
        if (list1[first_index] > list1[i] and list2[first_index] < list2[i]) or \
                (list1[first_index] < list1[i] and list2[first_index] > list2[i]):  # Condition for intersection
            count += 1
    if first_index + 1 < len(list1):  # Recursive call with an updated first index, if possible
        recursive_function(list1, list2, first_index + 1)


def find_num_intersections(list1, list2):
    recursive_function(list1, list2, 0)  # First Index is 0. Start with 0


if __name__ == '__main__':
    list1 = [4, 3, 1, 2]  # Two sets of points along lines y = 0 and y = 1
    list2 = [1, 2, 3, 4]
    count = 0  # Final count of the number of intersections. Global variable

    find_num_intersections(list1, list2)
    print(count)
