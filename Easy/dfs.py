from enum import Enum
from collections import OrderedDict

class State(Enum):
    visited = 1
    unvisted = 2
    visiting = 3

class Node:
    def __init__(self, num):
        self.num = num
        self.visitState = State.unvisted
        self.connectedTo = OrderedDict()

class Graph():
    def __init__(self):
        self.nodes = OrderedDict()

    def addNode(self, num):
        node = Node(num)
        self.nodes[num] = node
        return node
    
    def addEdge(self, src, dest, weight=0):
        if src not in self.nodes:
            node = Node(src)
            self.nodes[src] = node

        if dest not in self.nodes:
            node = Node(dest)
            self.nodes[dest] = node
        
        self.nodes[src].connectedTo[self.nodes[dest]] = weight


    def __str__(self):
        output = ""

        for node in self.nodes:
            nodeState = self.nodes[node].visitState
            if nodeState == State.unvisted:
                print(self.nodes[node].num)
                nodeState = State.visiting
                for adjacentNode in self.nodes[node].connectedTo:
                    print(adjacentNode.num)
                    adjacentNode.visitState = State.visited
            nodeState = State.visited


            
        return ""


graph = Graph()
graph.addEdge("A","B")
graph.addEdge("A","C")
graph.addEdge("C","D")
graph.addEdge("C","E")
graph.addEdge("D","F")
graph.addEdge("B","D")
graph.addEdge("E","F")
graph.addEdge("F","A")

def dfs(node):
    node.visitState = State.visiting
    print(node.num)

    for adjacentNode in node.connectedTo:
        if adjacentNode.visitState == State.unvisted:
            dfs(adjacentNode)
    node.visitState = State.visited

dfs(graph.nodes.get('A'))
