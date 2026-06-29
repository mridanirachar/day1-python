# DAY 5 - ATM Application

import datetime
import random
import math


class WrongPinError(Exception):
    pass


class LowBalanceError(Exception):
    pass


class WithdrawalLimitError(Exception):
    pass


correct_pin = 1234
balance = 5000

print("WELCOME TO PYTHON ATM")

now = datetime.datetime.now()
print("Date and Time:", now.strftime("%d-%m-%Y %H:%M:%S"))

pin_tries = 0
pin_ok = False

while pin_tries < 3:
    try:
        entered_pin = int(input("Enter your 4 digit PIN: "))

        if entered_pin != correct_pin:
            raise WrongPinError("Wrong PIN")
        else:
            print("PIN Verified")
            pin_ok = True
            break

    except WrongPinError as e:
        pin_tries += 1
        print(e)
        print("Attempts left:", 3 - pin_tries)

    except ValueError:
        print("Enter numbers only")

    finally:
        print("PIN check completed")

if not pin_ok:
    print("Too many wrong attempts. Card blocked.")
    exit()

while True:
    print("\n1. Withdraw Money")
    print("2. Deposit Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amt = float(input("Enter amount to withdraw: "))

            if amt <= 0:
                print("Amount must be greater than 0")
                continue

            if amt > 10000:
                raise WithdrawalLimitError("Maximum withdrawal amount reached")

            otp = random.randint(1000, 9999)
            print("your OTP is:", otp)

            users_otp = int(input("enter your OTP: "))

            if users_otp != otp:
                print("Invalid OTP")
                continue

            amt = math.ceil(amt)

            if amt > balance:
                raise LowBalanceError("Insufficient Balance")

            balance -= amt

            print("Withdrawal Successful")

        except WithdrawalLimitError as e:
            print(e)

        except LowBalanceError as e:
            print(e)

        except ValueError:
            print("Enter a valid amount")

        finally:
            print("Current Balance:", balance)

    elif choice == "2":
        try:
            amt = float(input("Enter amount to deposit: "))

            if amt <= 0:
                print("Amount must be greater than 0")
                continue

            amt = math.ceil(amt)
            balance += amt

            print("Deposit Successful")

        except ValueError:
            print("Enter a valid amount")

        finally:
            print("Current Balance:", balance)

    elif choice == "3":
        print("Current Balance:", balance)

    elif choice == "4":
        print("Thank You For Using ATM")
        print("Session Ended At:", datetime.datetime.now().strftime("%H:%M:%S"))

        trans_id = random.randint(1000, 9999)
        print("Transaction ID:", trans_id)

        break

    else:
        print("Invalid Choice")