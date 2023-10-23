# Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.

def custom_sort(tuples):
    def sort_key(item):
        if len(item) >= 2 and len(item[1]) >= 3:
            return item[1][2]
        return ''

    return sorted(tuples, key=sort_key)

# Example usage:
tuples = [('abc', 'bcd'), ('abc', 'zza')]
sorted_tuples = custom_sort(tuples)

print(sorted_tuples)
