myList=list() # This line will create a empty list

''' add elements to the list in run time'''

''' 
Append: this method is used to add elements to the list
Every time you add a element, it will add at the last position of the list
'''
import random

i=1

while i<=10:
    user="User"+str(random.randrange(1,50))
    myList.append(user)
    i+=1
print(myList)
