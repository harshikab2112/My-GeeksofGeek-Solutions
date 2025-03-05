def checkPrime(num):
    if num<2:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True

def nextPrime(n):
    number=n+1
    while not checkPrime(number):
        number+=1
    return number
