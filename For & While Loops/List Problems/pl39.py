#Write a Python program to reverse a given list 
# without using any built-in functions.

def reverse_list(input_list):
    reverse_list = []
    index = len(input_list) - 1

    while index >= 0:
        reverse_list.append(input_list[index])
        index -= 1

    return reverse_list

