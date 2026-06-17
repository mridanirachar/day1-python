# Employee Salary Calculator

name = input("Enter name: ")
age = int(input("Enter age: "))
salary = float(input("Enter salary: "))
exp = int(input("Enter experience: "))
perm = input("Permanent employee? (yes/no): ")

if perm == "yes":
    permanent = True
else:
    permanent = False

if exp<3:
    bonus=salary *5/100
elif exp<5:
    bonus=salary *10/100
else:
    bonus=salary *15/100

final_salary=salary+bonus


print("\nEmployee Details")
print("Name =", name)
print("Age =", age)
print("Experience =", exp)
print("Permanent Employee =", permanent)
print("Bonus =", bonus)
print("Final Salary =", final_salary)