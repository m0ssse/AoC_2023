class Solution:
    def solve(self, grid):
        self.res=0
        n, m = len(grid), len(grid[0])
        visited=set()
        visited.add((0, 1))
        self.res=0
        self.junctions=self.find_junctions(grid)
        self.junction_distances=self.get_junction_distances(grid, n, m)
        self.dfs((0, 1), visited, 0, (n-1, m-2))
        return self.res
    
    def dfs(self, node, visited, totaldist, target):
        if node==target:
            self.res=max(self.res, totaldist)
            return
        for ii, jj, d in self.junction_distances[node]:
            if (ii, jj) in visited:
                continue
            visited.add((ii, jj))
            self.dfs((ii, jj), visited, totaldist+d, target)
            visited.remove((ii, jj))
    
    def get_neighbs(self, grid, i, j, n, m):
        if grid[i][j]=="#":
            return []
        if grid[i][j]==">":
            return [(i, j+1)]
        elif grid[i][j]=="v":
            return [(i+1, j)]
        elif grid[i][j]=="<":
            return [(i, j-1)]
        elif grid[i][j]=="^":
            return [(i-1, j)]
        elif grid[i][j]==".":
            neighblist=[(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        res=[]
        for ii, jj in neighblist:
            if ii<0 or ii>=n or jj<0 or jj>=m or grid[ii][jj]=="#":
                continue
            res.append((ii, jj))
        return res

    def find_junctions(self, grid):
        junctionlist=[(0, 1)]
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if len(self.get_neighbs(grid, i, j, n, m))>=3:
                    junctionlist.append((i, j))
        junctionlist.append((n-1, m-2))
        return junctionlist
    
    def get_junction_distances(self, grid, n, m):
        junction_distances={node: [] for node in self.junctions}
        for node in self.junctions:
            stack=[(node, 0)]
            visited={node}
            while stack:
                (i, j), dist = stack.pop()
                if (i, j)!=node and (i, j) in junction_distances:
                    junction_distances[node].append((i, j, dist))
                    continue
                for ii, jj in self.get_neighbs(grid, i, j, n, m):
                    if (ii, jj) in visited:
                        continue
                    visited.add((ii, jj))
                    stack.append(((ii, jj), dist+1))
        return junction_distances

def read_input1(fname):
    with open(fname) as inputfile:
        return inputfile.read().split("\n")

def read_input2(fname):
    res=[]
    with open(fname) as inputfile:
        for line in inputfile:
            line=line.strip().replace(">", ".").replace("v", ".").replace("<", ".").replace("^", ".")
            res.append(line)
    return res

fname="day23_input.txt"
grid=read_input2(fname)
sol=Solution()
print(sol.solve(grid))