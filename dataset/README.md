# Result 

`Inception model evaluation.ipynb` IPython notebook for evaluating inception model 

`Training Classifier.ipynb` IPython notebook for training xgboost classifier 

`testing.csv` testing dataset 

`train_test.csv`training and testing dataset 

`training.csv` training dataset 

`xgb.model` classification model 

* Example of classification result, 

| Image name | 1st result | 1st score | 2nd result | 2nd score | 3rd result | 3rd score | 4th result | 4th score | 5th result | 5th score | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| 15.38203756895384-100.1636399994293-120-2013-09-5-Tree | lakeside, lakeshore | 0.2218 | worm fence | 0.110338 | swing | 0.0501 | golf ball| 0.0215 | golfcart, golf cart | 0.0179 

* Performance of inception model (All classes) 

| named | Top-1 & thresh=0.30 |	Top-1 & thresh=0.15	| Top-1 |	Top-5 | 
| --- | --- | --- | --- | --- |  
| sample size |	3739 | 7456 | 13274 | 60920 |  
| accuracy | 0.6060444 | 0.5053648 | 0.3836824 | 0.2774458 | 

* Performance of inception model (Each class) 

| named	| pot, flowerpot | stupa, tope | water jug | water bottle | trash can, garbage can | greenhouse, nursery | milk can | barrel, cask | canoe | rain barrel | lakeside, lakeshore | Dutch oven | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| Top-5_size | 11589.0 | 232.0 | 648.0 | 208.0 | 5587.0 | 9850.0 | 3017.0 | 1071.0 | 1737.0 | 2008.0 | 25291.0 | 496.0 | 
| Top-5_acc |0.4219519 |0.2758621 |	0.4012346 | 0.4086538 |	0.2980132 |	0.3636548 |	0.4474644 | 0.5770308 |	0.3172136 |	0.5363546 |	0.2354593 | 0.4798387 | 
| Top-1_size | 4236.0 | 33.0 | 48.0 | 40.0 | 925.0 | 1552.0 | 470.0 | 109.0 | 182.0 | 319.0 | 5292.0 | 68.0 | 
| Top-1_acc | 0.4497167 | 0.4848485 | 0.4583333 | 0.475 | 0.4497297 | 0.3936856 | 0.5765957 | 0.559633 | 0.5879121 | 0.6677116 | 0.2673847 | 0.5441176 | 
| Thresh_size |	2862.0 | 17.0 | 21.0 | 19.0 | 476.0 | 961.0 | 229.0 | 67.0 | 95.0 | 206.0 | 2471.0 | 32.0 | 
| Thresh_acc | 0.5345912 | 0.7647059 | 0.7142857 | 0.5263158 | 0.6491597 | 0.4412071 | 0.8165939 | 0.7014925 | 0.6526316 | 0.7621359 | 0.402671 | 0.59375 | 

## Classification based on Top-5 results

* Training and Testing set 

| | Sample sizes | Yes | No | Ratio | 
| --- | --- | --- | --- | --- | 
| Dataset | 60,920 | 16,902 | 44,018 | 0.28 |  
| Training set | 5,092 | 1,190 | 3,902 | 0.23 | 
| Testing set | 10,000 | 5,000 | 5,000 | 0.50 | 

* Classification Performance of XGBoost 

| | Training | Testing | 
| --- | --- | --- | 
| Accuracy | 0.766634 | 0.5025 | 

## Classification based on Top-1 result 


| | Sample sizes | 
| --- | --- |
| Dataset | 60,920 | 
| Select where top-1 score > 0.15 | 32,658 | 
| Select where top-1 = breeding sites | 7,456 | 

* Training and Testing set 

| | Sample sizes | Yes | No | Ratio | 
| --- | --- | --- | --- | --- |  
| Training set | 5,219 | 2,657 | 2,562 | 0.5091 | 
| Testing set | 2,237 | 1,111 | 1,126 | 0.4966 |

* Classification Performance of XGBoost 


| | SVM | Decision Tree | Knn | Random Forest |
| --- | --- | --- | --- | --- |
| Accuracy | 0.5739 | 0.5928 | 0.5928 | 0.6366 |

<table> 
  <tr> 
    <td colspan="4"><strong>Individual classifier</strong></td> 
    <td colspan="2"><strong>Voting classifier</strong></td> 
    <td colspan="1"><strong>Final Classifier</strong></td> 
  </tr> 
  <tr> 
    <td>SVM</td> 
    <td>Decision Tree</td> 
    <td>Knn</td> 
    <td>Random Forest</td> 
    <td>SVM + KNN + Decision Tree</td> 
    <td>Logistic Regression + Random Forest + GaussianNB</td> 
    <td>XGBoost</td> 
  </tr> 
  <tr> 
    <td>0.5739</td> 
    <td>0.5928</td> 
    <td>0.5928</td> 
    <td>0.6366</td> 
    <td>0.6165</td> 
    <td>0.6477</td> 
    <td><strong>0.6822</strong></td> 
  </tr> 
</table>