#Write a Python program using a for loop to print 
#the multiplication table of a given number N.
'''
N = int(input("Enter a number to print its multiplication table: "))

print(f"Multiplication table for {N}:")
for i in range(1,11):
    result = N*1
    print(f"{N} x {i} = {result}")'''

while True:
    # Get input from the user
    N = input("Enter a number to print its multiplication table (or type 'exit' to quit): ")

    # Check if the user wants to exit
    if N.lower() == 'exit':
        print("Exiting the program.")
        break

    # Try to convert input to an integer
    try:
        N = int(N)
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Print the multiplication table
    print(f"\nMultiplication table for {N}:")
    for i in range(1, 11):
        result = N * i
        print(f"{N} x {i} = {result}")

    print()  # Print a blank line for better readability
