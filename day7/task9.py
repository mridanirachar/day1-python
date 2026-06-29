# DAY 7 - Advanced Python
# Task: Employee Data Processing Tool

employees = [
    {"name": "John", "salary": 25000, "department": "Sales"},
    {"name": "Bob", "salary": 45000, "department": "IT"},
    {"name": "Alice", "salary": 30000, "department": "Sales"},
    {"name": "David", "salary": 60000, "department": "IT"},
    {"name": "Emma", "salary": 18000, "department": "HR"},
    {"name": "Tom", "salary": 75000, "department": "IT"},
    {"name": "Sam", "salary": 22000, "department": "HR"},
]

def report_decorator(function):
    def wrapper():
        print("\nEmployee Report")
        function()
    return wrapper

# filter()
high_salary = list(filter(lambda emp: emp["salary"] > 30000, employees))

# map()
employee_names = list(map(lambda emp: emp["name"].upper(), employees))

# comprehension
bonus_report = [
    {
        "name": emp["name"],
        "bonus_salary": emp["salary"] + (emp["salary"] * 0.10)
    }
    for emp in employees
]

# generator
def employee_generator():
    for emp in employees:
        yield emp["name"], emp["salary"], emp["department"]

@report_decorator
def show_report():
    print("Employees with salary above 30000:")
    for emp in high_salary:
        print(emp["name"], "-", emp["salary"])

print("Employee Names:")
print(employee_names)

print("\nEmployees in IT Department:")
it_employees = list(filter(lambda emp: emp["department"] == "IT", employees))
for emp in it_employees:
    print(emp["name"])

print("\nBonus Report:")
for emp in bonus_report:
    print(emp["name"], "-", emp["bonus_salary"])

show_report()

print("\nEmployee Details:")
for name, salary, department in employee_generator():
    print(name, "-", salary, "-", department)