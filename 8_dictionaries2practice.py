text = "The banana is common fruit of Bangladesh. It is grown in all the districts and all the seasons. Munsigonj and Narsingdi are famous for banana . banana has several varieties such as Sagore, Shabri, Chapa, Agniswar etc. It is very nutritious and sweet.Papaw is a delicious fruit.It keeps the liver function active. The papaw is grown in all the districts and in all seasons. The coconut is a common fruit of Bangladesh. It grows in all seasons. Its water is a sweet drink and its kernel is a tasty food. The mango , the orange , the lichi , the black-berry , the jack fruits, the pineapple etc. grow in different seasons."
fruits = ["banana", "Papaw", "coconut", "black-berry", "pineapple", "lichi", "orange", "mango"]

text = text.split(" ") # this will make a list using every words of the text variable
fruitList = []
for x in text:
    if x in fruits:
        fruitList.append(x)
print(fruitList)


fruitList = set({})
for x in text:
    if x in fruits:
        fruitList.add(x)  
print(fruitList) # removes duplicate

# --- remove comments to watch results ---

# fruitList = {}
# for x in text:
#     if x in fruits:
#         fruitList[x] = 1
# print(fruitList)  # counts how many times fruits appear


# fruitList = {}
# for x in text:
#     if x in fruits:
#         if x not in fruitList.keys():
#             fruitList[x] = 1
#         else:
#             fruitList[x] += 1 
# print(fruitList) # counts how many times fruits appear
