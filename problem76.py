# Function to extract column values and check if it is valid
def extract_col_values(array, col):
    k = 1
    for i in range(0, len(array) - 1):
        k = k * (array[i][col] < array[i + 1][col])
    return k


def get_invalid_col(array):
    valid_col = 0
    for i in range(0, len(array[0])): # Number of Columns
        valid_col += extract_col_values(array, i)
    return (len(array[0]) - valid_col)

if __name__ == '__main__':
    array = ["abc", "def", "ghi"]
    print(get_invalid_col(array))

    array = ["cba", "daf", "ghi"]
    print(get_invalid_col(array))

    array = ["abcdef"]
    print(get_invalid_col(array))

    array = ["zxy", "lmn", "abc"]
    print(get_invalid_col(array))