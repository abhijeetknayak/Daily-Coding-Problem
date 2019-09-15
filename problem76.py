str = 'a'

str1 = 'b'

array = ["abc", "def", "ghi"]

# Function to extract column values as a list
def extract_col_values(array, col):
    return [array[i][col] for i in range(0, len(array))]

def get_invalid_col(array):
    for i in range(0, len(array[0])): # Number of Columns
        col = extract_col_values(array, i)
        print(col)



get_invalid_col(array)



print(str1 > str)