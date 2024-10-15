#Write a Python program that takes a student’s percentage 
# as input and prints their corresponding grade according 
# to the following criteria: – 90% or above: A+ – 80-89%: 
# A – 70-79%: B – 60-69%: C – Below 60%: Fail

def determine_grad(percentage):
    if percentage >= 90:
        return "A+"
    
    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"
 
    elif percentage >= 60:
        return "C"

    else:
        return "Fail"

def main():
    try:
        percentage = float(input("Enter the student's percentage: "))
        if percentage < 0 or percentage> 100:
            print("Please enter a valid percentage between 0 and 100.")
        else:
            grade = determine_grad(percentage)
            print(f"The student's grade is: {grade}")

    except ValueError():
        print("Invalid input. Please enter a numeric value.")

if __name__ =="__main__":
    main()