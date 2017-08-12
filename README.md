# Mosquito Breeding Sites Detector

This project is about detecting Dengue’s vectors breeding site from Google Street View images using deep learning. The main vector is Aedes Egypti mosquito.

## Table of contents

* Pipeline of process
* Description of Code
* Directory Structure
* Getting Started
    * Prerequisites
    * Installing
    * Running
    * Result
* Built With

## Pipeline of process
![alt text](https://drive.google.com/open?id=0BwfdEKJrhCfQbm5Ua1NYMEJvSXc "Pipeline of process")

## Description of Code

#### All code is in scripts directory.

* `data_collection.py` used for retrieve google street view images of village that you want. The image size is 600x600 pixels.

* `image_recognition.py` used for recognize images , it will return top five classification results.

* `image_segmentation.py` used for extract segmented of image.

* `feature_vector_classification.py` used for classify the result of image recognition and image segmentation again for increasing more accuracy.

## Directory Structure

```
+Mosquito_Breeding_Sites_Detector
  +SegNet-Tutorial @ fcaf7c4
  +caffe-segnet @ dba4398
  +xgboost @ 771a95a
  +dataset
    -Inception model evaluation.ipynb	
    -Training Classifier.ipynb
    -testing.csv
    -train_test.csv
    -training.csv
    -xgb.model
  +geojson
    +province
    -village.geojson
  +scripts
    +feature_vector
      -feature_vector_classification.ipynb
      -to_geojson.ipynb
      -to_geojson.py
      -xgb_classifier.py
      -README.md
    +image_processing
      +model
      -__init__.py
      -image_divider.py
      -image_recognizer.py
      -inception.py      
      -README.md
    +image_retreival
      -GSV_loader.py
      -get_village_points.py
      -polygon_to_points.py
      -README.md
    +segnet
      +Models
      -__init__.py
      -pysegnet.py
      -README.md
    -data_collection.py
    -image_recognition.py
    -image_segmentation.py
    -feature_vector_classification.py
    -README.md
  +GSV/ชัยนาท/มโนรมย์/ท่าฉนวน/บ้านคลองรุน
    +divided
    +original
    +segmented
    -brd_sites.js
    -features.csv
    -features_classified.csv
    -visualization.html
  -README.md
  -INSTALL.md
  -RESULT.md
```

## Getting Started

These instructions is about how you copy this project up and running on your local machine for development and testing purposes.

### Prerequisites

* Tensorflow
* Caffe-Segnet
* Overpass
* Google street view static image API key

### Installing

* [Installing](INSTALL.md)

### Running 
* [Running](scripts/README.md)

### Result
* [Example Result](dataset/README.md)

## Built With

* [tensorflow](https://www.tensorflow.org/) - image recognition 
* [caffe-segnet](https://github.com/alexgkendall/caffe-segnet) - image segmentation
* [overpass](https://github.com/mvexel/overpass-api-python-wrapper) - street geojson
* [google map](https://developers.google.com/maps/) - street view image and visualization