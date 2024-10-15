#Write a Python program that takes three sides
# of a triangle as input and determines whether
# it forms an equilateral, isosceles, or scalene triangle

def classify_triangle(a,b,c):
    if a <= 0 or b<=0 or c<=0:
        return "Invalid triangle sides"
    
    if a == b == c:  
        return "Equilateral triangle"  
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
         return "Scalene triangle"
    
def main():
    try:
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of side c: "))

        result = classify_triangle(a,b,c)
        print(result)
    except ValueError:
        print("Please enter valid numeric values.")    
if __name__ == "__main__":
    main()