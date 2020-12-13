from sklearn import linear_model
import pandas
import kfold_template

#linear regression model
dataset = pandas.read_csv("business_data.csv")
sub_dataset = dataset.sample(n=1000)
#print(sub_dataset)

target = sub_dataset.iloc[:,2].values
data = sub_dataset.iloc[:,[5,6,7,8,12,16]].values
target = target.astype(int)

machine = linear_model.LinearRegression()

accuracy_score, confusion_matrix = kfold_template.run_kfold(4, data, target, machine)

results = pandas.DataFrame(['linear ',accuracy_score])


results.to_csv('linear_reg.csv')