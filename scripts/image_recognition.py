#!/usr/bin/env python
# -*- coding: utf-8 -*-

from image_processing import image_divider as divider
from image_processing import image_recognizer as recognizer
import os

province = 'ชัยนาท'
district = 'มโนรมย์'
subdist = 'ท่าฉนวน'
village = 'บ้านคลองรุน'

directory = os.path.join('../GSV',province, district, subdist, village)

divider.run(directory)	
recognizer.run(directory)