def isPalindrome(s):
    #Your code below
    #Remeber to ignore the case when comparing
    t=s.lower()
    if t==t[::-1]:
        return True
    else:
        return False
