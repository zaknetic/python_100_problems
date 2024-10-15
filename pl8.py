#Write a Python function to reverse a given string using slicing.

def reverse_string(s):
    # Reverse the string using slicing
    return s[::-1]

# Example usage
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
