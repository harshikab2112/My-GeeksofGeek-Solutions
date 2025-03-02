def doubleTup(numbers):
    
    #Write your code to create a tuple that 
    #holds 2*number 
    #Finally return the tuple
    mylist=[]
    
    for i in numbers:
        i*=2
        mylist.append(i)
    
    mytup=tuple(mylist)
    
    return mytup
