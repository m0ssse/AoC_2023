def predict(lines):
    lines[-1].append(0)
    for i in range(-2, -len(lines)-1, -1):
        lines[i].append(lines[i][-1]+lines[i+1][-1])

fname="day9_input.txt"
res=0
with open(fname) as inputfile:
    for line in inputfile:
        line=[int(x) for x in line.split()][::-1]
        diffs=[line]
        while True:
            if len(set(line))==1 and line[0]==0:
                predict(diffs)
                res+=diffs[0][-1]
                break
            line=[line[i]-line[i-1] for i in range(1, len(line))]
            diffs.append(line)
print(res)

