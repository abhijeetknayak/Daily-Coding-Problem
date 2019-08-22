soln = set()

k = 17
array = [10,3,5]


def solution(array, k):
    for num in array:
        if num in soln:
            return True
        else:
            soln.add(k - num)
    print(soln)
    return False

print(solution(array, k))