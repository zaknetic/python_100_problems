#Write a Python program using a while loop
# to check if a given number N is prime or not.


def prime_number(n):
    if n<= 1 :
        return False
    divisor = 2
    while divisor < n :
        if n % divisor == 0 :
            return False
        
        divisor += 1

    return True
number = int(input("Enter a number to check if it is prime: "))
if prime_number(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

