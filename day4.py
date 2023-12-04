def winning_numbers(line):
    winning, numbers = line.strip().split("|")
    winning=set(int(x) for x in winning.split())
    numbers=set(int(x) for x in numbers.split())
    return len(winning.intersection(numbers))

def part1(fname):
    res=0
    with open(fname) as inputfile:
        for line in inputfile:
            ind=line.find(":")
            val=winning_numbers(line[ind+1:])
            if val:
                res+=2**(val-1)
        return res
    
def part2(fname):
    with open(fname) as inputfile:
        lines=inputfile.readlines()
    res=[1]*len(lines)
    for i, line in enumerate(lines):
        ind=line.find(":")
        val=winning_numbers(line.strip()[ind+1:])
        for j in range(i+1,i+1+val):
            res[j]+=res[i]
    return sum(res)
    
fname="day4_input.txt"
print(part2(fname))
