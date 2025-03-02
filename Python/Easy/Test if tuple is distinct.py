arr = tuple(map(int, input().split()))

########### Write your code below ###############
# Print "True" if all elements of tuple are different, otherwise print "False"

present=set()
flag=True

for i in arr:
    if i in present:
        flag=False
        break
    present.add(i)
    
print(True if flag else False)

########### Another approach ############

if len(set(arr))==len(arr):
    print(True)
else:
    print(False)
