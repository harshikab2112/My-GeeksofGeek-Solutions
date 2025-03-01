st = {int(x) for x in input().split()}
i = int(input())
r = int(input())

########### Write your code below ###############
# Insert i in set
st.add(i)

########### Write your code above ###############

# Printing the set
for i in sorted(st):
    print (i, end=' ')
print()

########### Write your code below ###############
# Remove r from set
st.remove(r)
########### Write your code above ###############

# Printing the set
for i in sorted(st):
    print (i, end=' ')
print()

########### Write your code below ###############
sum = sum(st)# Sum of set elements
########### Write your code above ###############

# Print sum of set
print(sum)
