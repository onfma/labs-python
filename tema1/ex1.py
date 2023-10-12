# enerati codurile ascii in format hex string pentru un range de litere successive
# range-ul este dat de primul caracter, si numarul de elemente care incepe cu primul caracter

def generate_ascii_hex_range(start_char, n):
    ascii_hex_list = []
    for i in range(n):
        char = chr(ord(start_char) + i)
        ascii_hex = format(ord(char), '02x')  # convertire de la ascii la hex
        ascii_hex_list.append(ascii_hex)
    return ' '.join(ascii_hex_list)

print(generate_ascii_hex_range('0', 10))
print(generate_ascii_hex_range('a', 26))
print(generate_ascii_hex_range('A', 26))
