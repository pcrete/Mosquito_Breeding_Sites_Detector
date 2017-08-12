#!/usr/bin/env python
# -*- coding: utf-8 -*-

from feature_vector import to_geojson
from feature_vector import xgb_classifier
import argparse
import os

breeding_sites = [ 
                'pot, flowerpot', 'stupa, tope', 
                'water jug', 'water bottle', 
                'ashcan, trash can, garbage can, wastebin, ash bin,\
                 ash-bin, ashbin, dustbin, trash barrel, trash bin', 
                'greenhouse, nursery, glasshouse', 'milk can', 
                'barrel, cask', 'canoe', 'rain barrel', 
                # 'lakeside, lakeshore', 
                'Dutch oven' 
                ]

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--province',
		type=str,
		help='province/city name (จังหวัด)',
		required=True
	)
	parser.add_argument(
		'--district',
		type=str,
		help='district name (Amphoe อำเภอ)',
    	required=True
	)
	parser.add_argument(
		'--subdist',
		type=str,
		help='sub-district name (Tambon, ตำบล)',
		required=True
	)
	parser.add_argument(
		'--village',
		type=str,
		help='village name (หมู่บ้าน)',
		required=True
	)
	FLAGS, unparsed = parser.parse_known_args()
	
	province = FLAGS.province.decode('utf8')
	district = FLAGS.district.decode('utf8') 
	subdist = FLAGS.subdist.decode('utf8')
	village = FLAGS.village.decode('utf8')
    
	directory = os.path.join('../GSV',province, district, subdist, village)

	xgb_classifier.run(directory, breeding_sites)
	to_geojson.run(directory, breeding_sites)