# Set Assignment

# 1. Creating a set
fruits = {"apple", "banana", "mango", "apple", "banana"}

# printing set (duplicates will be removed automatically)
print("Fruits set:", fruits)


# 2. Adding an item to set
fruits.add("orange")

print("After adding:", fruits)


# 3. Removing an item from set
fruits.remove("banana")

print("After removing banana:", fruits)


# 4. Checking item in set
print("mango in set?", "mango" in fruits)
print("grape in set?", "grape" in fruits)


# 5. Loop through set
for item in fruits:
    print("Fruit:", item)


# 6. Another set example (numbers)
numbers = {1, 2, 3, 4, 5}

print("Numbers set:", numbers)
