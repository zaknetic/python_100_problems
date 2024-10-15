#Write a Python program that takes
# the coefficients (a, b, c) of a
# quadratic equation as input and 
# calculates and prints the real roots (if they exist)
# or a message indicating the complex roots.

import cmath

def find_roots(a,b,c):
    discriminant = b**2 - 4*a*c

    root1 = (-b + cmath.sqrt(discriminant))/(2*a)
    root2 = (-b - cmath.sqrt(discriminant))/(2*a)

    return root1,root2

def main():
    try:    

        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        if a == 0:
            print("Coefficient 'a' cannot be zero for a quadratic equation.")
            return
        root1, root2 = find_roots(a, b, c)


        if root1.imag == 0 and root2.imag == 0:
            print(f"The roots are real: {root1.real} and {root2.real}")
        else:
            print("The roots are complex.")
            print(f"Root 1: {root1}, Root 2: {root2}")

    except ValueError():
        print("Please enter valid numeric values.")


if __name__ == "__main__" :
    main()       