# Sets
# A set is defined with curly brackets
# Sets do lookups, adds and removes in O(1) (constant) time
# A set is a collection which is unordered, unchangable* and unindexed
# *Note: set *items* are unchangable but you can remove items and add new items

# Basic modifications
set1 = {"Apple", "Banana", "Orange", "Grapes", "Cherry"}

print(set1)

# .add(element)
# Adds a single element to the set. If the element exists, nothing changes
set1.add("Mango") 

print(set1)

# .update(iterable)
# Adds multiple elements from an iterable (list, tuple, or another set)
set1.update(["Watermelon", "Pineapple"]) 

print(set1)

# .remove(element)
# Removes a specific element. Raises a KeyError if the element is not found
set1.remove("Watermelon")

# .discard(element)
# Removes a specific element. Does nothing if the element is not found
# Safer than .remove()
set1.discard("Pineapple")

print(set1)

# .pop()
# Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty
set1.pop()

print(set1)

# .clear()
# Removes all elements leaving an empty set
set1.clear()

print(set1)


# Mathematical set operations
# Python sets shine when you need to compare two or more sets
# For most of these, you can use either a *method* or an *operator*

# Pro tip: methods (like .union()) accept any iterable (list, tuple, etc) as an argument
# whereas operators (like |) require *both* sides to be actual sets

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b) # Union: {1, 2, 3, 4, 5}
print(a & b) # Intersection: {3}
print(a - b) # Difference: {1, 2} (Elements that are in set a that are not in set b)
print(a ^ b) # Symmetric difference: {1, 2, 4, 5} (Opposite of intersection)

print(a.union(b)) # Union: {1, 2, 3, 4, 5}
print(a.intersection(b)) # Intersection: {3}
print(a.difference(b)) # Difference: {1, 2} (Elements that are in set a that are not in set b)
print(a.symmetric_difference(b)) # Symmetric difference: {1, 2, 4, 5} (Opposite of intersection)

# In-place mathematical operations
# If you want to modify the original set rather than creating a new one, use these methods

a.update(b) # Modifies set a to be a union of itself and set b
a.intersection_update(b) # Keeps only elements found in both
a.difference_update(b) # Removes all elements found in set b
a.symmetric_difference_update(b) # Keeps elements found in either set, but not both

a |= b # Modifies set a to be a union of itself and set b
a &= b # Keeps only elements found in both
a -= b # Removes all elements found in set b
a ^= b # Keeps elements found in either set, but not both

# Set comparisons and relationships
# These operations return a boolean (True or False) based on how two sets relate to eachother

print(a.issubset(b)) # Checks if all elements of set a are in set b
print(a.issuperset(b)) # Checks if set a contains all elements of set b
print(a.isdisjoint(b)) # Checks if set a and set b have zero elements in common

print(a <= b) # Checks if all elements of set a are in set b
print(a >= b) # Checks if set a contains all elements of set b


# Sets cheat sheet for Codility
my_list = ["Banana", "Banana", "Apple", "Cherry", "Cherry"]

unique_items = set(my_list) # Deduplicates list. (Removes repeated elements)
print("Unique items", unique_items)

# Lightning fast lookup. Faster than doing the same with a list
if "Banana" in unique_items: print("Banana!")

set_a = {5, 6, 7, 8}

set_b = {1, 2, 3, 4, 5, 6}

# Find whats in set_a but NOT in set_b
missing_items = set_a - set_b
print(missing_items)

# Find whats common in both
common_items = set_a & set_b
print(common_items)
