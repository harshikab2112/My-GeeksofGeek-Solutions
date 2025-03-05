class Solution:
    
    #Function to check if a string is subsequence of other string.
    def isSubSequence(self, A, B):
        #code here
        i=0
        for j in range(len(B)):
            if i<len(A) and A[i]==B[j]:
                i+=1
        return i==len(A)
