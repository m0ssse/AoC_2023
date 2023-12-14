def part1(fname):
    grid=read_input(fname)
    n, m = len(grid), len(grid[0])
    res=0
    for j in range(m):
        queue=[]
        k=0
        for i in range(n):
            if grid[i][j]==".":
                queue.append(i)
            elif grid[i][j]=="O":
                queue.append(i)
                res+=n-queue[k]
                k+=1
            else:
                queue.clear()
                k=0

    print(res)

def read_input(fname):
    with open(fname) as inputfile:
        return inputfile.read().split("\n")

def transpose(grid):
    n=len(grid)
    transp=[[grid[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i):
            transp[i][j], transp[j][i] = transp[j][i], transp[i][j]
    return transp

def rotate_ccw(grid):
    """rotates a square matrix 90 degrees counterclockwise"""
    return transpose(grid)[::-1]

def rotate_cw(grid):
    """rotates a square matrix 90 degrees clockwise"""
    return transpose(grid[::-1])

def tilt_N(grid):
    n, m = len(grid), len(grid[0])
    newgrid=[["."]*m for _ in range(n)]
    for j in range(m):
        queue=[]
        k=0
        for i in range(n):
            if grid[i][j]=="#":
                newgrid[i][j]="#"
                queue=[]
                k=0
            elif grid[i][j]==".":
                queue.append(i)
            else:
                queue.append(i)
                newgrid[queue[k]][j]="O"
                k+=1
    return newgrid

def tilt_S(grid):
    return tilt_N(grid[::-1])[::-1]

def tilt_E(grid):
    return rotate_cw(tilt_N(rotate_ccw(grid)))

def tilt_W(grid):
    return rotate_ccw(tilt_N(rotate_cw(grid)))

def print_grid(grid):
    for line in grid:
        print("".join(line))

def cycle(grid):
    return tilt_E(tilt_S(tilt_W(tilt_N(grid))))

def calculate_load(grid):
    res=0
    n=len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j]=="O":
                res+=n-i
    return res

def part2(fname):
    grid=read_input(fname)
    N=10**9
    i=0
    s="\n".join(grid)
    seen={s: 0}
    s="".join(grid)
    while i<N:
        grid=cycle(grid)
        s="\n".join(["".join(row) for row in grid])
        i+=1
        if s in seen:
            break
        seen[s]=i
    period=i-seen[s]
    cyclesleft=(N-i)%period
    for _ in range(cyclesleft):
        grid=cycle(grid)
    print(calculate_load(grid) )  
 
fname="day14_input.txt"
part1(fname)
part2(fname)
