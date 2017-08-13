# Training model and Evaluation

`Inception model evaluation.ipynb` IPython notebook for evaluating inception model

`Training Classifier.ipynb` IPython notebook for training xgboost classifier

`testing.csv` testing dataset

`train_test.csv`training and testing dataset

`training.csv` training dataset

`xgb.model` classification model

# Results

* Example of classification results

| Image name | 1st result | 1st score | 2nd result | 2nd score | 3rd result | 3rd score | 4th result | 4th score | 5th result | 5th score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15.38203756895384-100.1636399994293-120-2013-09-5-Tree | lakeside, lakeshore | 0.2218 | worm fence | 0.110338 | swing | 0.0501 | golf ball| 0.0215 | golfcart, golf cart | 0.0179

## Evaluation of Inception Model (Image Recognition)

* Performance of inception model (All classes)

| named | Top-5 | Top-1 | Top-1 & thresh=0.15 | Top-1 & thresh=0.30 |
| --- | --- | --- | --- | --- |
| sample size |	60920 | 13274 | 7456 | 3739 |
| accuracy | 0.2774 | 0.3837 |0.5053648 | 0.6060 |

* Performance of inception model (Each class)

| named	| flowerpot | stupa, tope | water jug | water bottle | trash can | greenhouse | milk can | barrel, cask | canoe | rain barrel | lakeside | Dutch oven |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Top-5_size | 11589 | 232 | 648 | 208 | 5587 | 9850 | 3017 | 1071 | 1737 | 2008 | 25291 | 496 | 
| Top-5_acc |0.4220 |0.2759 |	0.4012 | 0.4087 |	0.2980 |	0.3637 |	0.4475 | 0.5770 |	0.3172 |	0.5364 |	0.2355 | 0.4798 |
| Top-1_size | 4236 | 33 | 48 | 40 | 925 | 1552 | 470 | 109 | 182 | 319 | 5292 | 68 |
| Top-1_acc | 0.4498 | 0.48485 | 0.4583 | 0.475 | 0.4497 | 0.3937 | 0.5766 | 0.5596 | 0.5879 | 0.6677 | 0.2674 | 0.5441 |
| Thresh_size |	2862 | 17 | 21 | 19 | 476 | 961 | 229 | 67 | 95 | 206 | 2471 | 32 |
| Thresh_acc | 0.5346 | 0.7647 | 0.7143 | 0.5263 | 0.6492 | 0.4412 | 0.8165 | 0.7015 | 0.6526 | 0.7621 | 0.4027 | 0.5938 |

## Evaluation of Machine Learning Classifier

### Classification based on Top-5 results
* Training and Testing set

| | Sample sizes | Yes | No | Ratio |
| --- | --- | --- | --- | --- |
| Dataset | 60920 | 16902 | 44018 | 0.28 |
| Training set | 50920 | 11567 | 38723 | 0.23 |
| Testing set | 10000 | 5000 | 5000 | 0.50 |

* Classification Performance of XGBoost

| | Training | Testing |
| --- | --- | --- |
| Accuracy | 0.7666 | 0.5025 |

### Classification based on Top-1 result


| | Sample sizes |
| --- | --- |
| Dataset | 60920 |
| Select where top-1 score > 0.15 | 32658 |
| Select where top-1 = breeding sites | 7456 |

* Training and Testing set 

| | Sample sizes | Yes | No | Ratio |
| --- | --- | --- | --- | --- |
| Training set | 5219 | 2657 | 2,562 | 0.5091 |
| Testing set | 2237 | 1111 | 1126 | 0.4966 |

* Classification Performance

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