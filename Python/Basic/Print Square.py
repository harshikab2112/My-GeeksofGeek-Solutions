def square(s):
    #Complete the code given below
    for i in range(1,s+1):
        for j in range(1,s+1):
            if i==1 or i==s or j==1 or j==s:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
