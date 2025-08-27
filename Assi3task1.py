# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "factorial not defined for  negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
        return result

    # Sample call
    num = 5
    print("Factorial of", num, "is", factorial(num))
