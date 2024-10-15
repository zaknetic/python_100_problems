#Write a Python program to calculate the 
# average of all elements in a given list of integers.

num = [12,13,14,15,16]
total = sum(num)
avg = total/len(num) if num else 0
print(avg)