print((lambda a : a + 10) (5))


x = lambda a : a + 10  # x is the name of function
print(x(5))


x1 = lambda a, b, c : a + b + c
print(x1(5, 6, 2))


def cube(y):
    return y * y * y
print(cube(5))


# using the lambda function
lambda_cube = lambda y: y * y * y
print(lambda_cube(5))

