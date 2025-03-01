def lessThan(arr, k):
    ans = []

    # write your code below to append all numbers to ans which are less than k
    for i in arr:
        if i<k:
            ans.append(i)
    return ans
