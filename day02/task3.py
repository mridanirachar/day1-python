# Employee Attendance Management System

n = int(input("Enter number of employees: "))

for i in range(n):
    print("\nEmployee", i + 1)

    name = input("Enter name: ")
    working = int(input("Enter working days: "))
    present = int(input("Enter present days: "))
    rating = int(input("Enter performance rating: "))

    attendance = (present / working) * 100

    print("\nName:", name)
    print("Attendance:", attendance, "%")

    if attendance >= 90:
        print("Bonus Eligible")
    else:
        print("Not Eligible for Bonus")

    if rating >= 8:
        print("Performance: Excellent")
    elif rating >= 5:
        print("Performance: Good")
    else:
        print("Performance: Poor")