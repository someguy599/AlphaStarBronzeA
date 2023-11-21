NR, NC = map(int, input("").split(" "))
grid = []
sums = []
max = 0
coord = (0, 0)

for i in range(NR):
    grid.append(list(map(int, input("").split(" "))))

for row in range(NR - 2):
    for column in range(NC - 2):
        row1 = grid[row][column] + grid[row][column + 1] + grid[row][column + 2]
        row2 = grid[row + 1][column] + grid[row + 1][column + 1] + grid[row + 1][column + 2]
        row3 = grid[row + 2][column] + grid[row + 2][column + 1] + grid[row + 2][column + 2]
        if row1 + row2 + row3 > max:
            max = row1 + row2 + row3
            coord = (row + 1, column + 1)

print(max)
print(coord[0], coord[1])