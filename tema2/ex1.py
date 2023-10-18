# Write a function to return a list of the first n numbers in the Fibonacci string.

def fibonacci(n):
    fibonacci_list = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_list.append(a)
        a, b = b, a + b
    return fibonacci_list

n = 10 
fib_numbers = fibonacci(n)
print(f"The first {n} Fibonacci numbers are: {fib_numbers}")
