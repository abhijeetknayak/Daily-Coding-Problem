def find_count_naive(matrix, i1, j1, i2, j2):
    lim1 = matrix[i1][j1]  # Limits to find count
    lim2 = matrix[i2][j2]
    # lim1 = min(matrix[i1][j1], matrix[i2][j2])  # If max and min needs to be separated
    # lim2 = max(matrix[i1][j1], matrix[i2][j2])
    count = 0
    for row in matrix:
        count += len([1 for val in row if val > lim2 or val < lim1])  # Iterating over all rows to find possible values
    return count


if __name__ == '__main__':
    matrix = [[1, 3, 7, 10, 15, 20],
              [2, 6, 9, 14, 22, 25],
              [3, 8, 10, 15, 25, 30],
              [10, 11, 12, 23, 30, 35],
              [20, 25, 30, 35, 40, 45]]

    i1, j1 = 1, 1
    i2, j2 = 3, 3
    print(find_count_naive(matrix, i1, j1, i2, j2))
