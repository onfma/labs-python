# Write a function that receives a variable number of positional arguments and a variable number of keyword 
# arguments adn will return the number of positional arguments whose values can be found among keyword arguments values.

def my_function(*args, **kwargs):
    values_set = set(kwargs.values())
    count = sum(1 for arg in args if arg in values_set)
    return count

# Example usage:
result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)

print(result)