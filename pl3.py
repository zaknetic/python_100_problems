#Write a Python function to reverse a given string and return the reversed string

def reverse_str(s):
    rev = s[::-1]
    return rev

input_str = "ZAKARIA SOIKAIN"
reverse_str = reverse_str(input_str)
print(f"Reversr string:",reverse_str)

txt = "Hello World"[::-1]
print(txt)