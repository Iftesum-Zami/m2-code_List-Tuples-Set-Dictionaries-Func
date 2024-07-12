# using default argument

def my_function(country = "Norway"):
    print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_function2(x):
    return 5 * x

print(my_function2(3))
print(my_function2(5))
print(my_function2(9))


def Add(a, b):
    '''
    This will take two parameter
    Return value is integer
    '''
    return a + b


print(Add(10, 20))
print(Add.__doc__)

