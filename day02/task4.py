# ATM PIN Verification System

correct_pin = 1234
count = 0

while count < 3:
    pin = int(input("Enter PIN: "))

    if pin == correct_pin:
        print("Login Successful")
        print("Welcome to ATM")
        break
    else:
        print("Wrong PIN")
        count = count + 1

        if count == 3:
            print("Maximum Failed Attempts Limit Reached")
            print("Account Blocked")
        else:
            print("Try again")
            continue