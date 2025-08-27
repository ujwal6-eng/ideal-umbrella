def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Get user input
num = int(input("Enter a number: "))

# Call the factorial function and print the result
print(f"Factorial of {num} is: {factorial(num)}")

