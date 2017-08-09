#!/usr/bin/env python
# -*- coding: utf-8 -*-

from segnet import pysegnet as seg
import os

province = 'ชัยนาท'
district = 'มโนรมย์'
subdist = 'ท่าฉนวน'
village = 'บ้านคลองรุน'

directory = os.path.join('../GSV',province, district, subdist, village)

seg.segment(directory)