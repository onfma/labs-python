# The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules 
# for a dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows: 
# (key, "prefix", "middle", "suffix"). A value is considered valid if it starts with "prefix", 
# "middle" is inside the value (not at the beginning or end) and ends with "suffix". 
# The function will return True if the given dictionary matches all the rules, False otherwise.

def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key in dictionary:
            value = dictionary[key]
            if (prefix == "" or value.startswith(prefix)) and (suffix == "" or value.endswith(suffix)) and middle in value[1:-1]:
                continue
            else:
                return False
        else:
            return False
    return True

# Example usage:
rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
data = {
    "key1": "come inside, it's too cold out",
    "key2": "start with winter, end with winter",
    "key3": "this is not valid"
}

result = validate_dict(rules, data)

print(result)
