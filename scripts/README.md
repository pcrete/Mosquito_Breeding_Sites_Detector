# Description
This is going to describe all of processes, start from very begining to the end of process.

## 1. Data Collection
### Step 0: Convert shape file to geojson file
Command line to convert .shp to .geojson [link to install](http://www.gdal.org/ogr2ogr.html)
* **input:** subdistrict.shp
* **output:** subdistrict.geojson

For example, 
```command
ogr2ogr -f GeoJSON output.geojson input.shp
```
### Step 1: Convert polygon's subdistrict to points/coordinate
`image_retreival/polygon_to_points.py`
* **input:** subdistrict.geojson, province, district, and subdist
* **output:** points/coordinate of subdistrict

### Step 2: Extract village points from subdistrict points
`image_retreival/get_village_points.py`
* **input:** points of subdistrict
* **output:** points of village

### Step 3: Load Google Street View Image from village points
`image_retreival/GSV_loader.py`
* **input:** points of village
* **output:** street view images

## 2. Data Processing
### Step 1: Classify image
* **input:** street view images
* **output:** features vector (.csv)
### Step 1a: Image Segmentation
`image_segmentation.py`

* **input:** google street view images
* **output:** segmented image
### Step 1b: Image Recognition
`image_recognition.py`

* **input:** street view and segmented images
* **output:** top-5 classification results (.csv)

### Step 2: Features Vector Classification
* **input:** features (.csv)
* **output:** classification results (.csv)

## 3. Data Visualization

### Step 1: Generate geojson from classification result
`feature_vector/feature_vector_classification.py'
* **input:** classificatino results (.csv)
* **output:** geojson (.js)

### Step 2: Visualize on map
'GSV/../../../visulization.py'
* **input:** geojson (.js)
* **output:** map visualization

# How to run
Assuming you have installed all of require libraries in [Installing](install.md), simply run

* ## Data Collection
```python
python data_collection.py --province PROVINCE --district DISTRICT --subdist SUBDIST --village VILLAGE
```
* ## Data Processing
```python
python image_recognition.py --province PROVINCE --district DISTRICT --subdist SUBDIST --village VILLAGE
```
```python
python image_segmentation.py --province PROVINCE --district DISTRICT --subdist SUBDIST --village VILLAGE
```
```python
python feature_vector_classification.py --province PROVINCE --district DISTRICT --subdist SUBDIST --village VILLAGE
```
