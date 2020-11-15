'''
when i input a value rages between 1-7
if value=1 (monday)
value=2(tuesday)
'''

userInput=int(input("Enter a value in range of 1- 7 : "))

if userInput>=1 and userInput <=7:

    if userInput==1:
        print("Monday")
    elif userInput==2:
        print("Tuesday")
    elif userInput==3:
        print("Wednesday")
    elif userInput == 4:
        print("Thrusday")
    elif userInput==5:
        print("Friday")
    elif userInput == 6:
        print("Saturday")
    elif userInput == 7:
        print("Sunday")


else:
    print("Input a number ranges in between 1-7")