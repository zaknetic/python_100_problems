# Given a list of integers, write a Python program
#  using a for loop to find the sum, average, maximum,
#  and minimum values in the list.

numbers = [10,20,30,40,50]

total_sum = 0 
max_value = float('-inf')
min_value = float('inf')
count = 0

for num in numbers:
    total_sum += num
    count += 1
    
    if num > max_value:
        max_value = num
    
    
    if num < min_value:
        min_value = num

# average = total_sum / count if count > 0 else 0

if count > 0:
    average = total_sum / count
else:
    average = 0

print("Sum:", total_sum)
print("Average:", average)
print("Maximum:", max_value)
print("Minimum:", min_value)