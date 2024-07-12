list1 = ["Apple", "Banana", "Cherry", "Mango", "Guava"]

print(list1[0:2])
print(list1[2:])
print(list1[-1])
print(list1[-3:-1])
print(list1[0:5])
print(list1[0:5:2])

print(list1[-1:-2])  # start index is greater than stop index and default step size is +1(on the right). 
# So it returns an empty list. 

print(list1[-1:-2:-1])  # for the step size -1, it moves one step backwards(on the left)
