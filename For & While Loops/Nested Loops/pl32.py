#Write a Python program using nested loops to multiply 
# two matrices.

A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

B = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

rows_A = len(A)
cols_A = len(A[0])
rows_B = len(B)
cols_B = len(B[0])

if cols_A != rows_B:
    print("Cannot multiply the matrices. The number of columns in A must equal the number of rows in B.")
else: 
     result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

for i in range(rows_A):  # Loop through rows of A
        for j in range(cols_B):  # Loop through columns of B
            for k in range(cols_A):  # Loop through columns of A (or rows of B)
                result[i][j] += A[i][k] * B[k][j]  # Multiply and accumulate

# Print the result
print("Result of A * B:")
for row in result:
    print(row)