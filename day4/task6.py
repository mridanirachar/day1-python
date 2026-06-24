# bank account system

balance = 0

def create_account(name):
    print("account created for " + name)
    print("balance is 0")

def deposit(amount):
    global balance

    if amount <= 0:
        print("wrong amount")
        return

    balance = balance + amount
    print("money added = " + str(amount))
    print("new balance = " + str(balance))

def withdraw(amount):
    global balance

    if amount > balance:
        print("not enough money")
        return False

    balance = balance - amount
    print("money taken = " + str(amount))
    print("balance left = " + str(balance))
    return True

def show_balance():
    print("your balance is " + str(balance))

def transaction_summary(name, *transactions):
    print()
    print("transaction summary")
    print("name =", name)

    for i in transactions:
        print(i)

# function using **kwargs
def account_details(**details):
    print()
    print("account details")

    print("name =", details["name"])
    print("deposit =", details["deposit"])
    print("withdraw =", details["withdraw"])
    print("balance =", details["balance"])


# main program

print("welcome to my bank")

name = input("enter your name: ")

create_account(name)

print()

deposit_amount = int(input("enter amount to deposit: "))
deposit(deposit_amount)

print()

withdraw_amount = int(input("enter amount to withdraw: "))
result = withdraw(withdraw_amount)

print()

show_balance()

if result == True:
    msg = "withdraw " + str(withdraw_amount)
else:
    msg = "withdraw failed"

transaction_summary(
    name,
    "deposit " + str(deposit_amount),
    msg
)

# account details using **kwargs
account_details(
    name=name,
    deposit=deposit_amount,
    withdraw=withdraw_amount,
    balance=balance
)