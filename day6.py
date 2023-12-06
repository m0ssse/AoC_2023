from math import sqrt, floor, ceil

def solve1(fname):
    res=1
    with open(fname) as inputfile:
        lines=[line.strip() for line in inputfile.readlines()]
    times=[int(x) for x in lines[0].split(":")[1].split()]
    dist=[int(x) for x in lines[1].split(":")[1].split()]
    for i, M in enumerate(times):
        res*=count_ways(M, dist[i])
    print(res)

def solve2(fname):
    with open(fname) as inputfile:
        lines=[line.strip() for line in inputfile.readlines()]
    times="".join([x for x in lines[0].split(":")[1].split()])
    dist="".join([x for x in lines[1].split(":")[1].split()])
    print(count_ways(int(times), int(dist)))


def count_ways(M, d):
    t1=ceil((M-sqrt(M**2-4*d))/2)
    if t1*(M-t1)==d:
        t1+=1
    t2=floor((M+sqrt(M**2-4*d))/2)
    if t2*(M-t2)==d:
        t2-=1
    return t2-t1+1

fname="day6_input.txt"
solve1(fname)
solve2(fname)