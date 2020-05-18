from Routenetwork import Routenetwork
from preprocess import init,distanceList
from Astar import Astar
from Latlong import ShowNodesOnMap

data=init()
nodes=data[0]
edges=data[1]
nodedict=data[2]

g=Routenetwork()
for item in edges:
    g.addEdge(item)

g_edges = g.getEdges()
distances = distanceList(nodes,nodedict, g_edges)
for items in nodes:
    distances[(items,items)]=0
start='Birla Institute of Technology Hyderabad'
end='RGIA'

path = Astar(g,nodedict,distances,start,end)

print('Final Route :')
print('****Start****')
for item in path:
    print (item)
print('****End****')
ShowNodesOnMap(path,nodedict)
