#Given three variables: `a = ‘100’`, `b = 25`, and `c = ‘10.5’`,
#  write a Python program to perform the following operations and print 
# the results: – Convert `a` to an integer and add it to `b`. – Convert `c` to a float and subtract 
# it from the result of the first operation.
#  – Convert the final result to a string and concatenate it with the string ” is the answer.”


# Given viriable
a = '100'
b = 25
c = '10.5'

# Step 1: Convert `a` to an integer and add it to `b`

resukt_1 = int(a) + b

# Step 2: Convert `c` to a float and subtract it from the result of the first operation

result_2 = str(resukt_1 - float(c))

print(result_2," is answer")

#Method2

a = '100'
b = 25
c = '10.5'

final_res = str((int(a)+b)- float(c))

print(final_res," is Answer")





