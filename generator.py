from graph import *
import random

location_num = 200
r = random.uniform(0.3, 0.5)
home_num = round(r * location_num)

location_list = []
for i in range(location_num):
    location_list.append(i)

g = Graph()
for location in location_list:
    g.addVertex(location)

for i in range(len(location_list)):
    for j in range(len(location_list)):
        if i != j:
            indicator = random.random()
            w = random.randint(1001, 2000)
            if indicator <= 0.1:
                g.addEdge(i, j, w)
    if len(g.getVertex(i).getNeighbor()) == 0:
        w = random.randint(1001, 2000)
        e = random.randint(0, location_num)
        g.addEdge(i, e, w)

home_list = []
while len(home_list) < home_num:
    v = random.randint(0, home_num)
    if not(v in home_list):
        home_list.append(v)

print(g)
print(location_list)
print(home_num)
print(len(home_list))
print(home_list)

file = open("inputs/200.in", "w")
file.write(str(location_num)+"\n")
file.write(str(home_num)+"\n")
file.writelines(["%s " % loc for loc in location_list])
file.write("\n")
file.writelines(["%s " % h for h in home_list])
file.write("\n")
file.write("0" + "\n")
for loc1 in location_list:
    for loc2 in location_list:
        file.write(str(g.getEdgelen(loc1, loc2)) + " ")
    file.write("\n")

