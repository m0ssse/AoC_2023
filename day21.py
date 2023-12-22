def part1(grid, i, j, N):
    dist=bfs(grid, i, j)
    res=0
    for d in dist.values():
        if d<=N and d%2==0:
            res+=1
    return res

def bfs(grid, i, j):
    n=len(grid)
    dist={(i, j): 0}
    queue=[(i, j)]
    k=0
    while k<len(queue):
        ii, jj = queue[k]
        for iin, jjn in [(ii+1, jj), (ii-1, jj), (ii, jj+1), (ii, jj-1)]:
            if iin<0 or iin>=n or jjn<0 or jjn>=n or grid[iin][jjn]=="#" or (iin, jjn) in dist:
                continue
            dist[(iin, jjn)]=dist[(ii, jj)]+1
            queue.append((iin, jjn))
        k+=1
    return dist

def print_grid(grid, dist):
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j]=="#":
                print("#", end="")
            elif (i, j) in dist and dist[(i, j)]%2==0:
                print("O", end="")
            else:
                print(".", end="")
        print()

def read_input(fname):
    grid=[]
    starti=-1
    with open(fname) as inputfile:
        for i, line in enumerate(inputfile):
            if starti==-1 and "S" in line:
                starti, startj = i, line.find("S")
            grid.append(line.strip())
    return grid, starti, startj

def reachable_nodes_per_step_count(distances):
    res={}
    for node, dist in distances.items():
        if dist not in res:
            res[dist]=set()
        res[dist].add(node)
    return res

def find_reachables(stats, N):
    res=set()
    parity=N%2
    N=min(N, max(stats))
    for i in range(N+1):
        if i%2==parity:
            res=res.union(stats[i])
    return res


def part2(grid, i, j, N):
    """
    timanttikuvio:
    timantin nurkkia kannattaa lähteä tutkimaan nurkista, muita kannattaa lähteä keskeltä reunaa, koska kuvion reunojen keskeltä pääsee suoraan läpi
    """

    #lasketaan timantin koko
    n=len(grid)
    a=N//n
    if a%2==1:
        max_even_layer=a-1
        max_odd_layer=a-2
    else:
        max_odd_layer=a-1
        max_even_layer=a-2
    even_layers=max_even_layer//2
    odd_layers=(1+max_odd_layer)//2
    #parittomat kerrokset 1, 3, 5, jne näissä on 4, 12, 20 jne ruutua->yhteensä 4*odd_layers**2
    odd_squares=4*odd_layers**2
    #parilliset kerrokset 2, 4, 6 jne. näissä on 8, 16, 20.. kerrosta =8*(1+2+3...+even_layers)=4*(even_layers)*(even_layers+1)

    dist_start, dist_NW, dist_SW, dist_NE, dist_SE=bfs(grid, i, j), bfs(grid, 0, 0), bfs(grid, n-1, 0), bfs(grid, 0, n-1), bfs(grid, n-1, n-1)
    dist_N, dist_W, dist_S, dist_E=bfs(grid, 0, n//2), bfs(grid, n//2, 0), bfs(grid, n-1, n//2), bfs(grid, n//2, n-1)
    stats_start=reachable_nodes_per_step_count(dist_start)
    stats_NW=reachable_nodes_per_step_count(dist_NW)
    stats_SW=reachable_nodes_per_step_count(dist_SW)
    stats_NE=reachable_nodes_per_step_count(dist_NE)
    stats_SE=reachable_nodes_per_step_count(dist_SE)
    stats_N=reachable_nodes_per_step_count(dist_N)
    stats_W=reachable_nodes_per_step_count(dist_W)
    stats_S=reachable_nodes_per_step_count(dist_S)
    stats_E=reachable_nodes_per_step_count(dist_E)

    max_steps_needed=max(max(stats_start), max(stats_NW), max(stats_NE), max(stats_SW), max(stats_SE), max(stats_N), max(stats_E), max(stats_S), max(stats_W))
    if max_steps_needed%2==1:
        max_needed_even, max_needed_odd = max_steps_needed+1, max_steps_needed
    else:
        max_needed_even, max_needed_odd = max_steps_needed, max_steps_needed+1
    res=0
    return res

fname="day21_input.txt"
#fname="day21_test.txt"
N1=64
grid, i, j = read_input(fname)
print(i, j)
#print(part1(grid, i, j, N1))
#N2=26501365
N2=5000
print(part2(grid, i, j, N2))