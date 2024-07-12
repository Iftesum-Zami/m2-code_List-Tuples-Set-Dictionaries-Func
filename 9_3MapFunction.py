

def myfunc(a):
    return len(a)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))

print("---------------")

def square(x):
    return x*x
num = [1, 2, 3, 4, 5]
result = list(map(square, num))
print(result)
