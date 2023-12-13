def check_row_pattern(s, i):
    ii=i+1
    n=len(s)
    while i>=0 and ii<=n-1:
        if s[i]!=s[ii]:
            return False
        i-=1
        ii+=1
    return True

def find_all_row_patterns(s):
    res=[]
    n=len(s)
    for i in range(n-1):
        if check_row_pattern(s, i):
            res.append(i)
    return res

def transpose(s):
    res=[]
    n, m = len(s), len(s[0])
    for j in range(m):
        newrow=[]
        for i in range(n):
            newrow.append(s[i][j])
        res.append("".join(newrow))
    return res

def find_score(pattern):
    n, m=len(pattern), len(pattern[0])
    for i in range(n-1):
        if check_row_pattern(pattern, i):
            return 100*(i+1), i, -1
    pattern=transpose(pattern)
    for i in range(m-1):
        if check_row_pattern(pattern, i):
            return i+1, -1, i
    return 0, -1, -1

def score(i, j):
    return 100*(i+1)+j+1, i, j

def find_fixed_score(pattern):
    _, ii, jj = find_score(pattern)
    n, m = len(pattern), len(pattern[0])
    for i in range(n):
        for j in range(m):
            newpat=change(pattern, i, j)
            rowpats=find_all_row_patterns(newpat)
            for iii in rowpats:
                if ii!=iii:
                    return score(iii, -1)
            newpat=transpose(newpat)
            colpats=find_all_row_patterns(newpat)
            for jjj in colpats:
                if jjj!=jj:
                    return score(-1, jjj)


def change(pattern, i, j):
    pattern=[list(row) for row in pattern]
    pattern[i][j]="#" if pattern[i][j]=="." else "."
    return ["".join(row) for row in pattern]

def part1(patterns):
    res=0
    for pattern in patterns:
        res+=find_score(pattern)[0]
    print(res)

def part2(patterns):
    res=0
    for pattern in patterns:
        res+=find_fixed_score(pattern)[0]
    print(res)

fname="day13_input.txt"
with open(fname) as inputfile:
    patterns=[pattern.split("\n") for pattern in inputfile.read().split("\n\n")]
part1(patterns)
part2(patterns)