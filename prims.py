from graph import *
from heapdict import *
import sys


def prims(g, starting_car_location):
    mst = Graph()
    visited = []
    unvisited_homes = [node for node in g.vet_list.keys() if g.getVertex(node).isHome()]
    distTo = heapdict()
    edgeTo = {}
    mst.addVertex(starting_car_location)
    visited.append(starting_car_location)
    if g.getVertex(starting_car_location).isHome():
        mst.getVertex(starting_car_location).makeHome()
        unvisited_homes.remove(starting_car_location)
    for home in unvisited_homes:
        distTo[home] = sys.maxsize
        edgeTo[home] = None
    while len(unvisited_homes) != 0:
        for node in visited:
            path, total_weight = dijsktra(g, node, unvisited_homes)
            curr_home = path[0]
            if total_weight < distTo[curr_home]:
                distTo[curr_home] = total_weight
                edgeTo[curr_home] = path
        v = distTo.popitem()[0]
        unvisited_homes.remove(v)
        prev = edgeTo[v].pop(0)
        for vertex in edgeTo[v]:
            if prev not in visited:
                visited.append(prev)
            weight = g.getEdgelen(prev, vertex)
            mst.addEdge(prev, vertex, weight)
            prev = vertex
    return mst


def dijsktra(g, src, unvisited_homes):  # src: vertex id, unvisited_homes: list of vertices ids
    edgeTo = {}
    distTo = heapdict()
    visited = {}
    for node in g.vet_list.keys():
        distTo[node] = sys.maxsize
        visited[node] = False
    distTo[src] = 0
    edgeTo[src] = None
    visited[src] = True
    v = src
    while distTo.peekitem()[0] not in unvisited_homes:
        distTo.popitem()
        for i in g.getVertexNeighbor(v):
            if visited[i]:
                continue
            else:
                new_dist = distTo[v] + g.getEdgelen(v, i)
                if new_dist < distTo[i]:
                    distTo[i] = new_dist
                    edgeTo[i] = v
        v = distTo.peekitem()[0]
        visited[v] = True
    home = distTo.popitem()[0]
    path = []
    total_weight = 0
    while edgeTo[home] is not None:
        path.append(home)
        total_weight += g.getEdgelen(home, edgeTo[home])
        home = edgeTo[home]
    path.append(home)
    return path, total_weight


if __name__ == '__main__':
    
