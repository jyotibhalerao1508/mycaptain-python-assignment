# Function to generate Fibonacci numbers
def fibonacci(n):
    fib = [0, 1] # Initialize the first two numbers in the sequence
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2]) # Add the previous two numbers to generate the next number in the sequence
    return fib

# Example usage
n = 10 # Number of Fibonacci numbers to generate
fib_numbers = fibonacci(n)
print(fib_numbers)
