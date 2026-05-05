# User Input Assignment

# 1. Taking simple input
name = input("Enter your name: ")
print("Your name is:", name)


# 2. Taking number input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# adding numbers
sum = num1 + num2
print("Sum is:", sum)


# 3. Even or odd using input
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 4. Using float input
price = float(input("Enter price: "))
quantity = float(input("Enter quantity: "))

total = price * quantity
print("Total cost:", total)


# 5. Multiple input in one line
a, b = input("Enter two numbers: ").split()

# convert to int
a = int(a)
b = int(b)

print("Addition:", a + b)


# 6. Simple calculator
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Add:", x + y)
print("Sub:", x - y)
print("Mul:", x * y)
print("Div:", x / y)
