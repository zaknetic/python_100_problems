# Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.

# Function to check the number
def check_number(n):
    if n > 0 :
        return ("This is a posstive number")
    elif n < 0 :
        return ("This is a negative number")
    else:
        return ("This is a zero")

if __name__ == "__main__":
    try:
        # Take input from the user
        number = float(input("Enter a number: "))
        # Print the result
        result = check_number(number)
        print(result)
    except ValueError:
        print("Please enter a valid number.")


#method 2 
# Main program
if __name__ == "__main__":
    try:
        # Take input from the user
        number = float(input("Enter a number: "))
        
        # Check if the number is positive, negative, or zero
        if number > 0:
            print("The number is positive.")
        if number < 0:
            print("The number is negative.")
        if number == 0:
            print("The number is zero.")
    
    except ValueError:
        print("Please enter a valid number.")
