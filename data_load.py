
#load standard libraries
import numpy as np 
import pandas as pd 
import os


#load the data. This will load the test and train files as long
#as they are in the same directory as this script
train_data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'train.csv') )
test_data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'test.csv') )

train_data.sort_values(by = 'Survived', inplace = True)
