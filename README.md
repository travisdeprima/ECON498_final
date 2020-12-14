# ECON498_final

## Contents
- [Introduction](https://github.com/travisdeprima/ECON498_midterm/new/master?readme=1#introduction)
- [Technologies](https://github.com/travisdeprima/ECON498_midterm/new/master?readme=1#technologies)
- [Installation](https://github.com/travisdeprima/ECON498_midterm/new/master?readme=1#installation)
- [Explanation](https://github.com/travisdeprima/ECON498_midterm/new/master?readme=1#explanation)
  - [load_json](https://github.com/travisdeprima/ECON498_midterm/new/master?readme=1#load_json)
  - [kfold_template](https://github.com/travisdeprima/ECON498_midterm/new/master?readme=1#kfold_template)
  - [runme](https://github.com/travisdeprima/ECON498_midterm/new/master?readme=1#runme)
- [Limitations and Issues](https://github.com/travisdeprima/ECON498_midterm/new/master?readme=1#limitations-and-issues)

## Introduction
This code reads a dataset provided in the repository of business reviews on Yelp. The program then turns the dataset into a csv file that can then provided accuracy scores from a RandomForest model and a logistic model.
## Technologies
This program was written in Python version 3.7.6. Earlier versions of Python might not be up-to-date with the code provided in the program. Along with this, packages like pandas, sklearn, json, sklearn.model_selection, sklearn.metrics, and numpy may have to be installed prior to usage. 
## Installation
To install the program onto your computer, you can write the provided request into your terminal: 
```
pip install https://github.com/travisdeprima/ECON498_final.git
```
## Usage
After installing the program onto your computer we then run can run the file.

#### Explanation:

## load_json
The load_json.py file reads the json file `business_sample.json` and converts  certain qualitative variables to dummy variables in order to fit the data properly into out model.
```
cell_wi = (cell_state == "WI")
		if cell_state == "WI":
			data_wi.append(1)
		else:
			data_wi.append(0)
 ```
This type of structure is continued throughout the file and can be replicated for other variables the user deems necessary to look at. For the user, the ```load_yelp_json.py``` file is a good template to modify in order to analyze the varibles you desire.  

## kfold_template:
The kfold template I used and imported into my runme.py file was taken directly from the lecture regarding KFold. This is used to get our RandomForest and logistic model accuracy scores and confusion matricies.

```
def run_kfold(split_number,data,target,machine):
	kfold_object = KFold(n_splits=split_number)
	kfold_object.get_n_splits(data)

	results_accuracy = []
	results_confusion = []
	for training_index, test_index in kfold_object.split(data):
		data_training, data_test = data[training_index], data[test_index]
		target_training, target_test = target[training_index], target[test_index]
		machine.fit(data_training, target_training)
		results = machine.predict(data_test)
		results_accuracy.append(metrics.accuracy_score(target_test, results))
		results_confusion.append(metrics.confusion_matrix(target_test, results))
	return results_accuracy, results_confusion
  ```
## runme:
You will notice in the ```runme.py``` file that I have created a sub-dataset of variables to best fit the processing power of my computer. This is not required as the program can be adjusted to fit the entire dataset if one pleases. This can be simply commented out. 

Along with this your max_depth and n_estimators can be adjusted depending on dataset size. For this program, I just used the depth and estimators that were used in the class example, which showed to be just fine for my sub-dataset.

Another thing that can be changed is the data values that we can look at. Mind you that if you choose to use other variables in the dataset you must change them to dummy variables in the ```load_json.py``` file. 
```
target = sub_dataset.iloc[:,2].values
data = sub_dataset.iloc[:,[5,6,7,8,12,16]].values 

```
Finally the program runs both a Random Forest and Lojistic Regression to determine the accuracy scores and confusion matricies. These are saved into csv files named ```forest.csv``` and ```log_reg.csv```.

## Limitations and Issues
 Throughout the entire project there were a lot of difficulties, some of which I explained in my ```report.pdf``` file. Another major issue I had was that my prediction model wasn't running properly. Although I wasn't able to complete the prediction model, I was still able to gather enough to show that my Random Forest model accuracy scores were better than the logistic model's accuracy scores.
