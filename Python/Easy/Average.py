def nonNegativeAverage(arr):
    
    #Write your code to find average of positive numbers in number list
    #Return the answer
    mydict=[]
    for i in arr:
        if i>=0:
            mydict.append(i)
            
    average=sum(mydict)/len(mydict)
    return average
