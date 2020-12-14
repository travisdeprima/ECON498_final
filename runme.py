import kfold_template
import pandas
import json
import numpy
from sklearn import linear_model
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

dataset = pandas.read_csv('business_data.csv')
sub_dataset = dataset.sample(n=1000)
#print(sub_dataset)

target = sub_dataset.iloc[:,2].values
data = sub_dataset.iloc[:,[5,6,7,8,12,16]].values 

target = target.astype(int)
max_depth_list = [10]
n_estimators_list = [11]
results_list = []

for i in max_depth_list:
	machine = RandomForestClassifier(n_estimators=11, criterion='gini', max_depth=i)
	accuracy_score, confusion_matrix = kfold_template.run_kfold(4, data, target, machine)
	results_list.append(['Random Forest ',accuracy_score,str(i)])
	for i in confusion_matrix:
		print(i)

for k in n_estimators_list:
	machine = RandomForestClassifier(n_estimators=k, criterion='gini', max_depth=10)
	accuracy_score, confusion_matrix = kfold_template.run_kfold(4, data, target, machine)
	results_list.append(['Random Forest ',accuracy_score,str(k)])
	for i in confusion_matrix:
		print(i)

results = pandas.DataFrame(results_list)

results.to_csv('forest.csv')

#linear regression model
target = sub_dataset.iloc[:,2].values
data = sub_dataset.iloc[:,[5,6,7,8,12,16]].values

target = target.astype(int)
machine = linear_model.LogisticRegression()
accuracy_score, confusion_matrix = kfold_template.run_kfold(4, data, target, machine)

results = pandas.DataFrame(['logistic ',accuracy_score])

results.to_csv('log_reg.csv')
