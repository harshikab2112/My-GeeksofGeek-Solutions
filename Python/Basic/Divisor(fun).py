def divisor(n):
    # Complete the code given below
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")
