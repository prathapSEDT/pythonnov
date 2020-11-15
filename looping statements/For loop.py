# generate range of numbers from 1-50
# print the even numbers from 1-50

# task 1: i will pass a value, your logic need to check if the number is divisible by 5 or not
#Hint apply math divisible rule
#Task 2:if i pass any value your logic should say if it is prime number or not
#Task 3: Print the numbers from 50-1 (reverse order)
#Task 4:
'''
*
**
***
****
*****


'''

#
# for i in range(51):
#     if not i%2==0:
#         print(i)


# Print 2 table
'''
2 * 1= 2
2 * 2 =4
'''
userValue=input("Enter a number 1-20")
for i in range (1,21):
    print( userValue+" * "+str(i)+" = "+str(i* int(userValue)))
    # 5 * 1 = 5, 5 * 2 = 10.....
