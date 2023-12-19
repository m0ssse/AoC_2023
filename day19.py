def read_input(fname):
    with open(fname) as inputfile:
        workflow, parts = inputfile.read().split("\n\n")
    return workflow, parts

def parse_workflow(s):
    flows = s.split("\n")
    res={}
    for flow in flows:
        instructions_start = flow.find("{")
        name, instructions = flow[:instructions_start], flow[instructions_start+1:-1]
        res[name]=instructions.split(",")
    return res

def parse_parts(s):
    parts=s.split("\n")
    res=[]
    for part in parts:
        vals=part[1:-1].split(",")
        part={}
        for val in vals:
            param, value = val.split("=")
            part[param]=int(value)
        res.append(part)
    return res

def execute(part, workflow):
    for instruction in workflow:
        if ":" not in instruction:
            return instruction
        cond, dest = instruction.split(":")
        if eval(f"{part[cond[0]]}{cond[1]}{int(cond[2:])}"):
            return dest

def process_part(part, workflows):
    wf="in"
    while wf in workflows:
        wf=execute(part, workflows[wf])
    return sum(part.values()) if wf=="A" else 0

def part1(wf, parts):
    res=0
    for part in parts:
        res+=process_part(part, wf)
    return res

def total_through_workflow(population, workflows, wf):
    res=0
    for rule in workflows[wf]:
        if ":" not in rule:
            if rule=="A":
                res+=count_population(population)
                return res
            elif rule=="R":
                return res
            else:
                res+=total_through_workflow(population, workflows, rule)
                return res
        cond, dest = rule.split(":")
        acc, population = filter_pop(population, cond)
        if count_population(acc):
            if dest=="A":
                res+=count_population(acc)
            elif dest!="R":
                res+=total_through_workflow(acc, workflows, dest)
        if not count_population(population):
            return res
        

def part2(wf, l=1, u=4000):
    population={"x": [l, u], "m": [l, u], "a": [l, u], "s": [l, u]}
    return total_through_workflow(population, wf, "in")

def count_population(population):
    res=1
    for l, u in population.values():
        if u<l:
            return 0
        res*=(u-l+1)
    return res

def filter_pop(population, condition):
    accepted, rejected = {}, {}
    condkey, oper, thresh = condition[0], condition[1], int(condition[2:])
    for key, val in population.items():
        if key!=condkey:
            accepted[key]=val[:]
            rejected[key]=val[:]
        else:
            if oper=="<":
                accepted[key]=[population[key][0], min(thresh-1, population[key][1])]
                rejected[key]=[max(thresh, population[key][0]), population[key][1]]
            elif oper==">":
                accepted[key]=[max(thresh+1, population[key][0]), population[key][1]]
                rejected[key]=[population[key][0], min(thresh, population[key][1])]
    return accepted, rejected


fname="day19_input.txt"
wf, parts = read_input(fname)
wf, parts=parse_workflow(wf), parse_parts(parts)
print(part1(wf, parts))
print(part2(wf))