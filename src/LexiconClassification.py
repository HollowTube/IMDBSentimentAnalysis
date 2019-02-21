def LexiconClassifier(positiveReview,negativeReview): #counts occurances of each word 
    occurDict = {}
    
    for review in positiveReview:
        for words in review:
            if words not in occurDict:
                occurDict[words] = 1
            else:
                occurDict[words]+=1

    for review in negativeReview:
        for words in review:
            if words not in occurDict:
                occurDict[words] = -1
            else:
                occurDict[words]-=1
            
    return occurDict