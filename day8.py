from math import lcm

class Graph:
    def __init__(self):
        self.neighbs={}

    def add_node(self, node):
        self.neighbs[node]=[]

    def add_edge(self, node, dest):
        if node not in self.neighbs:
            self.add_node(node)
        self.neighbs[node].append(dest)

class Solution:
    def __init__(self, fname):
        self.graph=Graph()
        self.read_input_file(fname)

    def read_input_file(self, fname):
        self.startnodes=[]
        self.targetnodes=[]
        with open(fname) as inputfile:
            for i, line in enumerate(inputfile):
                if i==0:
                    self.instructions=line.strip()
                elif i>=2:
                    node, neighbs = line.strip().split(" = ")
                    if node.endswith("A"):
                        self.startnodes.append(node)
                    if node.endswith("Z"):
                        self.targetnodes.append(node)
                    neighbs=neighbs[1:-1].split(", ")
                    for neighb in neighbs:
                        self.graph.add_edge(node, neighb)

    def count_steps(self, startnode, targetnodes):
        i=0
        currnode=startnode
        N=len(self.instructions)
        while currnode not in targetnodes:
            if self.instructions[i%N]=="L":
                currnode=self.graph.neighbs[currnode][0]
            else:
                currnode=self.graph.neighbs[currnode][1]
            i+=1
        return i
    
if __name__=="__main__":
    fname="day8_input.txt"
    sol=Solution(fname)
    periods={}
    for node in sol.startnodes:
        periods[node]=sol.count_steps(node, sol.targetnodes)
    print(periods["AAA"])
    print(lcm(*list(periods.values())))