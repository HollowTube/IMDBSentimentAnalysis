#from sklearn.feature_selection import mutual_info_classif

from math import log

def keepImportantWords(n,x_pos,x_neg): 
    """
    x_pos is list of positive reviews (matrix)
    e.g. [["I","like","cats"],["Star","wars","is","troll"]]
    x_neg is same thing but negative
    keep words with PMI above n%
    """
    unfilteredWords = pointwiseMutualInfo(x_pos,x_neg)
    filteredWords = {}
    for words in unfilteredWords:
        if unfilteredWords[words][0]>n/100 or unfilteredWords[words][1]<-n/100:
            filteredWords[words] = unfilteredWords[words]
            
    return filteredWords
        

def pointwiseMutualInfo(x_pos,x_neg):
    wordCount = 0
    uniqueWords = {}
    
    for reviews in x_pos:
        for words in reviews:
            wordCount+=1
        
            if words not in uniqueWords:
                uniqueWords[words] = [1,1,0]
            else:
                uniqueWords[words][0]+=1
                uniqueWords[words][1]+=1
            
    for reviews in x_neg:
        for words in reviews:
            wordCount+=1
        
            if words not in uniqueWords:
                uniqueWords[words] = [1,0,1]
            else:
                uniqueWords[words][0]+=1
                uniqueWords[words][2]+=1

    wordScore={} 
    #key is word, value is array where first entry is correlation with positive review
    #and second is with negative review

    #Computes the mutual information between a word and positive
    probY = len(x_pos)/(len(x_pos)+len(x_neg)) #prob of positive
    for words in uniqueWords:
        probX = uniqueWords[words][0]/wordCount #prob of word
        probXY = uniqueWords[words][1]/wordCount #prob of getting both positive & word
        if probXY > 0:
            wordScore[words] = [log(probXY/(probX*probY),2)/-log(probXY,2),0]
            
    #Computes the mutual information between a word and negative
    probY = len(x_neg)/(len(x_pos)+len(x_neg))
    for words in uniqueWords:
        probX = uniqueWords[words][0]/wordCount
        probXY = uniqueWords[words][2]/wordCount
        if probXY > 0:
            wordScore[words] = [0,log(probXY/(probX*probY),2)/-log(probXY,2)]
    
    return wordScore