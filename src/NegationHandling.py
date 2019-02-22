# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 09:38:40 2019

@author: Mark Zhu
"""

def negationHandling(x_train):
    """
    given an matrix of individual words in order, combine "negation,"word" into
    "neg_word"
    """
    
    negation_words = ("not","hardly","barely","never","neither","scarcely",
                      "doesn't","doesnt","isn't","isnt","wasn't","wasnt",
                      "shouldn't","shouldnt","wouldn't","wouldnt","couldn't",
                      "couldnt","won't","wont","can't","cant","don't","dont")
    filteredMatrix = []
    for reviews in x_train:
        filteredReviews = []
        for index in range(len(reviews)-1):
            if reviews[index] in negation_words:
                reviews[index+1] = "neg_"+reviews[index+1]
                
        for words in reviews:
            if words not in negation_words:
                filteredReviews.append(words)
        filteredMatrix.append(filteredReviews)

    return filteredMatrix
            
