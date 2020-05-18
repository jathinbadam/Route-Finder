import urllib.parse
import json as JSON
from os import path
from Latlong import geoloc,openFiles,distanceMatrix
from Routenetwork import Routenetwork
import pickle


def nodeList(nodes):
    nodedict=dict()
    if not path.exists('/home/jathin/Desktop/FinalAI/Q3_final/dict.json'):
        for item in nodes:
            urllib.parse.quote(item)   
            nodedict[item]=geoloc(item)
 
        json = JSON.dumps(nodedict)
        f = open("/home/jathin/Desktop/FinalAI/Q3_final/dict.json","w")
        f.write(json)
        f.close()

    else:
        with open('/home/jathin/Desktop/FinalAI/Q3_final/dict.json', 'r') as f:
            nodedict=JSON.load(f)

    return nodedict

def distanceList(nodes, nodedict, g_edges):
    if not path.exists('/home/jathin/Desktop/FinalAI/Q3_final/distancesPickle'):
        distances={}
        for start,end in g_edges:
            print(start+'|')    
            print(end)
            matrix=distanceMatrix(nodedict, start, end)  
            t=(start,end)          
            distances[t]=matrix[0]
        
        for item in nodes:         
            if item=='RGIA':
                continue

            end = "RGIA"
            start=item
            matrix=distanceMatrix(nodedict, start, end)  
            t=(start,end)          
            distances[t]=matrix[0]
            matrix=distanceMatrix(nodedict, end, start)
            t=(end,start)          
            distances[t]=matrix[0]

        Databasefile = open('/home/jathin/Downloads/best-path-master/distancesPickle', 'wb')
        pickle.dump(distances, Databasefile)
        Databasefile.close()

    else:
        Databasefile = open('/home/jathin/Downloads/best-path-master/distancesPickle', 'rb')
        distances = pickle.load(Databasefile)
    
    return distances

def init():
    data=openFiles()
    nodes = data[0]
    edges = data[1]
    nodedict = nodeList(nodes)
    return (nodes, edges, nodedict)
