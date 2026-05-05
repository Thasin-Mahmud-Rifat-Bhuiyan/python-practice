# Loop Assignment

# 1. Simple for loop (print 1 to 5)
for i in range(1, 6):
    # print numbers
    print(i)


# 2. for loop with sum
total = 0

for i in range(1, 6):
    # adding numbers
    total = total + i

print("Sum is:", total)


# 3. while loop (print 1 to 5)
i = 1

while i <= 5:
    print(i)
    i = i + 1


# 4. even numbers using loop
for i in range(1, 11):
    if i % 2 == 0:
        print("Even:", i)


# 5. user input with loop
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i)


# 6. simple multiplication table
num = int(input("Enter a number for table: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# 7. break example
for i in range(1, 10):
    if i == 5:
        break  # stop loop at 5
    print(i)


# 8. continue example
for i in range(1, 10):
    if i == 3:
        continue  # skip 3
    print(i)
