# Write a function that receives as a parameter a variable number of lists and a whole number x. 
# Return a list containing the items that appear exactly x times in the incoming lists. 

from collections import Counter

def items_appearing_x_times(x, *lists):
    combined_list = []
    for lst in lists:
        combined_list.extend(lst)

    count = Counter(combined_list)
    result = [item for item, freq in count.items() if freq == x]
    return result

# Example usage:
list1 = [1, 2, 2, 3, 4, 4, 5]
list2 = [2, 3, 3, 4, 5, 5, 6]
list3 = [1, 2, 3, 4, 5, 6, 7, 8]

x = 2
result = items_appearing_x_times(x, list1, list2, list3)

print(result)
