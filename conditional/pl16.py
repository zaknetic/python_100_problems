#Write a Python program that takes the time in hours 
# (24-hour format) as input and prints 
# “Good Morning”, “Good Afternoon”, “Good Evening”, 
# or “Good Night” based on the time.


def greeting_based_on_time(hour):
    if 5 <= hour < 12:
        return "Good Moring"
    elif 12<= hour < 17 :
        return "Good Afternoon"
    elif 17<= hour < 21:
        return "Good Evening"
    
    elif (21 <= hour < 24) or (hour == 0):
        return "Good Night"
    else:
        return "Invalid hour. Please enter a time between 0 and 23."
    

def main():
    try:
        hour = int(input("Enter the time in hours (24-hour format): "))
        greeting = greeting_based_on_time(hour)
        print(greeting)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()

    
