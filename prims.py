from graph import *
from heapdict import *
import sys


def prims(g, starting_car_location):
    return


def dijsktra(g, src, unvisited_homes):      # src: vertex id, unvisited_homes: list of vertices ids
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
    hd = heapdict()
    hd["1"] = sys.maxsize
    hd["2"] = 2
    hd["2"] = 0.5
    print("3" in hd)
    print(hd["2"])
    print(hd.peekitem()[0])
    print(hd.popitem())
    print(len(hd))
