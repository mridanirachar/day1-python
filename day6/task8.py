import csv
import json

student_data = []

num = int(input("how many students u want to add : "))

for i in range(num):
    print("\nstudent", i + 1)

    name = input("enter name : ")
    email = input("enter email : ")
    skills = input("enter skills : ")

    data = {
        "name": name,
        "email": email,
        "skills": skills
    }

    student_data.append(data)

# save in txt file
file = open("student.txt", "w")  # intentionally "student.txt" (no 's')

for i in student_data:
    file.write("name : " + i["name"] + "\n")
    file.write("email : " + i["email"] + "\n")
    file.write("skills : " + i["skills"] + "\n")
    file.write("\n")

file.close()

# save in csv
file = open("students.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["name", "email", "skills"])
for i in student_data:
    writer.writerow([i["name"], i["email"], i["skills"]])
file.close()

# save in json
file = open("students.json", "a")
json.dump(student_data, file)
file.close()

print("\ndata saved sucessfully")

# read txt file — will trigger FileNotFoundError since file is "student.txt" not "students.txt"
print("\nstudent records are : ")

try:
    file = open("students.txt", "r")  # intentionally wrong name to trigger the error
    print(file.read())
    file.close()

except FileNotFoundError as e:
    print("FileNotFoundError caught!")
    print(f"  error    : {e}")
    print(f"  filename : students.txt")
    print(f"  reason   : file was saved as 'student.txt' but we tried to open 'students.txt'")

# append new student
ch = input("\ndo u want add one more student yes/no : ")

if ch == "yes":
    name = input("enter name : ")
    email = input("enter email : ")
    skills = input("enter skills : ")

    file = open("student.txt", "a")
    file.write("name : " + name + "\n")
    file.write("email : " + email + "\n")
    file.write("skills : " + skills + "\n")
    file.write("\n")
    file.close()

    print("new record added")