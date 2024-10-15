#Write a Python program using nested loops to print a chessboard pattern 
# (alternating “X” and “O” characters) of size 8×8.34. Number Pyramid: Write a 
# Python program using nested loops to print a number pyramid like the following: 1 22 333 4444 5555
# Move to the next line after each row

size = 8 


for i in range(size):
    for j in range(size):
        if (i+j)%2 == 0:
            print('X',end=' ')
        else:
            print('O',end=' ')
    print()      
print()            


# Print a number pyramid
rows = 5
for i in range(1, rows + 1):  # Loop through rows
    for j in range(i):  # Loop to print the number i, i times
        print(i, end='')  # Print the number without newline
    print()  # Move to the next line after each row
