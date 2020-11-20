list1=['a',4,7,2,9,3]

list2=['1',6,8,9,4,6]

'''
to add all the elements of a given list into another list , we use a method called extend
this method will add all the elements in the last of the give list
this method will not return any new list
if we try to save into a varibal will get the output as None
'''
list1.extend(list2)
print(list1)
