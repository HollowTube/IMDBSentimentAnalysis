import pandas as pd
import numpy as np


# Convention y = 1 means positive review
class NaiveBayes:
    def __init__(self, smoothing=False):
        self.marginal_y_1 = None
        self.marginal_y_0 = None
        self.cond_class_0 = None
        self.cond_class_1 = None
        self.smoothing = smoothing

    def fit(self, x_train, y_train):

        num_rows = x_train.shape[0]
        num_features = x_train.shape[1]

        # Getting the marginal probability of class y=1
        num_class_1 = 0
        for index, row in y_train.iterrows():
            num_class_1 += row[0]
        num_class_0 = num_rows - num_class_1
        self.marginal_y_1 = float(num_class_1) / (x_train.shape[0])
        self.marginal_y_0 = 1.0 - self.marginal_y_1

        # Getting the conditional probabilities
        cond_y1 = np.zeros(num_features)
        cond_y0 = np.zeros(num_features)

        for row_index, row in x_train.iterrows():
            feature_index = 0
            for feature in row:
                if int(feature) == 1:
                    if y_train.iloc[row_index][0] == 1:
                        cond_y1[feature_index] += 1
                    else:
                        cond_y0[feature_index] += 1
                feature_index += 1

        # Finishing up the conditional array, and deciding the apply smoothing or not
        if self.smoothing:
            cond_y0 = cond_y0 + 1
            cond_y1 = cond_y1 + 1
            self.cond_class_0 = cond_y0 * (1.0 / (num_class_0 + 2))
            self.cond_class_1 = cond_y1 * (1.0 / (num_class_1 + 2))
        else:
            self.cond_class_0 = cond_y0 * (1.0 / num_class_0)
            self.cond_class_1 = cond_y1 * (1.0 / num_class_1)

    def predict(self, x_test):
        prob_y1 = self.marginal_y_1
        prob_y0 = self.marginal_y_0

        result = np.zeros((x_test.shape[0]))

        # Calculating probabilities for each class
        for index, row in x_test.iterrows():
            feature_index = 0
            for feature in row:
                if int(feature) == 1:
                    prob_y1 *= self.cond_class_1[feature_index]
                    prob_y0 *= self.cond_class_0[feature_index]
                else:
                    prob_y1 *= (1 - self.cond_class_1[feature_index])
                    prob_y0 *= (1 - self.cond_class_0[feature_index])
                feature_index += 1
            if prob_y0 > prob_y1:
                result[index] = 0
            else:
                result[index] = 1

        return result
