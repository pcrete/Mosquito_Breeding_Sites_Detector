#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shapely.geometry import Polygon, Point, MultiPolygon, LineString, MultiLineString
import numpy as np
import json
from tqdm import tqdm
import os
import time
import math
import overpass

multipoly = []

def run(province, district, subdist):
	polygon = get_polygon(province, district, subdist)
	if(polygon != 'error'):
		return extract_coordinates(polygon)
	return 'error'

def get_polygon(province, district, subdist):
	# print(province, district, subdist)
	with open('../geojson/province/'+province+'.geojson') as f:
		data = json.load(f)
	print('Imported '+province+'\'s GeoJSON')

	if(district == "เมือง".decode('utf8')): district+=province

	match_feature = []
	for feature in data['features']:
		prop = feature['properties']
		if district==prop['AP_TN'] and subdist==prop['TB_TN']:
			print('loaded polygon')
			return Polygon(feature['geometry']['coordinates'][0])
	print('polygon not loaded')
	return 'error'

def extract_coordinates(polygon):
	data = generate_overpass_script(polygon)
	print('retrieved roads (linestrngs) from overpass api')
	multiline = []
	for feature in data['features']:
		if (feature['geometry']['type'] == 'LineString'):
			multiline.append(feature['geometry']['coordinates'])
	points = linestring_to_coords(multiline)
	print('linestring: '+str(len(multiline))+' lines')
	print('total points: '+str(len(points))+'points\n')
	return points

def generate_overpass_script(polygon):
	api = overpass.API(timeout=100)
	query = '(\nway[highway](poly:"'    
	# convert polygon to coordinates (longitude, latitude)
	coords = list(polygon.exterior.coords)
	for coord in coords:
		lng, lat =  coord
		query += str(lat)+' '+str(lng)+' '
	query = query[:-1] + '");\n);'
	return api.Get(query)

def linestring_to_coords(multiline):
	print('converting linestrings to coordinates..')
	points = []
	for line in tqdm(multiline,'Iterating through roads'):
		for i in range(len(line)-1):
			x1,y1 = line[i]
			x2,y2 = line[i+1]
			x1 += 0.0000000001

			degree = math.degrees(math.atan(abs((y1-y2)/(x1-x2))))
            
			if(degree < 45): 
				if(x1 == min(x1,x2)): start_x,start_y, end_x,end_y = x1,y1, x2,y2 
				else: start_x,start_y, end_x,end_y = x2,y2, x1,y1
                    
				m = (start_y-end_y)/(start_x-end_x)
				FROM, TO = start_x, end_x                      
				cur_x, cur_y = start_x, start_y
				while(FROM < TO):
					new_x, new_y = linearEquation_x(start_x, start_y, m, FROM)
					dist = math.hypot(new_x-cur_x, new_y-cur_y)
					meters = 111111*dist
					if(meters > 50):
						cur_x, cur_y = new_x, new_y
						points.append([cur_y, cur_x])  
					FROM += 0.000000123
			else:
				if(y1 == min(y1,y2)): start_x,start_y, end_x,end_y = x1,y1, x2,y2 
				else: start_x,start_y, end_x,end_y = x2,y2, x1,y1
	
				m = (start_y-end_y)/(start_x-end_x)
				FROM, TO = start_y, end_y                      
				cur_x, cur_y = start_x, start_y
				while(FROM < TO):
					new_x, new_y = linearEquation_y(start_x, start_y, m, FROM)
					dist = math.hypot(new_x-cur_x, new_y-cur_y)
					meters = 111111*dist
					if(meters > 50):
						cur_x, cur_y = new_x, new_y
						points.append([cur_y, cur_x])  
					FROM += 0.000000123
	return points

def linearEquation_x(x1, y1, m, x):
	y = m*(x-x1)+y1
	return x,y

def linearEquation_y(x1, y1, m, y):
	x = (y - y1 + (m*x1)) / m
	return x,y
