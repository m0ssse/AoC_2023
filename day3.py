def get_all_neighbs(i, j1, j2):
    res=[(i-1, j1-1), (i, j1-1), (i+1, j1-1),(i-1, j2+1), (i, j2+1), (i+1, j2+1)]
    for j in range(j1, j2+1):
        res.append((i+1, j))
        res.append((i-1, j))
    return res

def is_not_isolated(i, j1, j2, grid, n, m):
    neighbs=get_all_neighbs(i, j1, j2)
    for ii, jj in neighbs:
        if ii<0 or ii>=n or jj<0 or jj>=m:
            continue
        if grid[ii][jj] not in ".0123456789":
            return True
    return False

def get_neighboring_asterisks(i, j1, j2, grid, n, m):
    neighbs=get_all_neighbs(i, j1, j2)
    res=[]
    for ii, jj in neighbs:
        if ii<0 or ii>=n or jj<0 or jj>=m:
            continue
        if grid[ii][jj]=="*":
            res.append((ii, jj))
    return res

def solve(grid, n, m):
    res=0
    asterisks={}
    for i, line in enumerate(grid):
        currdigitstart=-1
        currdigit=""
        for j, char in enumerate(line):
            if char.isnumeric():
                if not currdigit:
                    currdigitstart=j
                currdigit+=char
            else:
                if currdigit:
                    if is_not_isolated(i, currdigitstart, j-1, grid, n, m):
                        res+=int(currdigit)
                    helper=get_neighboring_asterisks(i, currdigitstart, j-1, grid, n, m)
                    for ii, jj in helper:
                        if (ii, jj) not in asterisks:
                            asterisks[(ii, jj)]=[]
                        asterisks[(ii, jj)].append(int(currdigit))
                currdigitstart=-1
                currdigit=""
        if currdigit:
            if is_not_isolated(i, currdigitstart, j, grid, n, m):
                res+=int(currdigit)
            helper=get_neighboring_asterisks(i, currdigitstart, j, grid, n, m)
            for ii, jj in helper:
                if (ii, jj) not in asterisks:
                    asterisks[(ii, jj)]=[]
                asterisks[(ii, jj)].append(int(currdigit))
    print(res)
    res=0
    for nums in asterisks.values():
        if len(nums)==2:
            res+=nums[0]*nums[1]
    print(res)

fname="day3_input.txt"
with open(fname) as myfile:
    grid=myfile.read().split("\n")
n, m = len(grid), len(grid[0])
solve(grid, n, m)