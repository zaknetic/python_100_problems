#Write a Python program using a for loop to generate 
#the Fibonacci sequence up to a given limit N.

def fibonacci_sequence(limit):
    fib_seq = []
    a,b = 0,1
    for i in range(limit+1):
        if a > limit:
            break

        fib_seq.append(a)
        a,b = b, a+b
    return fib_seq

N = int(input("Enter the limit N: "))
fib_numbers = fibonacci_sequence(N)
print(f"Fibonacci sequence up to {N}: {fib_numbers}")