def pair_sum(dict, arr, sum):
    vis = set()
    for num in arr:
        if sum - num in vis:
            return True
        vis.add(num)
    return False
