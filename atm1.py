
def deposit(deposited_amount):
    global avail_amount
    avail_amount = avail_amount + deposited_amount
    print("You have deposited GH {} cedis in your Account.\nYour updated Account balance is {} ".format(
        deposited_amount, avail_amount))

    print_receipt(transaction_type="deposit",
                  amount=deposited_amount, balance=avail_amount)


def print_receipt(transaction_type, amount, balance):
    ask = input(
        "Do you want a receipt printed for this transaction? Y/N: ")

    if ask == "Y":
        print("Receipt printed for {} of {}. \n Your available balance is {}.".format(
            transaction_type, amount, balance))

    else:
        print("Receipt not printed ")


pin = 1234
app_state = False


id = int(input("Please enter your valid account pin number: "))
if id == 1234:
    print("Access granted.....")
    app_state = True
else:
    print("Invalid pin code. Please re-enter your valid pin")
