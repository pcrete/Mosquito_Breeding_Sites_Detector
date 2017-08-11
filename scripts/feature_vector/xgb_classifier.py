import os
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def select_rows(features, breeding_sites, threshold=0.1):
	print('total:', len(features))
	features = features[features['1st_score'] >= threshold]
	print('after thresh:',len(features))
	features = features.loc[features['1st_result'].isin(breeding_sites)]
	print('features:',len(features))
	return features

def add_segment(features):
	img_name = features.index
	segment = []
	for img in img_name:
		img = img[img.index('_',img.index('-'))+1:]
		img = img[img.index('_')+1:]
		segment.append(img)
	features['segment'] = segment
	return features

def preprocess(features): 
    features = features.drop('1st_score', axis=1)    
    features = features.drop('2nd_score', axis=1)
    features = features.drop('3rd_score', axis=1)    
    features = features.drop('4th_score', axis=1)
    features = features.drop('5th_score', axis=1)
    
    for c in features.columns:
        features[c]=features[c].fillna(-1)
        if features[c].dtype == 'object':
            lbl = LabelEncoder()
            lbl.fit(list(features[c].values))
            features[c] = lbl.transform(list(features[c].values))
    return features

def run(directory, breeding_sites):
	features = pd.read_csv(os.path.join(directory,'features.csv'), sep=';', index_col='img_name',
                        names=['img_name','1st_result','1st_score','2nd_result','2nd_score',
                                           '3rd_result','3rd_score','4th_result','4th_score',
                                           '5th_result','5th_score'])
    
	features = select_rows(features, breeding_sites, threshold=0.15)
	features = add_segment(features)

	data = preprocess(features)

	bst = xgb.Booster() 
	bst.load_model('../dataset/xgb.model')
	y_xgb = bst.predict(xgb.DMatrix(data))

	predicted = [int(round(value)) for value in y_xgb]

	features['cls'] = predicted

	classified = features.loc[features['cls'] == 1]
	print('classified:', len(classified))

	classified = classified.drop('cls',axis=1)
	classified = classified.drop('segment',axis=1)
	classified.to_csv(os.path.join(directory,'features_classified.csv'), header=None, sep=';')

	print('finised classification')