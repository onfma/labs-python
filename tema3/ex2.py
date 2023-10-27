# Write a function that receives a string as a parameter and returns a dictionary in which 
# the keys are the characters in the character string and the values are the number of occurrences 
# of that character in the given text.

def count_characters(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Example usage:
text = "hello, world!"
char_count = count_characters(text)

print(char_count)
