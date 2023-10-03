# Write a script that receives two strings and prints the number of occurrences of the first string in the second.
def count_occurrences(substring, string):
    count = 0
    start = 0
    while True:
        start = string.find(substring, start)  # Find the next occurrence of the substring
        if start == -1:
            break
        count += 1
        start += 1  # Move to the next character

    return count

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
print(count_occurrences(string1, string2))
