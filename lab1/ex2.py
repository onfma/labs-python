# Write a script that calculates how many vowels are in a string.
def count_vowels(string):
    vowels = set("AEIOUaeiou")
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

input_string = input("Enter a string: ")
print(count_vowels(input_string))