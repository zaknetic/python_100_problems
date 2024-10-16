#Write a Python program using a while loop 
# to reverse a given string.

# Function to reverse a string using a while loop
def reverse_string(input_string):
    reversed_string = ""  # Initialize an empty string to hold the reversed string
    index = len(input_string) - 1  # Start from the last index of the string
    
    # Use a while loop to build the reversed string
    while index >= 0:
        reversed_string += input_string[index]  # Append the current character to reversed_string
        index -= 1  # Move to the previous index
    
    return reversed_string  # Return the reversed string

# Example usage
input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print("Original String:", input_str)
print("Reversed String:", reversed_str)
