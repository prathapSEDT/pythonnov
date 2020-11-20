''' I want to add 13 elements to my list'''
''' U should not write not more than one line '''

''' List comprehension '''
'''
This list comprehension offers a shotrest path to access or modilfy the list
When we want to create a new list, based on some input values, use list comprehension
*** input must be iteratble
Ex: range, random, list, dict
'''

'''
Syntax:
newlist=[ variable for variable in iteratbleObject if condition==True]
'''
newlist=[x for x in range(1,101) if not x%2==0]
print(newlist)