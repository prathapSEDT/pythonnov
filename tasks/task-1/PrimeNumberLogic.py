'''
the number should get divisble by 1 and it self

the user provide a a value =5
1,2,3,4,5

'''
divisibleCount=0
userInput=input("Enter a number")
for x in range(1,int(userInput)+1):
    if int(userInput) % x==0:
        divisibleCount+=1
if divisibleCount==2:
    print("The user given number "+userInput+"  is a prime number")
else:
    print("The user given number is not a prime number")
