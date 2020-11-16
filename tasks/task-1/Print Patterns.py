
'''
*
**
***
****
*****
'''

'''
intailly i=1
i=2

'''
ptrn="*"
uma=""
for i in range(1,6):
    for j in range(1,i+1):#1,2, (2,3),(3,3),
        uma=uma+ptrn
    print(uma)
    uma=""