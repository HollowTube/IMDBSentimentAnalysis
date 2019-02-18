from unittest import TestCase
import pandas as pd
import numpy as np
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import confusion_matrix
from src.Naive_Bayes import naiveBayes


class test_naive_bayes(TestCase):

    def test_bernoulli_bayes(self):
        data = np.array([
            [0, 1, 1],
            [0, 1, 1],
            [1, 1, 0],
            [1, 0, 0],
            [1, 1, 1],
            [0, 1, 0],
            [1, 0, 1]])
        data_test = np.array([[0, 0, 0],
                              [1, 1, 1],
                              [1, 0, 1],
                              [0, 1, 0],
                              [1, 1, 0]])
        x_train = pd.DataFrame(data)
        x_test = pd.DataFrame(data_test)

        y_train = pd.DataFrame(np.array([[1], [1], [0], [0], [0], [0], [1]]))
        y_actual = pd.DataFrame(np.array([[0], [1], [1], [0], [0]]))

        # Testing it with sk-learn implementation
        bnb = BernoulliNB()
        bnb.fit(x_train,y_train)
        y_pred_1 = bnb.predict(x_test)
        cm_sk = confusion_matrix(y_actual, y_pred_1)


        # Testing it on homemade implementation
        nb = naiveBayes(smoothing=True)
        nb.fit(x_train, y_train)
        y_pred = nb.predict(x_test)
        cm = confusion_matrix(y_actual, y_pred)

        self.assertTrue(np.array_equal(cm,cm_sk))



