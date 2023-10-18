# Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"The prime numbers in the list are: {find_primes(numbers)}")
