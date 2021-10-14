import sys, os, time, re

class ATM:
    def __init__(self,name):
        self.name=name

#function that gives the info of the customers
    def account_info(self):
        print('Account Information: ')
        print('Name: ', name, end='\n')
        print('Account Number: ', info[name][0], end='\n')

#function to enable customers change their pin
    def pin_change(self):
        i=2
        while(i>0):
            p=int(input('Enter Original PIN: '))
            if p==info[name][1]:
                x=input('Enter New PIN: ')
                info[name][1]=x
                break
            else:
                i=i-1
                print('PIN incorrect, {} tries left'.format(i))
        if i==0:
            del info[name]
            print('Account Blocked!')

# Function to show account balance
    def account_balance(self):
        print('Account Balance: ',info[name][2])

#function to make a withdrawal
    def withdrawal(self):
        print('Account Balance: ',info[name][2])
        amt=float(input('Enter Amount To Be Withdrawn: '))
        if amt<=info[name][2]:
            info[name][2]=info[name][2]-amt
            print('New Account Balance is : ', info[name][2])
        else:
            print('Insufficient Balance in Account!')

#function to make deposits
    def deposit(self):
        amt=float(input('Enter Amount To Be Deposited: '))
        info[name][2]=info[name][2]+amt
        print('New Account Balance: ', info[name][2])

# python dictionary to store details of customers, ie their names, account numbers, ATM PIN and their available balance
info={"Ralph":[1234567,4000,12000.00], "Nana Kwame":[89101112,5000,27000.00], 'Gifty':[1314151617,6000,100000.00], 
       "Mawunyo":[666981111,7000,17000.00], "Raymond":[23456789,7777,10500.00] ,"Wadi":[23456789,7777,10500.00],"Effiansah":[23456789,7777,10500.00]}
k=info.keys()

flash = "* * * * * T A G   B A N K   G H A N A * * * * *\n"
for char in flash:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)
while (1):
    name=str(input('Enter Name: '))
    if name in k:
        i=2
        while(i>0):
            pin=int(input('Enter PIN: '))
            if pin==info[name][1]:
                print("...........Access Granted........")
                a=ATM(name)
                print("\n")
                while(1):
                    print('Enter 1 For Account Info')
                    print('Enter 2 For PIN Change')
                    print('Enter 3 For Balance Inquiry')
                    print('Enter 4 For Withdrawal')
                    print('Enter 5 For Deposit')
                    s=int(input('Select your choice: '))
                    if s==1:
                        a.account_info()
                    elif s==2:
                        a.pin_change()
                    elif s==3:
                        a.account_balance()
                    elif s==4:
                        a.withdrawal()
                    elif s==5:
                        a.deposit()
                    else:
                        print('Invalid Option Selected! Choose Again')
                        continue
                    e=input('Enter Y to exit, press any other key to continue operations: ')
                    if e=='y' or e=='Y':
                        print('Thank You for banking with us!')
                        break
                    else:
                        continue
                break
            else:
                i=i-1
                print('Incorrect PIN, {} tries left'.format(i))
        if i==0:
            del info[name]
            print('Account Blocked!')
        break