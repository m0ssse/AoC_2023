from heapq import heappush, heappop

def traverse(fname, minmoves, maxmoves):
    grid=[]
    with open(fname) as inputfile:
        for line in inputfile:
            grid.append([int(x) for x in line.strip()])
    n, m = len(grid), len(grid[0])
    heap=[]
    heappush(heap, (0, 0, 0, 1, 0, 0))
    heappush(heap, (0, 0, 0, 0, 1, 0)) #heat loss, i, j, di, dj, moves
    visited=set()
    visited.add((0, 0, 1, 0, 0))
    visited.add((0, 0, 0, 1, 0))
    while heap:
        loss, i, j, di, dj, moves=heappop(heap)
        if (i, j)==(n-1, m-1):
            return loss
        neighbs=[(i+di, j+dj, di, dj, moves+1)]
        if di and moves>=minmoves:
            neighbs.append((i, j+1, 0, 1, 1))
            neighbs.append((i, j-1, 0, -1, 1))
        elif dj and moves>=minmoves:
            neighbs.append((i+1, j, 1, 0, 1))
            neighbs.append((i-1, j, -1, 0, 1))
        for ii, jj, dii, djj, movesn in neighbs:
            if ii<0 or ii>=n or jj<0 or jj>=m or movesn>maxmoves:
                continue
            if (ii, jj, dii, djj, movesn) in visited:
                continue
            heappush(heap, (loss+grid[ii][jj], ii, jj, dii, djj, movesn))
            visited.add((ii, jj, dii, djj, movesn))

fname="day17_input.txt"
print(traverse(fname, 4, 10))