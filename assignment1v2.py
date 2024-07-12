def find_duplicates(input_list):
    duplicates = []
    seen = set()
    for item in input_list:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates

# Example usage
input_list = [1, 5, 6, 5, 1, 2, 3]
duplicate_elements = find_duplicates(input_list)
print("Duplicate elements:", duplicate_elements)
