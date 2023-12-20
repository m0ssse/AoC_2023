class Module:
    def __init__(self, label):
        self.outputs=[]
        self.label=label

    def add_output(self, dest):
        self.outputs.append(dest)

    def __str__(self):
        res=f"{self.label}\noutputs:\n"
        for output in self.outputs:
            res+=f"{output.label}\n"
        return res
    
class FlipFlop(Module):
    def __init__(self, label):
        super().__init__(label)
        self.on=0
        self.type="ff"

    def receive(self, pulse):
        res=[]
        _, _, type = pulse
        if type==1:
            return res
        self.on=1-self.on
        for dest in self.outputs:
            res.append((self, dest, self.on))
        return res

class Conjuction(Module):
    def __init__(self, label):
        super().__init__(label)
        self.memory={}
        self.type="con"

    def receive(self, pulse):
        sender, _, type = pulse
        self.memory[sender.label]=type
        for prevtype in self.memory.values():
            if prevtype==0:
                return [(self, dest, 1) for dest in self.outputs]
        return [(self, dest, 0) for dest in self.outputs]

class Broadcast(Module):
    def __init__(self, label):
        super().__init__(label)
        self.type="bc"

    def receive(self, pulse):
        _, _, type = pulse
        return [(self, dest, type) for dest in self.outputs]
    
class Button(Module):
    def __init__(self, label):
        super().__init__(label)
        self.type="but"
    
    def send(self):
        return [(self, dest, 0) for dest in self.outputs]
    
class Output(Module):
    def __init__(self, label):
        super().__init__(label)
        self.type="op"
    
    def receive(self, pulse):
        return []
    
def read_input(fname):
    res={}
    with open(fname) as inputfile:
        lines=inputfile.readlines()
    for line in lines:
        source, _ = line.strip().split(" -> ")
        if source=="broadcaster":
            res[source]=Broadcast(source)
        elif source[0]=="%":
            label=source[1:]
            res[label]=FlipFlop(label)
        else:
            label=source[1:]
            res[label]=Conjuction(label)
    for line in lines:
        source, outputs = line.strip().split(" -> ")
        if source=="broadcaster":
            label=source
        else:
            label=source[1:]
        outputs=outputs.split(", ")
        for dest in outputs:
            if dest not in res:
                res[dest]=Output(dest)
            if res[dest].type=="con":
                res[dest].memory[label]=0
            res[label].add_output(res[dest])
    return res

def part1(button, N):
    res=[0, 0]
    for _ in range(N):
        queue=[]
        out=button.send()
        for pulse in out:
            queue.append(pulse)
        i=0
        while i<len(queue):
            pulse=queue[i]
            source, dest, type=pulse
            output=dest.receive(pulse)
            for pulse in output:
                queue.append(pulse)
            i+=1
        for _, _, type in queue:
            res[type]+=1
    print(res[0]*res[1])

fname="day20_input.txt"
modules=read_input(fname)
button=Button("button")
button.add_output(modules["broadcaster"])
N=1000
part1(button, N)