import csv
import urllib.parse
import requests
import json 
import gmplot


key ="Ak0BvGTJ4dDGEHQIcSL8lbjb_1AOW7w01T2SZa39s5sb4XYjau1uS01XAuusuRBF"

nodes = []
edges = []
places = "data/places.csv"
conn = "data/edges.csv"

def geoloc(item):
    sendurl='http://dev.virtualearth.net/REST/v1/Locations?query='+item+'&key='+key
    r=requests.get(sendurl)
    try:
        j=json.loads(r.text)
        try:
            loc = j['resourceSets'][0]['resources'][0]['geocodePoints'][0]['coordinates']
            return(tuple(loc))
        except ValueError:
            print("Wrong")
    except ValueError:
        print("Wrong")
    return []

def getjson(nodedict, start=False, dest=False):
    data_origin=[]
    data_dest=[]
    jsondata = {}
    
    temp={}
    temp['latitude']=nodedict[dest][0]
    temp['longitude']= nodedict[dest][1]
    data_dest.append(temp)

    temp={}
    temp['latitude']=nodedict[start][0]
    temp['longitude']=nodedict[start][1]
    data_origin.append(temp)

    jsondata['origins']=data_origin
    jsondata['destinations']=data_dest
    jsondata['travelMode']='driving'
    jsondata=json.dumps(jsondata)
    return jsondata

def distanceMatrix(nodedict, start=False,dest=False):
    sendurl='https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?key='+key
    jsondata=getjson(nodedict,start,dest)   
    r = requests.post(url=sendurl, data=jsondata)
    try:
        j=json.loads(r.text)
        distances=[]
        try:
            loc = j['resourceSets'][0]['resources'][0]['results']
            for item in loc:
                distances.append(item['travelDuration'])
                print(distances)
            return(((distances)))
        except ValueError:
            print("Wrong")
    except ValueError:
        print("Wrong")

def openFiles():
    with open(places, encoding='utf-8-sig') as fileplace:
        placereader=csv.reader(fileplace)

        for place in placereader:
            place=''.join(place)
            nodes.append((place))

    with open(conn, encoding='utf-8-sig') as fileconn:
        connreader=csv.reader(fileconn)
        for edge in connreader:
            edges.append(edge)

    return (nodes,edges)

def ShowNodesOnMap(path, nodedict):
    latitudes=[]
    longitudes=[]
    lat = []
    long = []

    gmap = gmplot.GoogleMapPlotter(17.41744041442871, 78.49571228027344,11.7) 


    for items in edges:
        lat.append(nodedict[items[0]][0])
        lat.append(nodedict[items[1]][0])
        long.append(nodedict[items[0]][1])
        long.append(nodedict[items[1]][1])


    gmap.plot(lat,long,'black',edge_width = 2.5)

   

    for items in path:
        latitudes.append(nodedict[items][0])
        longitudes.append(nodedict[items][1]) 
        gmap.marker(nodedict[items][0],nodedict[items][1],'green', title = items)

    for items in nodes:
        if not items in path:
            gmap.marker(nodedict[items][0],nodedict[items][1],'blue',title = items)
        elif items == 'Birla Institute of Technology Hyderabad':
            gmap.marker(nodedict[items][0],nodedict[items][1],'red',title = items)
        elif items == 'RGIA':
            gmap.marker(nodedict[items][0],nodedict[items][1],'red',title = items)


    gmap.plot(latitudes,longitudes,'green', edge_width=5)
    gmap.draw('/home/jathin/Desktop/FinalAI/Q3_final/map.html')
    
