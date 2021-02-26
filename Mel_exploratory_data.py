#!/usr/bin/env python
# coding: utf-8

# In[52]:


#Coding Club Titanic

#load standard libraries
import numpy as np 
import pandas as pd 
import os
import seaborn as sns
import matplotlib.pyplot as plt

#%cd /ihome/che2201-2020f/mim134/Coding_club
#load the data. This will load the test and train files as long
#as they are in the same directory as this script

train_data = pd.read_csv("train.csv")
#print (train_data)
Standard_data =  train_data.drop(['Name','Ticket','Cabin'],axis = 1)




# change male to 0 and female to 1
Standard_data = Standard_data.replace({'male':0, 'female':1})

# change place from embarkment C=0, Q=1, S=2
Standard_data['Embarked'] = Standard_data['Embarked'].replace({'C':0, 'Q':1, 'S':2})
Standard_data['Embarked'] = Standard_data['Embarked'].fillna(Standard_data['Embarked'].mean())
#find replacement age
Standard_data['Age'] = Standard_data['Age'].fillna(Standard_data['Age'].mean())



Standard_data.hist()


# In[53]:



# Standardize the data attributes for the data.
#from sklearn import preprocessing

from sklearn import preprocessing 
X_imputed=preprocessing.Imputer().fit_transform(Standard_data) 
print(X_imputed)
X_imputed_df = pd.DataFrame(X_imputed, columns = Standard_data.columns)
X_imputed_df


# In[54]:


# find correlations
from scipy.stats import pearsonr
corr, _ = pearsonr(X_imputed_df['Survived'], X_imputed_df['Age'])
print('Pearsons correlation for age: %.3f' % corr)

corr, _ = pearsonr(X_imputed_df['Survived'], X_imputed_df['Sex'])
print('Pearsons correlation for Sex: %.3f' % corr)

corr, _ = pearsonr(X_imputed_df['Survived'], X_imputed_df['Pclass'])
print('Pearsons correlation for class: %.3f' % corr)

corr, _ = pearsonr(X_imputed_df['Survived'], X_imputed_df['Fare'])
print('Pearsons correlation for fare: %.3f' % corr)

corr, _ = pearsonr(X_imputed_df['Survived'], X_imputed_df['Embarked'])
print('Pearsons correlation for embarked: %.3f' % corr)

corr, _ = pearsonr(X_imputed_df['Survived'], X_imputed_df['SibSp'])
print('Pearsons correlation for sibling/spouses: %.3f' % corr)

corr, _ = pearsonr(X_imputed_df['Survived'], X_imputed_df['Parch'])
print('Pearsons correlation for children/parents: %.3f' % corr)


# In[68]:


#Standard_data.plot( x='Survived', y='Fare', kind = 'bin')
boxplot = X_imputed_df.boxplot(column = ['Fare'],by = 'Survived')
#X_imputed_df.boxplot(column = ['Sex'], by = ['Survived'])


# In[70]:


sns.violinplot(x = 'Survived', y = 'Sex',data = Standard_data)


# In[78]:


X_imputed_df.value_counts(["Survived", "Pclass"])
#X_imputed_df.value_counts(["Survived", "Sex"])
percentclass1 = 136/(136+80)*100
percentclass2 = 87/(87+97)*100
percentclass3 = 119/(119+372)*100
print(percentclass1)
print(percentclass2)
print(percentclass3)


# In[75]:


Standard_data.value_counts(["Survived"])
X_imputed_df.value_counts(["Survived"])


# In[ ]:




