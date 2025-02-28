def find_greatest_number(a, b, c):
    # Write your code here
    if a>=b and a>=c:
        return a
    elif b>=c and b>=a:
        return b
    else:
        return c
