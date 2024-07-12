carBrand =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(carBrand)
print(carBrand["brand"])
print(carBrand.get("Name", "Invalid Key")) # this works like carBrand["key"], but benefit is, it gives a default value if key is not found

print("--------------------------------------------------")

carBrand2 = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(carBrand2.items()) # gives both keys and value together as list
print(carBrand2.keys()) # gives the keys (1st column) as a list
print(carBrand2.values()) # gives the values (2nd column) as a list

print("--------------------------------------------------")

carBrand3 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020 # dictionaries will take unique keys. If multiples are there, it will take the last one
}
print(carBrand3)

print("--------------------------------------------------")

carBrand4 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x, y in carBrand4.items(): # assigns keys in x and values in y
    print(x, y)
