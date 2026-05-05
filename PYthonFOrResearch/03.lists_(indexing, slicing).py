# Lists Assignment (Indexing & Slicing)

# 1. Creating a list
fruits = ["apple", "banana", "mango", "orange", "grapes"]

# printing full list
print("Full list:", fruits)


# 2. Indexing (accessing single item)
print("First item:", fruits[0])  # apple
print("Third item:", fruits[2])  # mango


# 3. Negative indexing
print("Last item:", fruits[-1])  # grapes
print("Second last:", fruits[-2])  # orange


# 4. Slicing (part of list)
print("First three items:", fruits[0:3])  # apple, banana, mango

print("From index 2 to end:", fruits[2:])  # mango, orange, grapes

print("Middle items:", fruits[1:4])  # banana, mango, orange


# 5. Slicing with step
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Every second number:", numbers[0:9:2])  # 1,3,5,7,9


# 6. Simple loop with list
for item in fruits:
    print("Fruit:", item)
