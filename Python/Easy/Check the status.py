class Solution:
    def checkStatus(self, a, b, flag):
      
        if flag:
            return (a<0 and b<0)
        return (a>=0 and b<0) or (a<0 and b>=0)
