class Brick:
    def __init__(self, end1, end2, id):
        x1, y1, z1 = end1
        x2, y2, z2 = end2
        self.dx, self.dy, self.dz = x2-x1, y2-y1, z2-z1
        self.x, self.y, self.z = end1
        self.id=id
        self.supported_bricks=set()
        self.supporting_bricks=set()

    def get_coordinates(self):
        if self.dx:
            return [(x, self.y, self.z) for x in range(self.x, self.x+self.dx+1)]
        elif self.dy:
            return [(self.x, y, self.z) for y in range(self.y, self.y+self.dy+1)]
        elif self.dz:
            return [(self.x, self.y, z) for z in range(self.z, self.z+self.dz+1)]
        return [(self.x, self.y, self.z)]
    
    def __hash__(self):
        return hash(self.id)
    
    def __eq__(self, other):
        return self.id==other.id
    
    def __str__(self):
        res=f"brick {self.id}\nsupported by:\n"
        for brick in self.supporting_bricks:
            res+=f"{brick.id}\n"
        res+="supports:\n"
        for brick in self.supported_bricks:
            res+=f"{brick.id}\n"
        return res
    
def drop_brick(brick, occupied):
    if brick.z==1:
        return False
    brick.z-=1
    brick_has_to_stop=False
    for x, y, z in brick.get_coordinates():
        if (x, y, z) in occupied:
            brick_has_to_stop=True
            supporting_brick=occupied[(x, y, z)]
            supporting_brick.supported_bricks.add(brick)
            brick.supporting_bricks.add(supporting_brick)
    if brick_has_to_stop:
        brick.z+=1
        return False
    return True

def read_input(fname):
    brick_list=[]
    with open(fname) as inputfile:
        for i, line in enumerate(inputfile):
            end1, end2 = line.strip().split("~")
            end1=[int(x) for x in end1.split(",")]
            end2=[int(x) for x in end2.split(",")]
            brick_list.append((Brick(end1, end2, i)))
    return brick_list

def simulate(bricks):
    bricks_by_z_coordinate=sorted(bricks, key=lambda brick: brick.z)
    occupied_squares={} #keys=coordinates, values=bricks
    for brick in bricks_by_z_coordinate:
        while drop_brick(brick, occupied_squares):
            continue
        for x, y, z in brick.get_coordinates():
            occupied_squares[(x, y, z)]=brick

def solve(bricks):
    simulate(bricks)
    res1= []
    for brick in bricks:
        canDisintegrate=True
        for brick2 in brick.supported_bricks:
            if len(brick2.supporting_bricks)==1:
                canDisintegrate=False
        if canDisintegrate:
            res1.append(brick)
    res2=0
    for brick_to_disintegrate in bricks:
        helper=set()
        queue=[brick_to_disintegrate]
        helper.add(brick_to_disintegrate)
        i=0
        while i<len(queue):
            brick=queue[i]
            for brick2 in brick.supported_bricks:
                queue.append(brick2)
            for brick3 in brick.supporting_bricks:
                if brick3 not in helper:
                    break
            else:
                helper.add(brick)
            i+=1
        res2+=len(helper)-1
    print(res2)


fname="day22_input.txt"
bricks=read_input(fname)
solve(bricks)
