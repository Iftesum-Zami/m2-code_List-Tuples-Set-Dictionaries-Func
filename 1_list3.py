list1 = ["apple", "banana", "cherry", "mango", "orange"]

print(list1 + ["tomato", 50]) # print the list1 with adding ["tomato", 50]
print(list1 * 3)
print(list1) # it will print original list, since we didn't overwrite the original one

list2 = ["apple", "banana", "cherry", "mango", "orange"]
list2[0] = "tomato"  # this will overwrite the 1st element of list2 by "tomato"
print(list2)
