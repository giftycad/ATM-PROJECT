avail_amount = 5000
def check_balance():
    print("Your Account balance is GH {} cedis ".format(avail_amount))
def withdraw(withdrawal_amount):
    global avail_amount
    avail_amount = avail_amount - withdrawal_amount
    if (avail_amount <= withdrawal_amount):
        print("Insufficient funds..")
    else:
        print("Your Account balance is GH {} gh cedis ".format(avail_amount))
        print("Your updated Account balance is GH {} cedis ".format(avail_amount))
    print_receipt(transaction_type="withdrawal",
                  amount=withdrawal_amount, balance=avail_amount)