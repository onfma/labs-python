# Write a function that receives as parameters two lists a and b and returns: 
# (a intersected with b, a reunited with b, a - b, b - a)

def list_operations(a, b):
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))
    return intersection, union, a_minus_b, b_minus_a

# Example usage:
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
result = list_operations(list_a, list_b)

intersection, union, a_minus_b, b_minus_a = result
print("Intersection:", intersection)
print("Union:", union)
print("a - b:", a_minus_b)
print("b - a:", b_minus_a)
