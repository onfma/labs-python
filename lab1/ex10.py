# Write a function that counts how many words exists in a text. 
# A text is considered to be form out of words that are separated by only ONE space. 
# For example: "I have Python exam" has 4 words.
def count_words(text):
    words = text.split(" ")
    word_count = len([word for word in words if word.strip()])

    return word_count

text = "I have Python exam"
print(count_words(text))
