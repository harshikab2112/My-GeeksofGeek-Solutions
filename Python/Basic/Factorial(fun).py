def nFactorial(n):
    
    ans = 1
    
    
    #Write your code below
    if n==0 or n==1:
        return ans
    else:
        for i in range(2,n+1):
            ans*=i
    return ans
