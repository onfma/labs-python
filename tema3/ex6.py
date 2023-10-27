# Write a function that receives as a parameter a list and returns a tuple (a, b), 
# representing the number of unique elements in the list, and b representing the number of duplicate 
# elements in the list (use sets to achieve this objective).

def count_unique_and_duplicates(input_list):
    unique_elements = set()
    duplicate_elements = set()
    
    for item in input_list:
        if item in unique_elements:
            duplicate_elements.add(item)
        else:
            unique_elements.add(item)
    
    a = len(unique_elements)
    b = len(duplicate_elements)
    
    return a, b

# Example usage:
my_list = [1, 2, 2, 3, 4, 4, 5]
result = count_unique_and_duplicates(my_list)

print(result)
