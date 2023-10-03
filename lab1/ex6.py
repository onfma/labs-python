# Write a function that validates if a number is a palindrome.
def is_palindrome(number):
    number_str = str(number)
    reversed_str = number_str[::-1]
    return number_str == reversed_str

# Test the function with a few examples
num1 = 121
num2 = 12321
num3 = 12345

print(f"{num1} is a palindrome: {is_palindrome(num1)}")
print(f"{num2} is a palindrome: {is_palindrome(num2)}")
print(f"{num3} is a palindrome: {is_palindrome(num3)}")
