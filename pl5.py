#Write a Python program that converts a temperature in Celsius to Fahrenheit. Take the Celsius temperature as input from the user.

#method 1

C = float(input("Enter your Celsius temperature:"))
F = C*(9/5) + 32
print(f"{C} Dgree Celsius conver {F} Fahrenheit .")


#method 2 

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Take Celsius temperature as input from the user
celsius_input = float(input("Enter temperature in Celsius: "))

# Convert the temperature
fahrenheit_output = celsius_to_fahrenheit(celsius_input)

# Output the result
print(f"{celsius_input}°C is equal to {fahrenheit_output}°F")


#method 3

while True:
    # Take Celsius temperature as input from the user
    celsius_input = input("Enter temperature in Celsius (or type 'exit' to quit): ")

    # Allow the user to exit the loop
    if celsius_input.lower() == 'exit':
        print("Exiting the program.")
        break

    # Convert the input to a float
    try:
        celsius_input = float(celsius_input)
        # Convert Celsius to Fahrenheit
        fahrenheit_output = (celsius_input * 9/5) + 32
        # Output the result
        print(f"{celsius_input}°C is equal to {fahrenheit_output}°F")
    except ValueError:
        print("Please enter a valid number.")
