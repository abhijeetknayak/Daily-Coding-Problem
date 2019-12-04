import numpy as np

def recurse(i, j):
    global count
    if i == height - 1 and j == width - 1: # Exit this Recursive call. Reached Exit
        count += 1
    if i + 1 < height and mat[i + 1][j] == 0: # Possible movement to the right
        recurse(i + 1, j)
    if j + 1 < width and mat[i][j + 1] == 0: # Possible Movement Down
        recurse(i, j + 1)

if __name__ == '__main__':
    mat = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    height, width = mat.shape

    count = 0
    i, j = 0, 0 # Start Points

    # Calling Function to recursively find all paths
    recurse(i, j)

    print(count)

