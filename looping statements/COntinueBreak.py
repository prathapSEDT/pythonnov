'''
Continue:
this keyword it is used to skip the current iteration of the running loop
i am running a loop using "for" when i reach to the value of 5 or 6, i need skip the current transaction and i need go for the next transaction
'''

for i in range(1,11):
    print(i)

    if i==5:
        #continue
        break;

    print('''
    ***********
    -----------
    ###########
    !!!!!!!!!!!
    ***********
    ''')