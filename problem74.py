def find_count(N, X):
    count = 0
    for i in range(1, N + 1):
        if X % i == 0: # i divides X
            val = X // i
            if val <= N:
                count += 1
    return count

if __name__ == '__main__':
    print(find_count(5, 12))
    print(find_count(1, 1))