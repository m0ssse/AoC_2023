class Beam:
    reflections={"/": {(1, 0): (0, -1), (0, -1): (1, 0), (-1, 0): (0, 1), (0, 1): (-1, 0)}, "\\":{(-1, 0): (0, -1), (0, 1): (1, 0), (1, 0): (0, 1), (0, -1): (-1, 0)}}

    def __init__(self, i, j, di, dj):
        self.i=i
        self.j=j
        self.di=di
        self.dj=dj
    
    def move(self):
        self.i+=self.di
        self.j+=self.dj

    def pos(self):
        return self.i, self.j
    
    def vel(self):
        return self.di, self.dj

    def turn(self, char):
        self.di, self.dj = Beam.reflections[char][(self.di, self.dj)]

def simulate(beam, grid):
    n, m = len(grid), len(grid[0])
    #visited tiles are saved as a dictionary containing the coordinates and a set of directions that a light beam has traveled at a particular point
    #it is not enough to check whether a previous light beam has been at a particular point because beams traveling in different direction may energise
    #different tiles
    visited={}
    stack=[beam]
    i, j = beam.pos()
    di, dj = beam.vel()
    while stack:
        beam=stack[-1]
        beam.move()
        i, j = beam.pos()
        di, dj = beam.vel()
        if i<0 or i>=n or j<0 or j>=m:
            stack.pop()
            continue
        if (i, j) in visited and (di, dj) in visited[(i, j)]:
            stack.pop()
            continue
        if (i, j) not in visited:
            visited[(i, j)]=set()
        visited[(i, j)].add((di, dj))
        if grid[i][j] in "\\/":
            beam.turn(grid[i][j])
        elif grid[i][j]=="-":
            if di:
                stack.pop()
                stack.append(Beam(i, j, 0, 1))
                stack.append(Beam(i, j, 0, -1))
        elif grid[i][j]=="|":
            if dj:
                stack.pop()
                stack.append(Beam(i, j, 1, 0))
                stack.append(Beam(i, j, -1, 0))
    return len(visited)

def part1(fname):
    beam=Beam(0, -1, 0, 1)
    with open(fname) as inputfile:
        grid=inputfile.read().split("\n")
    print(simulate(beam, grid))

def part2(fname):
    with open(fname) as inputfile:
        grid=inputfile.read().split("\n")
    res=0
    n, m = len(grid), len(grid[0])
    for i in range(n):
        res=max(res, simulate(Beam(i, -1, 0, 1), grid))
        res=max(res, simulate(Beam(i, m, 0, -1), grid))
    for j in range(m):
        res=max(res, simulate(Beam(-1, j, 1, 0), grid))
        res=max(res, simulate(Beam(n, j, -1, 0), grid))
    print(res)

fname="day16_input.txt"
part1(fname)
part2(fname)
