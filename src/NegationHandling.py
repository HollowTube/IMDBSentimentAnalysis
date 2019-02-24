# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 09:38:40 2019

@author: Mark Zhu
"""


def negationHandling(word_list):
    """
    given an matrix of individual words in order, combine "negation,"word" into
    "neg_word"
    """

    negation_words = ("not", "hardly", "barely", "never", "neither", "scarcely",
                      "doesn't", "doesnt", "isn't", "isnt", "wasn't", "wasnt",
                      "shouldn't", "shouldnt", "wouldn't", "wouldnt", "couldn't",
                      "couldnt", "won't", "wont", "can't", "cant", "don't", "dont")

    for index in range(len(word_list) - 1):
        if word_list[index] in negation_words:
            word_list[index + 1] = "neg_" + word_list[index + 1]
            word_list.pop(index)
    return ' '.join(word_list)
