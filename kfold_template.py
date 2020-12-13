import pandas
from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

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