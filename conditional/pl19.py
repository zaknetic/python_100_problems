# Write a Python program that takes an integer . as input 
# and prints whether the  number falls within the ranges:
# 0-50, 51-100, 101-150, or above 150.

def check_range(number):
    if 0 <= number <= 50:
        return "The number is in the range 0-50."
    elif 51<= number <= 100:
        return "The number is in the range 51-100."
    
    elif 101<= number <= 150:
        return "The number is in the range 101-150."
    elif number > 150:
        return "The number is above 150."
    else:
       return "The number is negative and out of range."

def main() :
    try:
        number = int(input("Enter an integer: "))
        result = check_range(number)
        print(result)

    except ValueError():
         print("Please enter a valid integer.")

if __name__ == "__main__":
    main()

