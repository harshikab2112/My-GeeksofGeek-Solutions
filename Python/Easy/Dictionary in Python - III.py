#User function Template for python3

# insert into dictionary
def insert_dict(query, dict):
    
    # Your code here
    key,value=query[1],int(query[2])
    dict[key]=value

# deleting from dictionary
def del_dict(query, dict):
    
    # Your code here
    key=query[1]
    if key in dict:
        del dict[key]
    else:
        print(-1)

# print marks of required name
def print_dict(key, dict):
    
    # Your code here
    if key in dict:
        print(f"Marks of {key} is {dict[key]}")
    else:
        print(-1)
