arr = tuple(map(int, input().split()))
x = int(input())

# Print the index of x in arr
for i in range(0,len(arr)):
    if arr[i]==x:
        print(i)
