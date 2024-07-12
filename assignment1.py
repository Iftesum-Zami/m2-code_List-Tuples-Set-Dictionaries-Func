numbers = [1, 5, 6, 5, 1, 2, 3] 
duplicate = [] 
for num in numbers: 
    if numbers.count(num) > 1:  # for selecting the numbers which occur more than 1 time 
        if num not in duplicate:  # not for repeating the selected numbers 
            duplicate.append(num) 
print("The list of duplicate numbers:", duplicate)