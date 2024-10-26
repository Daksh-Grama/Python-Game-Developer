# Dictionaries
# 1. Dictionaries are another kind of data type in python
# 2. Dictionaries are represented using curly brackets
# 3. Dictionaries store items in the form of key value pair eg : {"name" : "Daksh"}. Here name is the key and Daksh is the value.
# 4. Dictionary keys can have similar values
# 5. Keys in dictionary should be unique, if keys are repeated then previous value gets replaced with the latest value
# 6. Values in dictionary can only be accessed through the keys

sample_dictionary = {"name" : "Daksh", "age" : 10, "city" : "Luxembourg"}
print(sample_dictionary)

# Fetching a value from dictionary
print(sample_dictionary["city"])

# adding an item in dictionary
sample_dictionary["profession"] = "Swimming"
print("\n")
print(sample_dictionary)

# deleting an item from dictionary
del sample_dictionary["age"]
print(sample_dictionary)

sample_dictionary = {'name': 'Daksh', 'city': 'Luxembourg', 'profession': 'Swimming', "name" : "Daksh Grama", "place" : "Luxembourg", 
                     1234 : 5678, 987 : "Test Value"}
print("\n")
print(sample_dictionary)

print("\n")

# Checking all keys in a dictionary
print(sample_dictionary.keys())

# Checking all values in a dictionary
print(sample_dictionary.values())

print("\n")
# Checking all items in a dictionary
print(sample_dictionary.items())