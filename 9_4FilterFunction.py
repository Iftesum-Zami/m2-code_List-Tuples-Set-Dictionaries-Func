ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
    if x < 18:
        return False
    else:
        return True
    
adults = list(filter(myFunc, ages))
print(adults)

print("-------------------------")

num = [5, 12, 17, 18, 25, 32]
result = list(filter(lambda x: x%2 == 0, num))
print(result)
print(num)