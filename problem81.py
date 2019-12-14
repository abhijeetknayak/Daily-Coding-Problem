import sys

def possible_combinations(listA, listB):
    retList = []
    if len(listA) == 0: return listB # No elements in first list
    elif len(listB) == 0: return listA # No elements in second list
    else:
        for i in listA:
            for j in listB:
                retList.append((i + j)) # Iterating over all elements in both the list to find combinations
    return retList

if __name__ == '__main__':
    mapping = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["r", "q", "t"],
               "6": ["l", "m", "n"]}
    finalList = []
    num = str(12356) #str(sys.argv[1])

    for i in range(0, len(num)):
        try:
            # First iteration with [] and mapping of first element
            finalList = possible_combinations(finalList, mapping[num[i]])
        except:
            print("Key {} missing in Mapping table".format(num[i]))
    print(finalList)




