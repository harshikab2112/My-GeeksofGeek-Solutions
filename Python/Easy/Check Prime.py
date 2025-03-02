n = int(input())

# Your code here
if n<2:
    print(False)
else:
    x=int(n**0.5)+1
    for i in range(2,x):
        if n%i==0:
            print(False)
            break
    else:
        print(True)
