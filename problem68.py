def find_attacks(a):
    count = 0
    for (i, j) in a:
        for (l, m) in a:
            if i != l and j != m:
                x, y = abs(i - l), abs(j - m)
                if x == y: # Expect the absolute difference to be equal(Diagonal)
                    count = count + 1
    return int(count / 2) # Count includes two attacks for a pair of bishops


def find_attack_add(a, m):
    count = 0
    for (x, y) in a:
        new_points = []
        i, l, s = x, x, x
        j, n, t = y, y, y

        # Adding possible attack points in all directions
        while i + 1 < m and j + 1 < m:
            i, j = i + 1, j + 1
            new_points.append((i, j))
        while x - 1 >= 0 and y - 1 >= 0:
            x, y = x - 1, y - 1
            new_points.append((x, y))
        while l - 1 >= 0 and n + 1 < m:
            l, n = l - 1, n + 1
            new_points.append((l, n))
        while s + 1 < m and t - 1 >= 0:
            s, t = s + 1, t - 1
            new_points.append((s, t))

        # Checking if the bishop points are in the possible attack points
        for i in a:
            if i in new_points:
                count = count + 1

    return int(count / 2) # Each attack between a pair counted twice


if __name__ == '__main__':
    # a = [(0, 0), (1, 2), (2, 2), (4, 0)]
    a = [(0, 0), (0, 3), (1, 5), (1, 6), (2, 1), (2, 4), (3, 0), (4, 2), (4, 6), (5, 2), (5, 4), (6, 0), (6, 6)]
    print(find_attacks(a))
    print(find_attack_add(a, 7))

