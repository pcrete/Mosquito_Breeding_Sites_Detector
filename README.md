# Mosquito Breeding Sites Detector

## Table of contents

* Installation
* How it works
* How to use
* Links

## Getting Started

## Prerequisites

## Installing


# How it works
## Pipeline of processes
![alt text](http://silverpond.com.au/img/blog/pedestrian-detection-details/image03.png "Logo Title Text 1")

## 1. Data Collection
### Step 1: Convert shape file to geojson file
Command line to convert .shp to .geojson [link to install](http://www.gdal.org/ogr2ogr.html)
* input: subdistrict.shp
* output subdistrict.geojson

For example, 
```command
ogr2ogr -f GeoJSON output.geojson input.shp
```

### Step 2: Convert subdistrict polygon to points
* input: subdistrict.geojson
* output points of subdistrict


### Step 3: Extract village points from subdistrict points
* input: points of subdistrict
* output points of village


### Step 4: Load Google Street View Image from village points
* input: points of village
* output google street view image

## 2. Data Processing
### Step 1: Classify image
* input: google street view images
* output: features (.csv) 
#### Step 1a: Image Recognition
* input: google street view images
* output: top five classification result with confident (.csv) 
#### Step 1b: Image Segmentation
* input: google street view images
* output segmented image

### Step 2: Cascade Classification
* input: features (.csv)
* output classificatino result (.csv)

## 3. Data Visualization

### Step 1: Generate geojson from classification result
* input: classificatino result (.csv)
* output result geojson (.js)

### Step 2: Visualize on map
* input: result geojson (.js)
* output map visualization

# Built With
* [tensorflow](https://www.tensorflow.org/) - image recognition 
* caffe-segnet - image segmentation
* google map - visualization script