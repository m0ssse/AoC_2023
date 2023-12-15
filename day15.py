def hash(s, k=17, N=256):
    res=0
    for char in s:
        res=((res+ord(char))*k)%N
    return res

def part1(fname):
    with open(fname) as inputfile:
        strs=inputfile.read().strip().split(",")
    res=0
    for s in strs:
        res+=hash(s)
    print(res)

def part2(fname):
    pass

def process(s, boxes):
    if "=" in s:
        add_lens(s, boxes)
    else:
        remove_lens(s, boxes)

def add_lens(s, boxes):
    """lenses are stored in boxes as tuples, where the first element is the label and the second is the focal length"""
    label, focalL = s.split("=")
    boxind=hash(label)
    for i in range(len(boxes[boxind])):
        if boxes[boxind][i][0]==label:
            boxes[boxind][i]=(label, focalL)
            return
    boxes[boxind].append((label, focalL))

def remove_lens(s, boxes):
    label=s[:-1]
    boxind=hash(label)
    for i in range(len(boxes[boxind])):
        if boxes[boxind][i][0]==label:
            boxes[boxind].pop(i)
            return
        
def get_focal_power(boxes):
    res=0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            res+=(i+1)*(j+1)*int(lens[1])
    return res

def part2(fname):
    boxes=[[] for _ in range(256)]
    with open(fname) as inputfile:
        strs=inputfile.read().strip().split(",")
    for s in strs:
        process(s, boxes)
    print(get_focal_power(boxes))

fname="day15_input.txt"
part2(fname)