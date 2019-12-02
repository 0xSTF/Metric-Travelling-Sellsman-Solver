class Vertex(object):
    def __init__(self, node):
        self.id = node
        self.neighbor = {}      # key: vertex, value: weight
        self.home = False
        self.dropOff = False

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id) + " " + str(self.home) + " " + str(self.neighbor.values())

    def getID(self):
        return self.id

    def isLeaf(self):
        return len(self.neighbor) == 1

    def makeHome(self):
        self.home = True

    def isHome(self):
        return self.home

    def makeDropOff(self):
        self.dropOff = True

    def isDropOff(self):
        return self.dropOff

    def addNeighbor(self, node, weight):
        for i in self.neighbor.keys():
            if i == node:
                return
        self.neighbor[node] = weight
        node.neighbor[self] = weight

    def getNeighbor(self):
        return self.neighbor

class Graph(object):
    def __init__(self):
        self.vet_list = {}      # key: vertex id, value: vertex
        self.size = 0

    def addVertex(self, node):
        if node in self.vet_list.keys():
            return
        else:
            self.size += 1
            new = Vertex(node)
            self.vet_list[node] = new
            return new

    def getVertex(self, node):
        if node not in self.vet_list.keys():
            return 0
        return self.vet_list[node]

    def getVertexNeighbor(self, node):
        neighbors = self.getVertex(node).getNeighbor().keys()
        return [i.id for i in neighbors]

    def addEdge(self, n1, n2, weight):
        if n1 != n2:
            if n1 not in self.vet_list:
                self.addVertex(n1)
            if n2 not in self.vet_list:
                self.addVertex(n2)
            self.vet_list[n1].addNeighbor(self.getVertex(n2), weight)

    def getEdgelen(self, n1, n2):
        if n1 != n2:
            if self.getVertex(n2) not in self.getVertex(n1).getNeighbor().keys():
                return "x"
            else:
                return self.getVertex(n1).getNeighbor()[self.getVertex(n2)]
        else:
            return "x"

    def deleteLeaf(self, node):
        """
        recursively prune leaves until get to a non-leaf or TA's home
        return its id
        """
        v = self.getVertex(node)
        if len(v.getNeighbor()) == 0:
            return v.getID()
        for key in v.getNeighbor().keys():
            incident_v = key
        # incident_v = self.getVertex(v.getNeighbor().keys()[0])
        incident_v.getNeighbor().pop(v)
        self.vet_list.pop(node)
        self.size -= 1
        if incident_v.isLeaf() and (not incident_v.isHome()) and (not incident_v.isDropOff):
            return self.deleteLeaf(incident_v.getID())
        else:
            incident_v.makeDropOff()
            return incident_v.getID()

    def __str__(self):
        print(self.size)
        return str(self.vet_list)
