
get_ipython().magic('reset -sf')

#load standard libraries
import numpy as np 
import pandas as pd 
import os

#example list a
list_a= [1,2,3,1,2,3]
list_a.append(4)
list_a.sort()

#get a specific item out of a list
third_item_a = list_a[2]

#sum of the list
list_sum = sum(list_a)

#set of a list
set_a = set(list_a)

#example list b
list_b = ['text', 1, 'more text']
set_b = set(list_b)

#operations on sets
set_b.difference(set_a)
set_b.union(set_a)
set_b.intersection(set_a)

#example tuple
tuple_a =  (1,2,3,1,2,3)

dict_a = {'one':1, 'two':2, 'three':3}


#converting to advanced structures

#dataframe
dataframe_a = pd.DataFrame(index = [0], data = dict_a)

#array
array_a = np.array(list_a)
array_a.mean()
array_a.std()


#This is a basic function
def get_mean_std(data):
#data should be an array

    mean_data = data.mean()
    std_data = data.std()
    return [mean_data, std_data]



