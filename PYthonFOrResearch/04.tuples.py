# Tuples Assignment

# 1. Creating a tuple
fruits = ("apple", "banana", "mango", "orange")

# printing full tuple
print("Full tuple:", fruits)


# 2. Indexing in tuple
print("First item:", fruits[0])  # apple
print("Third item:", fruits[2])  # mango


# 3. Negative indexing
print("Last item:", fruits[-1])  # orange
print("Second last:", fruits[-2])  # mango


# 4. Slicing in tuple
print("First two items:", fruits[0:2])  # apple, banana
print("From index 1:", fruits[1:])  # banana, mango, orange


# 5. Tuple with numbers
numbers = (10, 20, 30, 40, 50)

print("Numbers tuple:", numbers)

print("Sum of first two:", numbers[0] + numbers[1])


# 6. Loop through tuple
for item in fruits:
    print("Fruit:", item)
