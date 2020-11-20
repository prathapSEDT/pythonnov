'''
Collections are called as , collection of same or different items under a single variable
generally a variable can store max of one value one at a time, it can not store multiple values, to overcome that
collections are introduced
in python we have different types

* List
* tuple
* Set
* Dict

'''

'''
List: 
list is a dynamically growing element
List stores all the elements in the respective index order
List will preserve the order of insertion
To get the values from a list , we should retrive by index only
list in python is represented in []
'''
''' ************* List creation with static values ****************'''
mylist=['prathap','raj','krish']# 0--- prathap , 1-raj,2-krish
print(mylist[1])
for emp in mylist:

    if emp=="raj":
        print(emp)

''' *************  Add elements to the list dynamic *************'''