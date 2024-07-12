# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set cannot have duplicates
my_set2 = {1, 2, 3, 4, 3, 2}
print(my_set2)

# (***important***) we can make set from a list
my_set3 = set([1, 2, 3, 2])
print(my_set3)

# sorting
numbers = {100, 200, 300, 400}
print(sorted(numbers))  # **this will print as list, but if we convert it to set, the set won't be sorted
