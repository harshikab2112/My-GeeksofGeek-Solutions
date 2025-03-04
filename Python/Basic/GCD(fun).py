def gcd(a, b):
    
    # code here to calculate and return gcd of a and b
    while b:
        a,b=b,a%b
    return a
