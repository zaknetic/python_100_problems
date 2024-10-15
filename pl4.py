#Given a list of integers, write a Python program to convert each element of the list to a string.

#method 1
int_list = [1,2,3,4,5,6]

str_list = []

for num in int_list:
    str_list.append(str(num))

print("List of stering:",str_list)

#method 2

# Given list of integers
int_list = [1, 2, 3, 4, 5]

# Convert each element to a string
str_list = [str(num) for num in int_list]

# Output the result
print("List of strings:", str_list)

#method 3

# Given list of integers
int_list = [1, 2, 3, 4, 5]

# Convert each element to a string using map
str_list = list(map(str, int_list))

# Output the result
print("List of strings:", str_list)


#method 4 
# Given list of integers
int_list = [1, 2, 3, 4, 5]

# Initialize an empty list for strings
str_list = []
index = 0

# Convert each element to a string using a while loop
while index < len(int_list):
    str_list.append(str(int_list[index]))
    index += 1

# Output the result
print("List of strings:", str_list)



