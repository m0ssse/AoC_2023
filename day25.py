import graphviz

def read_input(fname, edges_to_remove):
    graph={}
    with open(fname) as inputfile:
        for line in inputfile:
            node, neighbs = line.strip().split(": ")
            neighbs=neighbs.split()
            if node not in graph:
                graph[node]=[]
            for neighb in neighbs:
                if neighb not in graph:
                    graph[neighb]=[]
                if (node, neighb) in edges_to_remove or (neighb, node) in edges_to_remove:
                    continue
                graph[node].append(neighb)
                graph[neighb].append(node)
    return graph

def solve(graph):
    res=1
    visited=set()
    for node in graph:
        if node not in visited:
            stack=[node]
            compsize=0
            visited.add(node)
            while stack:
                currnode=stack.pop()
                compsize+=1
                for neighb in graph[currnode]:
                    if neighb not in visited:
                        visited.add(neighb)
                        stack.append(neighb)
            res*=compsize
    print(res)

def visualise(graph):
    mygraph=graphviz.Graph("connections", format="svg", engine="neato")
    for node in graph:
        mygraph.node(node)
    for node, neighbs in graph.items():
        for neighb in neighbs:
            mygraph.edge(node, neighb)
    mygraph.render(directory='doctest-output').replace('\\', '/')

fname="day25_input.txt"
edges_to_remove=[("nct", "kdk"), ("cvx", "tvj"), ("spx", "fsv")]
#fname="day25_test.txt"
#edges_to_remove=[("hfx", "pzl"), ("bvb", "cmg"), ("nvd", "jqt")]
graph=read_input(fname, edges_to_remove)
#visualise(graph)
solve(graph)
    