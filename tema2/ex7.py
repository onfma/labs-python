# Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and the second 
# element will be the greatest palindrome number.

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def find_palindromes(numbers):
    palindrome_count = 0
    greatest_palindrome = None

    for number in numbers:
        if is_palindrome(number):
            palindrome_count += 1
            if greatest_palindrome is None or number > greatest_palindrome:
                greatest_palindrome = number

    return palindrome_count, greatest_palindrome

# Example usage:
numbers = [121, 123, 1331, 45654, 78987, 12321, 54321]
result = find_palindromes(numbers)

print(result)
