# Dictionary Assignment (Model Configuration Example)

# 1. Creating a simple dictionary (model config)
model_config = {
    "model_name": "SimpleAI",
    "version": 1.0,
    "language": "English",
    "max_tokens": 1000,
}

# printing full dictionary
print("Model Config:", model_config)


# 2. Accessing values using keys
print("Model Name:", model_config["model_name"])
print("Version:", model_config["version"])


# 3. Adding new key-value pair
model_config["author"] = "Student"

print("After adding author:", model_config)


# 4. Updating value
model_config["version"] = 2.0

print("After update:", model_config)


# 5. Removing a key
del model_config["max_tokens"]

print("After deleting max_tokens:", model_config)


# 6. Loop through dictionary
for key in model_config:
    print(key, ":", model_config[key])
