from enum import Enum
from collections import Collection
from typing import OrderedDict

class State(Enum):
    unvisited = 1
    visited = 2
    visiting = 3

class Node:
    def __init__(self, num):
        self.num = num
        self.visitState = State.unvisited
        self.adjacent = OrderedDict()

class Graph:
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

        self.nodes[src].adjacent[self.nodes[dest]] = weight

    def __str__(self):
        output = ""

        for node in self.nodes:
            if self.nodes.get(node).visitState != State.visited:
                output += "Node: " + str(node)

                for neighbor in self.nodes[node].adjacent:
                    output += " -> Node: " + str(neighbor.num)
                    neighbor.visitState = State.visited
        return output

graph = Graph()
graph.addEdge(2, 5)
print(graph)
