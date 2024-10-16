#Write a Python program using a while loop to 
# calculate the sum of all even numbers 1 and N, 
# where N is taken as input from the user.

N = int(input("Enter a postive integer N:"))

sum_even = 0
current_number = 2

while current_number <= N:
    sum_even += current_number
    current_number +=2

print(f"The sum of all even numbers between 1 and {N} is: {sum_even}")