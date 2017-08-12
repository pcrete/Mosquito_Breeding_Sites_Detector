import csv 
import os 
import json 
from tqdm import tqdm 
import pandas as pd
from jsoncomment import JsonComment

def get_info(image_name): 
    info = image_name.replace('-','_').split('_') 
    return info[0] , info[1], info[3], info[4] 

def get_data(image_name): 
    info = image_name.replace('-','_').split('_') 
    return info[2], info[5], info[6] 

def get_coor(image_name): 
    info = image_name.replace('-','_').split('_') 
    return info[0]+'_'+info[1]

def get_result(row):
    results = [[row[1],float(format(float(row[2]), '.5f'))],
              [row[3],float(format(float(row[4]), '.5f'))],
              [row[5],float(format(float(row[6]), '.5f'))],
              [row[7],float(format(float(row[8]), '.5f'))],
              [row[9],float(format(float(row[10]), '.5f'))]]
    return row[1], results

def run(directory, breeding_sites):
    check_coor = []
    GeoJSON = {} 
    GeoJSON['type'] = "FeatureCollection" 
    GeoJSON['features'] = []
    with open(os.path.join(directory,'features_classified.csv')) as csvfile: 
        rows = list(csv.reader(csvfile, delimiter=';', quotechar='|'))   
        for row_x in rows: 
            coor_x = get_coor(row_x[0])
            if(coor_x not in check_coor):
             
                lat, lng, year, month = get_info(row_x[0])
                Feature = {
                    'type': "Feature", 'geometry':{ 'type':"Point",'coordinates':[float(lng),float(lat)] },
                    'properties':{
                                    'image_name':lat+'_'+lng,
                                    'date':{ 
                                        'month':month, 'year':year 
                                    },
                                    'brd_sites':{}, 'count':{}                                    
                             }
                }
                SUM = 0
                for row_y in rows:
                    coor_y = get_coor(row_y[0])
                    if(coor_x == coor_y): 
                        head, chop, segnet = get_data(row_y[0])
                        label, results = get_result(row_y)

                        Feature['properties']['brd_sites'].update({
                                head:{
                                     chop:{
                                        'inception':results, 'segnet':segnet, 'label':label
                                       }
                                }})

                        if label in Feature['properties']['count']:
                            Feature['properties']['count'][label] += 1
                        else:
                            Feature['properties']['count'][label] = 1
                            
                        SUM += 1
                Feature['properties']['sum'] = SUM                           
                GeoJSON['features'].append(Feature)
                check_coor.append(coor_x)
        
        
        with open(os.path.join(directory,'brd_sites.js'), 'w') as f: 
            f.write('brd_sites('+json.dumps(GeoJSON, sort_keys=True, indent=4, separators=(',', ': '))+')')
        
        print('----------------------')
        print('converted to geojson')
        print('unique coordinate: '+str(len(check_coor)))
        print('----------------------')