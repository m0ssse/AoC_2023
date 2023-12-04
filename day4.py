def winning_numbers(line):
    winning, numbers = line.strip().split("|")
    winning=set(int(x) for x in winning.split())
    numbers=set(int(x) for x in numbers.split())
    return len(winning.intersection(numbers))

def solve(fname):
    with open(fname) as inputfile:
        lines=inputfile.readlines()
    res1=0
    res2=[1]*len(lines)
    for i, line in enumerate(lines):
        ind=line.find(":")
        val=winning_numbers(line.strip()[ind+1:])
        if val:
            res1+=2**(val-1)
        for j in range(i+1, i+1+val):
            res2[j]+=res2[i]
    return res1, sum(res2)
    
fname="day4_input.txt"
print(solve(fname))