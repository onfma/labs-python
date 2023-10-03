# Find the greatest common divisor of multiple numbers read from the console.
import math

def find_gcd(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = math.gcd(result, num)
    return result

input_str = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in input_str.split()]
print(find_gcd(numbers))
