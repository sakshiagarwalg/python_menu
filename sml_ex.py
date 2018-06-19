#! /usr/bin/python3
from sklearn import tree
import os
# data
#feautures_name are weight and texture
# texture_name: smooth=0 and bumpy=1
data=[[100,0],[130,0],[135,1],[150,1]] 
# target   
output=["orange","orange","apple","apple"] 
# calling decision tree classifier                          
algo=tree.DecisionTreeClassifier()
# train the data
trained_algo=algo.fit(data,output)
# testing
predict=trained_algo.predict([[100,1]])
# printing the output
print(predict)
