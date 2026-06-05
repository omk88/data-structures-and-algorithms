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


# Initialising
counts = {"apple": 2, "banana": 5}

# Adding / Updating
counts["orange"] = 1 # Inserts: {'apple': 2, 'banana': 5, 'orange': 1}
counts["apple"] = 3 # Updates: {'apple': 3, 'banana': 5, 'orange': 1}

# Safe deletion
counts.pop("pear", 0) # Returns 0 because 'pear' doesn't exist in the dictionary. No error thrown


# Safe lookups (Crucial for Codility)
# In an exam, trying to access a key that isn't in your map will crash your program
# You must know how to safely look up values

# The 'in' keyword checks if a key exists in a dictionary
# .get(key, default) fetches the value for key. If the key does not exist, it returns the default value instead of raising an error

counts = {"apple": 3, "banana": 5}

# Method 1: Explicit check
if "pear" in counts:
    print(counts["pear"])

# Method 2: The .get() method (cleaner and highly recommended)
pear_count = counts.get("pear", 0) # Returns 0 because 'pear' does not exist
apple_count = counts.get("apple", 0) # Returns 3


# Iterating (looping) through hashmaps
