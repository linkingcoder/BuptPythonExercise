def generate_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0
    row, col = 0, 0

    for num in range(n * n, 0, -1):
        matrix[row][col] = num

        next_row, next_col = row + directions[direction][0], col + directions[direction][1]

        if (
            next_row < 0
            or next_row >= n
            or next_col < 0
            or next_col >= n
            or matrix[next_row][next_col] != 0
        ):
            direction = (direction + 1) % 4

        row, col = row + directions[direction][0], col + directions[direction][1]

    return matrix

def print_spiral_matrix(matrix):
    n = len(matrix)
    for row in matrix:
        for num in row:
            print('{0:>{width}}'.format(num, width=4),end='')
        print()

# 读取测试组数
T = int(input())
for _ in range(T):
    n = int(input())
    spiral_matrix = generate_spiral_matrix(n)
    print_spiral_matrix(spiral_matrix)
