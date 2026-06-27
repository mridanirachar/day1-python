#User Registration Validator

import re

print("User Registration")

# patterns
username_pattern = r"^[A-Za-z]{3,}$"
email_pattern = r".+@.+\..+"
phone_pattern = r"^[6-9][0-9]{9}$"
password_pattern = r".{8,}"

username = input("Enter username: ")

while not re.match(username_pattern, username):
    print("Invalid username")
    username = input("Re-enter username: ")

print("Username is valid")

email = input("Enter email: ")

while not re.match(email_pattern, email):
    print("Invalid email")
    email = input("Re-enter email: ")

print("Email is valid")

phone = input("Enter phone number: ")

while not re.match(phone_pattern, phone):
    print("Invalid phone number")
    phone = input("Re-enter phone number: ")

print("Phone number is valid")

password = input("Enter password: ")

while not re.match(password_pattern, password):
    print("Password must be at least 8 characters")
    password = input("Re-enter password: ")

print("Password is valid")

print("\nRegistration Successful")