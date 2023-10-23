# Write a function that will receive a list of words  as parameter and will return a list of lists of words,
# grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.

def group_by_rhyme(words):
    rhyme_groups = {}

    for word in words:
        rhyme = word[-2:]
        if rhyme in rhyme_groups:
            rhyme_groups[rhyme].append(word)
        else:
            rhyme_groups[rhyme] = [word]

    return list(rhyme_groups.values())

# Example usage:
words = ['ana', 'banana', 'carte', 'arme', 'parte']
rhyme_groups = group_by_rhyme(words)

print(rhyme_groups)
