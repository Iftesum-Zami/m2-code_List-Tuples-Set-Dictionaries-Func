def my_function1(fname):  #Parameters
    print("Good morning!", fname)

my_function1("Emil")  #Arguments
my_function1("Tobias")
my_function1("Linus")

print("------------------------------------")

#This function expects 2 arguments, and gets 2 arguments:
def my_function2(fname, lname):
    print(fname,  lname)

my_function2("Emil", "Refsnes")

print("------------------------------------")

#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.
def my_function3(child3, child2, child1):
    print("The youngest child is", child3)

my_function3(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
