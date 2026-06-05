# Hashmaps
# A hashmap is implemented using the built in 'dict' (dictionary) datatype
# They have a time complexity of O(1) for lookups, insertions and deletions
# Hashmaps store key-value pairs
# Every key must be unique and immutable but the values can be anything and repeat

# Creation and basic modifications
# You will use dictionaries constantly to count frequencies or map IDs to objects

# Creates an empty dictionary
my_dict = {}
# OR
my_dict = dict()

my_dict[key] = "value" # Inserts a new key-value pair or updates the value if it already exists

del my_dict[key] # Removes the key and its value. Raises a KeyError if the key doesn't exist

my_dict.pop(key, default) # Removes the key and returns its value. If the key isn't found, it returns the default value instead of crashing

my_dict.clear() # Empties the dictionary


