soln = set()

k = 17
array = [10,3,5,7]


def solution(array, k):
    for num in array:
        if num in soln:
            return True
        else:
            soln.add(k - num)
    print(soln)
    return False

def soln_hash_table(array, k):
    table = {}
    for val in array:
        table.setdefault(val, 0)
    for x in table.keys():
        if k - x in table:
            return True
    return False


print(solution(array, k))
print(soln_hash_table(array, k))