# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 06:08:49 2019

@author: Mark Zhu
"""
import os
from MutualInfo import keepImportantWords

pos_path = "..\data\\train\\pos\\"
neg_path = "..\data\\train\\neg\\"

neg_review_list = []
pos_review_list = []
review_list = []
test_set = []

for file in os.listdir(neg_path):
    file_path = os.path.join(neg_path, file)
    fh = open(file_path, 'r', encoding="utf8")
    neg_review_list.append(fh.read())
    fh.close()
    
for file in os.listdir(pos_path):
    file_path = os.path.join(pos_path, file)
    fh = open(file_path, 'r', encoding="utf8")
    pos_review_list.append(fh.read())
    fh.close()

x_pos = []
x_neg = []

for rev in neg_review_list:
    x_neg.append(rev.split())
for rev in pos_review_list:
    x_pos.append(rev.split())
    
print(keepImportantWords(10,x_pos,x_neg))