from feature_vector import to_geojson
from feature_vector import xgb_classifier
import os

breeding_sites = [ 
                'pot, flowerpot', 'stupa, tope', 
                'water jug', 'water bottle', 
                'ashcan, trash can, garbage can, wastebin, ash bin,\
                 ash-bin, ashbin, dustbin, trash barrel, trash bin', 
                'greenhouse, nursery, glasshouse', 'milk can', 
                'barrel, cask', 'canoe', 'rain barrel', 
                'lakeside, lakeshore', 'Dutch oven' 
                ]

province = 'ชัยนาท'
district = 'มโนรมย์'
subdist = 'ท่าฉนวน'
village = 'บ้านคลองรุน'

directory = os.path.join('../GSV',province, district, subdist, village)

xgb_classifier.run(directory, breeding_sites)
to_geojson.run(directory, breeding_sites)