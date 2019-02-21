#from unittest import TestCase
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from src.Naive_Bayes import NaiveBayes
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC


class ModelTester():
    
    def test_all(self,x_train,y_train,x_test,y_test): #assuming x_train/x_test are matrices of words and y_train/y_test are lists of pos/neg
        logReg = LogisticRegression().fit(x_train,y_train)
        logRegScore = logReg.score(x_test,y_test)
    
        deciTree = DecisionTreeClassifier().fit(x_train,y_train)
        deciTreeScore = deciTree.score(x_test,y_test)
    
        linSVC = LinearSVC().fit(x_train,y_train)
        linSVCScore = linSVC.score(x_test,y_test)
        
        print("Logistic regression has a score of {}".format(logRegScore))
        print("Decision Tree has a score of {}".format(deciTreeScore))
        print("Linear SVC has a score of {}".format(linSVCScore))
        
        
    