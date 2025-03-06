def sequence(tup):
    # code here to return tuple containing whole sequences
    d=tup[1]-tup[0]
    for _ in range(3):
        tup+=(tup[-1]+d,)
    return tup
