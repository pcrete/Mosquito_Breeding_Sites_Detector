import numpy as numpy 
import math
import cv2
import scipy.misc
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tqdm import tqdm 
from collections import Counter
from sklearn.neighbors import NearestNeighbors

Sky = [128,128,128]
Building = [128,0,0]
Pole = [192,192,128]
Road = [128,64,128]
Pavement = [60,40,222]
Tree = [128,128,0]
SignSymbol = [192,128,128]
Fence = [64,64,128]
Car = [64,0,128]
Pedestrian = [64,64,0]
Bicyclist = [0,128,192]
Unlabelled = [0,0,0]
colors = np.array([Sky, Building, Pole, Road, 
                          Pavement, Tree, SignSymbol, 
                          Fence, Car, Pedestrian, Bicyclist, 
                          Unlabelled])
labels = ['Sky', 'Building', 'Pole', 'Road', 
          'Pavement', 'Tree', 'SignSymbol', 
          'Fence', 'Car', 'Pedestrian', 'Bicyclist', 
          'Unlabelled']

knn = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(colors)

img_size = 600
window_size = 149

def run(directory):
    print directory

    original_path = os.path.join(directory, 'original')
    segmented_path = os.path.join(directory, 'segmented')
    divided_path = os.path.join(directory, 'divided')
    if not os.path.exists(divided_path):
        os.makedirs(divided_path)
        
    for img_path in tqdm(os.listdir(original_path),'dividing images..'):
        divide_image(original_path, segmented_path, divided_path, img_path)

def divide_image(original_path, segmented_path, divided_path, img_path):
    original_img = mpimg.imread(os.path.join(original_path, img_path))
    segmented_img = mpimg.imread(os.path.join(segmented_path, img_path[:-4]+'_segmented.jpg'))
    segmented_img = cv2.resize(segmented_img, (600,600))
    
    original_blocks = get_blocks(original_img)
    segmented_blocks = get_blocks(segmented_img)
    
    save_block(divided_path, img_path, original_blocks, segmented_blocks)

def get_blocks(img):
    blocks = []
    for r in range(0,img_size-window_size,window_size):
        for c in range(0,img_size-window_size,window_size):
            window = img[r:r+window_size,c:c+window_size]
            blocks.append(window)
    return blocks

def save_block(divided_path, img_path, original_blocks, segmented_blocks):
    for i, block in enumerate(original_blocks):
        if(i >= 4):
            segment = get_segment(segmented_blocks[i])
            path = divided_path+'/'+img_path[:-4]+'_'+str(i+1)+'_'+segment+'.jpg'
            scipy.misc.imsave(path, block)

def get_segment(img):    
    r,g,b = img[:,:,0].flatten(), img[:,:,1].flatten(), img[:,:,2].flatten()
    r = Counter(r).most_common(1)[0][0]
    g = Counter(g).most_common(1)[0][0]
    b = Counter(b).most_common(1)[0][0]

    y = np.array([r,g,b])
    y = y.reshape(-1, y.shape[0])
    indices = knn.kneighbors(y)[1]
    return labels[indices[0,0]]