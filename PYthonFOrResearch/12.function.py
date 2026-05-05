# Function


# 1. Simple function (no parameter, no return)
def say_hello():
    # this function just prints a message
    print("Hello, this is a function")


say_hello()


# 2. Function with parameter
def greet(name):
    # this function takes a name and prints it
    print("Hello", name)


greet("Rahim")


# 3. Function with return value
def add(a, b):
    # this function adds two numbers and returns result
    return a + b


result = add(2, 3)
print("Sum is:", result)


# 4. Function with condition (if-else inside function)
def check_even_odd(num):
    # check number is even or odd
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


check_even_odd(5)


# 5. Function using user input
def get_square():
    # take input from user and print square
    num = int(input("Enter a number: "))
    print("Square is:", num * num)


get_square()


# 6. Function with default parameter
def country(name="Bangladesh"):
    # default value use kora hocche
    print("Country:", name)


country()
country("India")
