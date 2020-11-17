'''
Write a program to print fibonical series of number available 1-5
9
a=0
b=1
print(a)
print(b)


'''

def print_febonical(n):
    a=0
    b=1
    print(a)
    for i in range(2,n):
        print(b)
        c=a+b
        a=b
        b=c

print_febonical(9)

