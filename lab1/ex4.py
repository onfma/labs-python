# Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
import re

def camelcase_to_snakecase(input_string):
    snakecase_string = re.sub(r'([a-z])([A-Z])', r'\1_\2', input_string)
    return snakecase_string.lower()

input_string = input("Enter a string in UpperCamelCase: ")
print(camelcase_to_snakecase(input_string))
