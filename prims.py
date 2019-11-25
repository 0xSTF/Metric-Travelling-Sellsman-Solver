from graph import *
from heapdict import *
import sys
def prims(g, starting_car_location):

    return

def dijsktra(g, src, unvisited_homes):
    edgeTo = {}
    distTo = heapdict()
    for node in g.vet_list:
        distTo[node] = sys.maxsize
    distTo[src] = 0
    edgeTo[src] = None
    v = src
    while distTo.peekitem()[0] not in unvisited_homes:
        g.getVertex()


if __name__ == '__main__':
    hd = heapdict()
    hd["1"] = sys.maxsize
    hd["2"] = 2
    hd["2"] = 0.5
    print("3" in hd)
    print(hd.peekitem()[0])
    print(hd.popitem())
    print(len(hd))
