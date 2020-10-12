"""
References : 1. https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/
"""
def count(list1):
# Converting list to upper case
    l = [x.upper() for x in list1]
# create a empty dict    
    items = {}
#loop over the list
    for i in l:
#check if i is "in" items if true increment [1] 
        if i in items:
            items[i] +=1
        else:
            items[i] = 1
    return items
input = ['A', 'a', 'B', 'c', 'A'] 
print(count(input))
