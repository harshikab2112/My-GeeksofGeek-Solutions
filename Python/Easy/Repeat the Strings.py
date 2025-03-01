def combo_string(a, b):
  # your code here
    if len(a)>=len(b):
        short=b
        longer=a
    else:
        short=a
        longer=b
    return short+longer+short
