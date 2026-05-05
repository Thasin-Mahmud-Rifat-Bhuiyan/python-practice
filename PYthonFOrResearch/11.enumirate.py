# enumerate() Assignment

# 1. simple list
fruits = ["apple", "banana", "mango"]

# using enumerate
for i, fruit in enumerate(fruits):
    # i = index, fruit = value
    print(i, fruit)


# 2. start index from 1
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)


# 3. using user input
names = []

# take 3 names from user
for i in range(3):
    name = input("Enter name: ")
    names.append(name)

# print with index
for i, name in enumerate(names):
    print("Index:", i, "Name:", name)


# 4. simple example with marks
marks = [50, 60, 70]

for i, m in enumerate(marks):
    print("Student", i, "Marks:", m)
