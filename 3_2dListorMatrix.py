A = [
    [1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]
]

print("A =", A) 
print("A[1] =", A[1]) 
print("A[1][2] =", A[1][2])
print("A[0][-1] =", A[0][-1])

column = []   # empty list
for row in A:
    column.append(row[2]) # ***prints 3rd element (3rd col) of each row. [5, 9, 11]

print("3rd column =", column)
