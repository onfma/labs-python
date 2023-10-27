# Compare two dictionaries without using the operator "==" returning True or False. 
# (Attention, dictionaries must be recursively covered because they can contain other containers, 
# such as dictionaries, lists, sets, etc.)

def compare_dicts(dict1, dict2):
    if type(dict1) != type(dict2):
        return False

    if isinstance(dict1, dict):
        if set(dict1.keys()) != set(dict2.keys()):
            return False

        for key in dict1.keys():
            if not compare_dicts(dict1[key], dict2[key]):
                return False
    elif isinstance(dict1, (list, set, tuple)):
        if len(dict1) != len(dict2):
            return False

        for item1, item2 in zip(dict1, dict2):
            if not compare_dicts(item1, item2):
                return False
    else:
        if dict1 != dict2:
            return False

    return True

# Example usage:
dict1 = {'a': 1, 'b': [2, 3, {'c': 4}], 'd': (5, 6)}
dict2 = {'a': 1, 'b': [2, 3, {'c': 4}], 'd': (5, 6)}
dict3 = {'a': 1, 'b': [2, 3, {'c': 5}], 'd': (5, 6)}

result1 = compare_dicts(dict1, dict2)  # true
result2 = compare_dicts(dict1, dict3)  # false

print(result1)
print(result2)
