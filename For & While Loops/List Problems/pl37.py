# Write a Python program to find the 
# maximum and minimum values in a given list of integers.

num = [10,5,3,-20]
if num :
    max = num[0]
    min = num[0]

    for i in num:
        if i> max:
            max = i
        if i<min:
            min = i
    print(max)
    print(min)
else:
    print("empty")