
#load standard libraries
import numpy as np 
import pandas as pd 
import os
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

#load the data. This will load the test and train files as long
#as they are in the same directory as this script
train_data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'train.csv') )
test_data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'test.csv') )

train_data.sort_values(by = 'Survived', inplace = True)
y = train_data["Survived"]


#fill in missing values in both the test set and the train set
column_means = train_data.mean()
train_data.fillna(column_means, inplace = True)

column_means = test_data.mean()
test_data.fillna(column_means, inplace = True)



#only use these features for now
features = ["Pclass", "Sex", "SibSp", "Parch", "Age", "Fare", "Embarked"]

#convert categorical data to numerical data
X = pd.get_dummies(train_data[features])

#use a standard scalar to scale the data
X = scaler.fit_transform(X)

#do the same thing for the test data
X_test = pd.get_dummies(test_data[features])
X_test= scaler.fit_transform(X_test)



#Try a few different models here
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100,  random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)



from sklearn.neighbors import NearestCentroid
clf = NearestCentroid()
clf.fit(X, y)
predictions = clf.predict(X_test)


# predictions = []

# for i, row in test_data.iterrows():
#     pass
#     if row['Sex'] == 'female':
#         predictions.append(1)
#     else:
#         predictions.append(0)


output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('my_submission.csv', index=False)
print("Your submission was successfully saved!")



