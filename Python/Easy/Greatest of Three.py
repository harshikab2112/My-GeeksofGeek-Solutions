# Take a, b and c input and print the greatest of three
a=int(input())
b=int(input())
c=int(input())

if a>=b and a>=c:
    print(a)
elif b>=c and b>=a:
    print(b)
else:
    print(c)
