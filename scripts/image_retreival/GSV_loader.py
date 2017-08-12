#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import urllib2
from io import BytesIO
from tqdm import tqdm
import json
import os

key_index = 0

def run(vill_points, path, keys):
    if not os.path.exists(path): 
        os.makedirs(path)

    for lat, lng in tqdm(vill_points, 'loading GSV'):
        loading(lat, lng, path, keys)
    print('GSV loaded\n')

def loading(lat, lng, path, keys): 
    global key_index 
    heads=['0','60','120','180','240','300'] 
    fov='110' 
    pitch='-30'
    j = 0 
    check = False
    while not check: 
        location = str(lat)+','+str(lng) 
        try: 
            key = keys[key_index] 
            baseMetaUrl = "https://maps.googleapis.com/maps/api/streetview/metadata" 
            metaUrl = baseMetaUrl+"?location="+location+"&fov="+fov+"&pitch="+pitch+"&key="+key 
            requestMeta = urllib2.urlopen(metaUrl)    
            metaJson = json.loads(requestMeta.read().decode('utf8')) 
            if metaJson["status"] == 'OK': 
                for heading in heads:
                    lat, lng = str(metaJson["location"]["lat"]), str(metaJson["location"]["lng"]) 
                    coordinate = lat+','+lng
                    baseImgUrl = "https://maps.googleapis.com/maps/api/streetview?size=600x600" 
                    imgUrl = baseImgUrl+"&location="+coordinate+"&fov="+fov+"&heading="+heading+"&pitch="+pitch+"&key="+key 
                    requestImg = urllib2.urlopen(imgUrl) 
                    image = Image.open(BytesIO(requestImg.read())) 
                    image.save(path +'/'+lat+'_'+lng+'_'+heading+'_'+metaJson["date"]+'.jpg') 
            check = True 
        except urllib2.HTTPError as e: 
            key_index+=1 
            print('Change Key Index to '+str(key_index)) 
            if key_index>len(keys)-1:  
                print(lat,lng,path) 
                break 
            print('Forbidden '+str(e.getcode())+': '+imgUrl) 
            continue