#!/usr/bin/env python
# -*- coding: utf-8 -*-

from segnet import pysegnet as seg
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
	
	province = FLAGS.province
	district = FLAGS.district
	subdist = FLAGS.subdist
	village = FLAGS.village
	
	directory = os.path.join('../GSV',province, district, subdist, village)

	seg.segment(directory)