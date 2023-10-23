# Write a function that receives a variable number of lists and returns a list of 
# tuples as follows: the first tuple contains the first items in the lists,
# the second element contains the items on the position 2 in the lists, etc.

def zip_lists(*lists):
    max_length = max(len(lst) for lst in lists)
    zipped = []

    for i in range(max_length):
        zipped_tuple = tuple(lst[i] if i < len(lst) else None for lst in lists)
        zipped.append(zipped_tuple)

    return zipped

# Example usage:
list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]
result = zip_lists(list1, list2, list3)

print(result)
