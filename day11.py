def print_grid(grid):
    for row in grid:
        print("".join(row))

def is_blank_row(grid, i):
    for char in grid[i]:
        if char=="#":
            return False
    return True

def is_blank_column(grid, j):
    for row in grid:
        if row[j]=="#":
            return False
    return True

def find_row_offsets(grid, offset):
    n=len(grid)
    res=[0]*n
    for i in range(1, n):
        if is_blank_row(grid, i-1):
            res[i]=offset+res[i-1]
        else:
            res[i]=res[i-1]
    return res

def find_column_offsets(grid, offset):
    m=len(grid[0])
    res=[0]*m
    for j in range(1, m):
        if is_blank_column(grid, j-1):
            res[j]=res[j-1]+offset
        else:
            res[j]=res[j-1]
    return res

def main():
    fname="day11_input.txt"
    grid=[]
    with open(fname) as inputfile:
        for line in inputfile:
            grid.append(list(line.strip()))
    offset=999999 #1 for part 1, 999999 for part 2
    offsets_row, offsets_col = find_row_offsets(grid, offset), find_column_offsets(grid, offset)
    galaxies=[]
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char=="#":
                galaxies.append((i+offsets_row[i], j+offsets_col[j]))
    res=0
    for i in range(len(galaxies)):
        for j in range(i):
            res+=abs(galaxies[i][0]-galaxies[j][0])+abs(galaxies[i][1]-galaxies[j][1])
    print(res)
main()