# List Comprehension

# 1. simple list creation
numbers = [i for i in range(1, 6)]
print(numbers)

# 2. squares using list comprehension
squares = [i * i for i in range(1, 6)]
print(squares)


# Dictionary Comprehension

# 3. simple dictionary
square_dict = {i: i * i for i in range(1, 6)}
print(square_dict)

# 4. only even numbers in dictionary
even_dict = {i: i * i for i in range(1, 11) if i % 2 == 0}
print(even_dict)
