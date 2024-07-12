input_list = [1, 5, 6, 5, 1, 2, 3]
duplicates = []

for i in range(len(input_list)):
    for j in range(i + 1, len(input_list)):
        if input_list[i] == input_list[j] and input_list[i] not in duplicates:
            duplicates.append(input_list[i])

print("Duplicate elements:", duplicates)
