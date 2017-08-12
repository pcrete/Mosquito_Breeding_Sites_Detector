#!/usr/bin/env python
# -*- coding: utf-8 -*-

from image_processing import image_divider as divider
from image_processing import image_recognizer as recognizer
import argparse
import os

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

	divider.run(directory)	
	recognizer.run(directory)