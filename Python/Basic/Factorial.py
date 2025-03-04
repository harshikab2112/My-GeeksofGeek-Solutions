n = int(input())

# Your code here
factorial=1
if n==0 or n==1:
    print(factorial)
else:
    for i in range(2,n+1):
        factorial*=i
    print(factorial)
