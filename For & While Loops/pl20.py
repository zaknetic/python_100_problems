#Write a Python program using a for loop to calculate
# the sum of the first N natural numbers, where N is 
# taken as input from the user.


n = int(input("Enter a postive integer n:"))

total_sum = 0

if n < 1:
    print("Please enter a positive integer greater than 0.")

else:
    for i in range(1,n+1):
        total_sum += i
    print(f"The sum of the first {n} natural numbers is: {total_sum}")