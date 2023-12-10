def get_neighbs(char, i, j):
    if char=="-":
        return [(i, j+1), (i, j-1)]
    if char=="|":
        return [(i+1, j), (i-1, j)]
    if char=="F":
        return [(i+1, j), (i, j+1)]
    if char=="J":
        return [(i-1, j), (i, j-1)]
    if char=="L":
        return [(i-1, j), (i, j+1)]
    if char=="7":
        return [(i+1, j), (i, j-1)]
    return []

def print_grid(grid):
    for row in grid:
        print("".join(row))

def print_flow(grid):
    for row in grid:
        for flow in row:
            if flow:
                print(f"({flow})", end="")
            else:
                print("    ", end="")
        print()

def get_top_left(grid):
    n, m = len(grid), len(grid[0])
    for k in range(n+m-1):
        for ii in range(k+1):
            if grid[ii][k-ii]=="F":
                return ii, k-ii

def is_inside(i, j, grid, flowdir):
    n=len(grid)
    for ii in range(i+1, n):
        if grid[ii][j]=="-":
            if flowdir[ii][j]=="LR":
                return 0
            return 1
        if grid[ii][j]=="F":
            if flowdir[ii][j]=="DR":
                return 0
            return 1
        if grid[ii][j]=="7":
            if flowdir[ii][j]=="LD":
                return 0
            return 1
        if grid[ii][j]=="L":
            if flowdir[ii][j]=="RU":
                return 0
            return 1
        if grid[ii][j]=="J":
            if flowdir[ii][j]=="UL":
                return 0
            return 1
    return 0

def get_flow_direction(grid):
    #keys: tile, flow_from
    #values: flow_to, flow_from (next), di, dj
    flow_mapping={
        ("-", "L"): ("R", "L", 0, 1),
        ("-", "R"): ("L", "R", 0, -1),
        ("|", "D"): ("U", "D", -1, 0),
        ("|", "U"): ("D", "U", 1, 0),
        ("F", "D"): ("R", "L", 0, 1),
        ("F", "R"): ("D", "U", 1, 0),
        ("7", "D"): ("L", "R", 0, -1),
        ("7", "L"): ("D", "U", 1, 0),
        ("L", "U"): ("R", "L", 0, 1),
        ("L", "R"): ("U", "D", -1, 0),
        ("J", "U"): ("L", "R", 0, -1),
        ("J", "L"): ("U", "D", -1, 0)
    }
    iis, jjs = get_top_left(grid)
    n, m = len(grid), len(grid[0])
    res=[[""]*m for _ in range(n)]
    res[iis][jjs]="DR"
    iin, jjn = iis, jjs+1
    flow_from="L"
    while not res[iin][jjn]:
        #print_flow(res)
        flow_to, flow_from_new, di, dj = flow_mapping[(grid[iin][jjn], flow_from)]
        res[iin][jjn]=f"{flow_from}{flow_to}"
        iin, jjn = iin+di, jjn+dj
        flow_from=flow_from_new
    return res

fname="day10_input.txt"
grid=[]
with open(fname) as inputfile:
    for line in inputfile:
        grid.append(list(line.strip()))
n, m = len(grid), len(grid[0])
dist=[[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j]=="S":
            dist[i][j]=0
            iis, jjs = i, j
init_neighbs=[(iis, jjs+1), (iis, jjs-1), (iis+1, jjs), (iis-1, jjs)]
true_neighbs=[]
for iin, jjn in init_neighbs:
    if (iis, jjs) in get_neighbs(grid[iin][jjn], iin, jjn):
        true_neighbs.append((iin, jjn))
for char in "-|FLJ7":
    neighbcands=get_neighbs(char, iis, jjs)
    for neighb in neighbcands:
        if neighb not in true_neighbs:
            break
    else:
        grid[iis][jjs]=char
        break
queue=[(iis, jjs)]
i=0
res=0
visited=set()
while i<len(queue):
    ii, jj = queue[i]
    i+=1
    if (ii, jj) in visited:
        continue
    visited.add((ii, jj))
    neighbs=get_neighbs(grid[ii][jj], ii, jj)
    for iin, jjn in neighbs:
        if iin<0 or iin>=n or jjn<0 or jjn>=m or (iin, jjn) in visited:
            continue
        dist[iin][jjn]=dist[ii][jj]+1
        res=max(res, dist[iin][jjn])
        queue.append((iin, jjn))
print(res)
helper=[]
for i in range(n):
    row=[]
    for j in range(m):
        if dist[i][j]>=0:
            row.append(grid[i][j])
        else:
            row.append(".")
    helper.append(row)

flowdir=get_flow_direction(helper)
res=0
for i in range(n):
    for j in range(m):
        if helper[i][j]==".":
            if is_inside(i, j,helper, flowdir):
                res+=1

print(res)