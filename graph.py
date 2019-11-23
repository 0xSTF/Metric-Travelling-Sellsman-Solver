class Vertex(object):
    def __init__(self, node):
        self.id = node
        self.neighbor = {}

    def addNeighbor(self, node, weight):
        self.neighbor[node] = weight
        node.neighbor[self] = weight

    def getNeighbor(self):
        return self.neighbor

class Graph(object):
    def __init__(self):
        self.vet_list = {}
        self.size = 0

    def addVertex(self, node):
        self.size += 1
        new = Vertex(node)
        self.vet_list[node] = new
        return new

    def getVertex(self, node):
        return self.vet_list[node]

    def addEdge(self, n1, n2, weight):
        if n1 != n2:
            if n1 not in self.vet_list:
                self.addVertext(n1)
            if n2 not in self.vet_list:
                self.addVertext(n2)
            self.vet_list[n1].addNeighbor(n1, n2, weight)

    def getEdgelen(self, n1, n2):
        if n1 != n2:
            if self.getVertex(n2) not in self.getVertex(n1).getNeighbor().keys:
                return "x"
            else:
                return self.getVertex(n1).getNeighbor()[self.getVertex(n2)]
        else:
            return "x"
