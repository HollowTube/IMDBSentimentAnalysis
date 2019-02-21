# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 09:08:51 2019

@author: Mark Zhu
"""

from math import log

x_pos = [["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"],
        ["All","men","must","die"]]
x_neg = [["All","children","must","live"],
         ["All","children","must","stop","die","okay"],
         ["All","children","must","live"],
         ["All","children","must","stop","die","okay"],
         ["All","children","must","live"],
         ["All","children","must","stop","die","okay"],
         ["All","children","must","live"],
         ["All","children","must","stop","die","okay"],
         ["All","children","must","live"],
         ["All","children","must","stop","die","okay"],
         ["children","must","live"],
         ["All","children","must","stop","die","okay"]]

wordCount = 0
uniqueWords = {}
for reviews in x_pos:
    for words in reviews:
        wordCount+=1
        
        if words not in uniqueWords:
            uniqueWords[words] = [1,1]
        else:
            uniqueWords[words][0]+=1
            uniqueWords[words][1]+=1
            
for reviews in x_neg:
    for words in reviews:
        wordCount+=1
        
        if words not in uniqueWords:
            uniqueWords[words] = [1,0]
        else:
            uniqueWords[words][0]+=1
            

print(wordCount)
print(uniqueWords)
#wordCount now holds total number of words

probY = len(x_pos)/(len(x_pos)+len(x_neg))
print(probY)
for words in uniqueWords:
    probX = uniqueWords[words][0]/wordCount
    probXY = uniqueWords[words][1]/wordCount
    print("{} and {} and {}".format(probX,probY,probXY))
    if probXY > 0:
        #selfInfo = -log(probXY,2)
        #print("{} and {}".format(probXY,selfInfo))
        #print("{}: {}".format(words,log(probXY/(probX*probY))/selfInfo,2))
        print("{}: {}".format(words,log(probXY/(probX*probY),2)/-log(probXY,2)))
