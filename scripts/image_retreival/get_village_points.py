from shapely.geometry import Polygon, Point, MultiPolygon, LineString, MultiLineString
import numpy as np
from urllib import request
from urllib import error
from io import BytesIO
import json
from tqdm import tqdm
import os
import time
from scipy.spatial import distance

def get_points(province, district, subdist, village, points, key): 
    vill_points = [] 
    village_list = get_village_lists(province, district, subdist, village)

    for lat, lng in tqdm(points, 'get village points'): 
        nearVill = knn(village_list, lat, lng)
        if nearVill == village:
            location = str(lat)+','+str(lng) 
            baseMetaUrl = "https://maps.googleapis.com/maps/api/streetview/metadata" 
            metaUrl = baseMetaUrl+"?location="+location+"&key="+key
            requestMeta = request.urlopen(metaUrl)    
            metaJson = json.loads(requestMeta.read().decode('utf8')) 
            if metaJson["status"] == 'OK': 
                vill_points.append([metaJson["location"]["lat"], metaJson["location"]["lng"]]) 
    print('village points: '+str(len(vill_points))+' points')

    return vill_points
     
def get_village_lists(province, district, subdist, village):
    village_list = []
    with open('../geojson/village.geojson') as F: 
        villages = json.load(F)

    for feature in villages["features"]: 
        prop = feature['properties']
        if str(prop['PRV_NAME'])==province and str(prop['AMP_NAME']) == district and str(prop['TAM_NAME']) == subdist:  
            temp = {
                'Village':prop['NAME'],
                'Coordinate':feature['geometry']['coordinates']
            }
            village_list.append(temp)  
    return village_list 

def knn(village_list, lat, lng): 
    dst = {} 
    for vill in village_list: 
        a = (lat,lng) 
        b = (vill["Coordinate"][1],vill["Coordinate"][0]) 
        dst[vill["Village"]] = distance.euclidean(a,b) 
    return min(dst, key=lambda k: dst[k])