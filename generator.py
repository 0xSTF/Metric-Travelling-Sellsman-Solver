from graph import *
import random

location_num = 50
r = random.uniform(0.3, 0.5)
home_num = r * location_num

location_list = []
for i in range(location_num):
    location_list.append(i)

g = graph()
for location in location_list:
    g.addVertex(location_list)

for i in range(len(location_list)):
    for j in range(len(location_list)):
        if i != j:
            indicator = random.random()
            w = random.randint(6, 10)
            if indicator <= 0.3:
                g.addEdge(i, j, w)
    if len(g.getVertex(i).getNeighbor()) == 0:
        w = random.randint(6, 10)
        e = random.randint(0, location_num)
        g.addEdge(i, e, w)

home_list = []
while len(home_list) < home_num:
    v = random.randint(0, home_num)
    if not(v in home_list):
        home_list.append(v)

for loc in g:
    print(loc.value)
for loc in location_list:
    print(loc)
for h in home_list:
    print(h)

#writing to input.in

