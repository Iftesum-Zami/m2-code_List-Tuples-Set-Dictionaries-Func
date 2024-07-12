fruits = ("apple", "banana", "cherry")
# green = fruits[0]
# yellow = fruits[1]
# red = fruits[2]
(green, yellow, red) = fruits # instead of previous 3 lines

print(green)
print(yellow)
print(red)


fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green2, yellow2, *red2) = fruits2

print(green2) # 1st
print(yellow2) # 2nd
print(red2) # 3,4,5th


fruits3 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(*green3, yellow3, red3) = fruits3

print(green3) # 1, 2, 3
print(yellow3) # 4th
print(red3) # 5th


fruits4 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green4, *yellow4, red4) = fruits4

print(green4) # 1st
print(yellow4) # 2, 3, 4
print(red4) # 5th
