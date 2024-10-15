if __name__ == "__main__":

    try:
        y = int(input("Enter your year:"))

        if y % 4 == 0 and y % 100 != 0:
            print(f"{y} is leap year")
        elif y % 400 == 0:
            print(f"{y} is not leap year")

        else: 
           print(f"{y} is not leap year")

    except ValueError:
         print("Please enter a valid year.")



