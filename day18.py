def read_input1(fname):
    res=[]
    with open(fname) as inputfile:
        for line in inputfile:
            dir, N, _ = line.strip().split()
            res.append((dir, int(N)))
    return res

def read_input2(fname):
    res=[]
    with open(fname) as inputfile:
        for line in inputfile:
            _, _, code = line.strip().split()
            N, dir = int(code[2:-2], 16), "RDLU"[int(code[-2])]
            res.append((dir, N))
    return res

def get_corners(instructions):
    directions={"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}
    corners=[]
    i=j=0
    for dir, N in instructions:
        di, dj = directions[dir]
        i+=di*N
        j+=dj*N
        corners.append((i, j, N))
    return corners

def calculate_area(corners):
    N=len(corners)
    res=0
    edgepts=0
    for i in range(N):
        x1, x2, y1, y2 = corners[i][0], corners[(i+1)%N][0], corners[i][1], corners[(i+1)%N][1]
        res+=(y1+y2)*(x1-x2)
        edgepts+=corners[i][-1]
    return (abs(res)+edgepts+2)//2

fname="day18_input.txt"
print(calculate_area(get_corners(read_input1(fname))))
print(calculate_area(get_corners(read_input2(fname))))