#Write a Python program using nested for loops
#  to print various patterns, such as a right-angled 
# triangle, an inverted right-angled triangle,
# and so on


def right_angled_triangle(n):
    print("Right-Angled Triangle:")
    for i in range(n):
        print("* " * (i + 1))  # Print i + 1 asterisks

def inverted_right_angled_triangle(n):
    print("\nInverted Right-Angled Triangle:")
    for i in range(n, 0, -1):
        print("* " * i)  # Print i asterisks

def pyramid(n):
    print("\nPyramid:")
    for i in range(n):
        spaces = " " * (n - i - 1)  # Calculate leading spaces
        stars = "* " * (2 * i + 1)  # Calculate stars
        print(spaces + stars)  # Print spaces followed by stars

# Get the height of the patterns from the user
n = int(input("Enter the height of the patterns: "))

right_angled_triangle(n)
inverted_right_angled_triangle(n)
pyramid(n)
