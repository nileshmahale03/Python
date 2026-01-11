#matrix

#input matrix
N, M = map(int, input().split())

matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

#creating a 2D list
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[1][2])

rows = 3
cols = 3
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * j)
    matrix.append(row)

print(matrix)

#iterating over 2D lists

for row in matrix:
    print(row)

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()

for row in matrix:
    for val in row:
        print(val, end = " ")
    print()

for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        print(matrix[i][j])

#diagonal sum
N = len(matrix)

main_sum = 0
secondary_sum = 0

for i in range(N):
    main_sum += matrix[i][i]
    secondary_sum += matrix[i][N - i - 1]

print(main_sum, secondary_sum)

#8 direction neighbour check 
def has_dot_neighbor(matrix, X, Y):
    n = len(matrix)
    m = len(matrix[0])

    # 8 possible directions
    dirs = [
        (0, -1),   # left
        (0,  1),   # right
        (-1, 0),   # up
        (1,  0),   # down
        (-1, -1),  # top-left
        (-1,  1),  # top-right
        (1,  1),   # bottom-right
        (1, -1)    # bottom-left
    ]

    for dx, dy in dirs:
        nx, ny = X + dx, Y + dy

        # check bounds
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == '.':
                return True

    return False

#mirror array 
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    matrix[i].reverse()

for row in matrix:
    print(*row)