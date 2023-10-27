# Write a function that receives as parameters two lists a and b and returns 
# a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)

def set_operations(a, b):
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    a_minus_b = set(a) - set(b)
    b_minus_a = set(b) - set(a)
    
    return [intersection, union, a_minus_b, b_minus_a]

# Example usage:
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
result = set_operations(list_a, list_b)

print(result)
