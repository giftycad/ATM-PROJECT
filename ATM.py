while app_state:
    print("\n")
    print(""" ******** Welcome to T.A.G Bank! ********\n
     1. Check balance
     2. Withdraw Cash
     3. Deposit Money
     4. Quit""")
    choice = int(input("Please enter the number of your choice: "))
    if choice == 1:
        check_balance()
    elif choice == 2:
        withdrawl = float(input("Please enter amount to withdraw: "))
        withdraw(withdrawl)
    elif choice == 3:
        amt_to_deposit = float(input("Please enter amount to deposit: "))
        deposit(amt_to_deposit)
    elif choice == 4:
        print(" Thank you for banking with us!!!")
        app_state = False
    else:
        print("Invalid number choice .\t Select the correct number")
