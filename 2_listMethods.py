# most of the list methods showed here overwrites the original on 
# so be carefull and dont use them as variable

fruits1 = ['apple', 'banana', 'cherry']
fruits1.append("orange") # Adds an element at the end of the list
print(fruits1)

fruits2 = ['apple', 'banana', 'cherry', 'orange']
fruits2.clear() # Removes all the elements from the list 
print(fruits2)

fruits3 = ["cherry", "apple", "banana", "cherry"]
x = fruits3.count("cherry") # Returns the number of elements with the specified value (don't overwrite, take info)
print(x)

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars) # Add the elements of a list (or any iterable), to the end of the current list
print(fruits) # prints elements of fruits then cars

fruits4 = ['apple', 'banana', 'cherry']
x = fruits4.index("cherry") # Returns the index of the specified value
print(x)

fruits5 = ['apple', 'banana', 'cherry']
fruits5.insert(1, "orange") # Adds an element at the specified position
print(fruits5)

fruits6 = ['apple', 'banana', 'cherry']
fruits6.pop(1) # Removes the element at the specified position. If no parameter given, removes last one by default
print(fruits6)

fruits7 = ['apple', 'banana', 'cherry']
fruits7.remove("banana") # Removes the first item with the specified value
print(fruits7)

fruits8 = ['apple', 'banana', 'cherry']
fruits8.reverse() # Reverses the order of the list (descending when numeric values)
print(fruits8)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort() # Sorts the list (ascending when numeric values)
print(cars)
# cars.sort(reverse=False) 

