# Write a function that extract a number from a text 
# (for example if the text is "An apple is 123 USD", this function will return 123, 
# or if the text is "abc123abc" the function will extract 123). 
# The function will extract only the first number that is found.
def extract_number(input_string):
    number = 0


input_string = input("Enter text: ")
print(extract_number(input_string))