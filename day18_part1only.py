def read_input(fname):
    res=[]
    with open(fname) as inputfile:
        for line in inputfile:
            dir, N, _ = line.strip().split()
            res.append((dir, int(N)))
    return res

def count_points_outside(mini, minj, n, m, visited):
    i, j = -1, -1
    outside=set()
    outside.add((i, j))
    stack=[(i, j)]
    while stack:
        ii, jj = stack.pop()
        for iin, jjn in [(ii+1, jj), (ii-1, jj), (ii, jj+1), (ii, jj-1)]:
            if iin<-1 or iin>n or jjn<-1 or jjn>m or (iin+mini, jjn+minj) in visited or (iin, jjn) in outside:
                continue
            outside.add((iin, jjn))
            stack.append((iin, jjn))
    return len(outside)

def part1(instructions):
    visited=set()
    directions={"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}
    mini, minj, maxi, maxj = 10**9, 10**9, -10**9, -10**9
    i, j = 0, 0
    for dir, N in instructions:
        di, dj = directions[dir]
        for _ in range(N):
            i+=di
            j+=dj
            visited.add((i, j))
            mini, minj, maxi, maxj = min(i, mini), min(j, minj), max(i, maxi), max(j, maxj)
    n, m = maxi-mini+1, maxj-minj+1
    print((n+2)*(m+2)-count_points_outside(mini, minj, n, m, visited))

fname="day18_input.txt"
part1(read_input(fname))