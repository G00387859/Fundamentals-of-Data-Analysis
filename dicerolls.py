##
#November 2nd, 2020: Write a Python function called dicerolls that simulates
#rolling dice. 
# Your function should take two parameters: the number of dice k and
#the number of times to roll the dice n. The function should simulate randomly
#rolling k dice n times, keeping track of each total face value. It should then return
#a dictionary with the number of times each possible total face value occurred. So,
#calling the function as diceroll(k=2, n=1000) should return a dictionary like:
#{2:19,3:50,4:82,5:112,6:135,7:174,8:133,9:114,10:75,11:70,12:36}
#You can use any module from the Python standard library you wish and you should
#include a description with references of your algorithm in the notebook.

import random


def count(list1):
# Converting list to upper case
    #l = [x.upper() for x in list1]
# create a empty dict [2]   
    items = {}
#loop over the list
    for i in list1:
#check if i is "in" items if true increment [1] 
        if i in items:
            items[i] +=1
        else:
            items[i] = 1
    return items

#k = the number of the dice. There are k dice
#n = the number of times the dice is rolled
def diceroll(k,n):
    list1 = []
        #roll the dice
    for _ in range(n-1):#for x in range(6)
        random_integer = random.randint(1, 6*k)
       # print(random_integer)
        list1.append(random_integer)
    return list1
print(count(diceroll(3,1000)))
#print(diceroll(3,10))

