import copy
from collections import Counter

x = 10
y = x
y = 15

print(x)
print(y)

list1 = [1, 2, 3]
list2 = list1
list2.append(4)

print(list1)
print(list2)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(id(a))
print(id(b))
print(id(c))

original = [1, 2, [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[2][0] = 999

print(original)
print(shallow)
print(deep)

fruits = ["apple", "banana", "apple", "orange"]

print(Counter(fruits))

student = {
    "name": "Bob",
    "marks": [80, 90, 85]
}

print(student)

with open("requirements.txt", "w") as f:
    f.write("requests\n")

print("requirements.txt created")