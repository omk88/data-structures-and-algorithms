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
# When you need to process the data you've collected, you can loop through keys, values or both

for key in my_dict: # Loop through the keys by default
    print(key)

for value in my_dict.values(): # Loop through only the values
    print(value)

for key, value in my_dict.items(): # Loop through both keys and values
    print(key, value)

# Looping through both keys and values
scores = {'Alice': 95, 'Bob': 88}

for name, score in scores.items():
    print(f"{name} scored {score}")


# Advanced / Shortcut syntaxes
# To write fast, bug free code under a timer, Python provides two powerful tools in its standard library that interviewers love

# A. collections.defaultdict
# When counting frequencies in a standard dictionary, you usually have to write code like this

# The tedious way
if item not in counts:
    counts[item] = 0
counts[item] += 1

# A defaultdict automates this. If a key doesn't exist, it automatically initialises it with a default value (like 0 for integers)
from collections import defaultdict

# Tell it to default to integers (which start at 0)
counts = defaultdict(int)

for item in ['a', 'b', 'c']:
    counts[item] += 1 # No 'if item not in counts' check needed!

# Result: {'a': 2, 'b': 1}

# B. collections.counter
# If your goal is literally just to count how many times items appear in a list, Python has a build in hashmap subclass that does it in just one line

from collections import Counter

my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

counts = Counter(my_list)

print(counts)           # Counter({'banana': 3, 'apple': 2, 'orange': 1})
print(counts['apple'])  # 2


# Use a set if you only care about *presence* (have I seen this number before)
# Use a hashmap (dict) if you care about association or frequency. (How many times have I seen this number? Or, which index have I seen this number at?)