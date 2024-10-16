#Write a Python program using a while loop to calculate 
#the factorial of a given number N.

def factorial(N):
    if N < 0:
        return "Factorial is not define for negative numbers."
    result = 1
    while N > 1:
        result *= N
        N -= 1
    return result

try:
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {number} is {factorial(number)}.")
except ValueError:
    print("Please enter a valid integer.")